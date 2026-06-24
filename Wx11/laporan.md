# LAPORAN HASIL PRAKTIKUM JARINGAN KOMPUTER
## MODUL 11: ANALISIS DINAMIKA PROTOKOL DHCP

### Komponen Data Mahasiswa
* **Nama Lengkap:** Jevico Royvaldo
* **NIM:** 103072400151
* **Kelas:** IF-04-01

---

## A. Capaian Praktikum
1. Mengamati, membedah, dan memahami tahapan pertukaran paket data pada protokol DHCP (Dynamic Host Configuration Protocol) menggunakan bantuan Wireshark.

---

## B. Prosedur Eksperimen
1. Membuka antarmuka *Command Prompt* (CMD) pada sistem operasi Windows.
2. Mengeksekusi instruksi `ipconfig /release` guna melepaskan konfigurasi alamat IP yang sedang aktif.
3. Mengaktifkan fitur penyadapan paket (*capture*) pada Wireshark dengan memilih kartu jaringan yang sedang tersambung (Wi-Fi).
4. Menjalankan perintah `ipconfig /renew` untuk menuntut alokasi alamat IP baru dari jaringan.
5. Menghentikan proses perekaman data Wireshark begitu komputer berhasil mengamankan alamat IP baru.
6. Menyaring lalu lintas data di Wireshark menggunakan keyword filter `bootp`.

---

## C. Hasil Pengamatan dan Bedah Paket

### 1. Log Arus Lalu Lintas DHCP

**Display Filter:** `bootp`

![DHCP Overview](Bbb.jpg)

**Tabel Rekaman Transmisi Data:**

| No. Frame | Waktu Muncul | Tipe Pesan (Message Type) | IP Asal (Source) | IP Tujuan (Destination) | Kode Transaksi (Transaction ID) |
|-------|-------|--------------|--------|-------------|----------------|
| 83 | 3.65s | DHCP Discover | 0.0.0.0 | 255.255.255.255 | 0x12b91479 |
| 146 | 5.80s | DHCP Offer | 192.168.100.1 | 255.255.255.255 | 0x12b91479 |
| 147 | 5.81s | DHCP Request | 0.0.0.0 | 255.255.255.255 | 0x12b91479 |
| 148 | 5.91s | DHCP ACK | 192.168.100.1 | 255.255.255.255 | 0x12b91479 |
| 401 | 11.49s | DHCP Request | 192.168.100.31 | 192.168.100.1 | 0x1a9df1b3 |
| 403 | 11.55s | DHCP ACK | 192.168.100.1 | 192.168.100.31 | 0x1a9df1b3 |

**Catatan Log:**
* Urutan data dari Frame 83 sampai 148 mencerminkan siklus jabat tangan DORA awal sebagai akibat langsung dari perintah `ipconfig /renew`.
* Frame 401 dan 403 merepresentasikan tahapan pembaruan durasi hak sewa (*renewal process*).
* Empat paket inisiasi pertama beroperasi di bawah satu payung sesi yang sama, ditandai oleh kesamaan *Transaction ID* (**0x12b91479**).

---

### 2. Pembedahan DHCP Discover (Frame 83)

![DHCP Discover](Aaa.png)

**Rincian Parameter Atribut:**
```text
Message type: Boot Request (1) - Discover
Transaction ID: 0x12b91479
Client MAC address: Intel_13:13:13:6b (70:9c:d1:13:13:6b)
Client IP address: 0.0.0.0 (Kondisi Kosong / Belum Beridentitas)

Options:
  (53) DHCP Message Type: Discover (1)
  (61) Client identifier
  (12) Host Name: DESKTOP-3NDRVUR
  (55) Parameter Request List:
    - Subnet Mask (1)
    - Router (3)
    - Domain Name Server (6)
    - Domain Name (15)