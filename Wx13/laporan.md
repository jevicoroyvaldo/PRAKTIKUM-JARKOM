# **LAPORAN PRAKTIKUM JARINGAN KOMPUTER**
## **MODUL 13: ETHERNET DAN ADDRESS RESOLUTION PROTOCOL (ARP)**

### **Identitas Mahasiswa**
* **Nama Lengkap:** Jevico Royvaldo
* **Nomor Induk Mahasiswa (NIM):** 103072400151
* **Kelas:** IF-04-01

---

## A. Ruang Lingkup & Tujuan Praktikum
1. Menganalisis secara mendalam arsitektur data dan mekanisme kerja lapisan Data Link (*Ethernet Frame*).
2. Menginvestigasi siklus hidup pertukaran pesan pada protokol ARP (*Address Resolution Protocol*) dalam memetakan alamat logika (IP) ke alamat fisik (MAC) menggunakan Wireshark.

---

## B. Metodologi & Langkah Kerja 

### 1. Perekaman Arsitektur Frame Ethernet
1. Bersihkan seluruh riwayat penjelajahan dan data *cache* pada aplikasi peramban web (*browser*) untuk memastikan transmisi data bermula dari kondisi kosong.
2. Jalankan aplikasi **Wireshark** dan aktifkan fitur *packet capture* pada kartu jaringan yang sedang aktif berinteraksi dengan internet.
3. Akses tautan laboratorium jaringan berikut: `http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html`.
4. Pastikan dokumen teks "Bill of Rights AS" termuat secara utuh pada layar peramban.
5. Hentikan perekaman lalu lintas di Wireshark untuk memulai proses pembedahan parameter *frame* Ethernet.

### 2. Inspeksi Tabel Cache ARP Lokal
1. Buka jendela terminal **Command Prompt** (CMD) pada sistem operasi Windows.
2. Eksekusi perintah pemeriksaan pemetaan memori:
   ```bash
   arp -a