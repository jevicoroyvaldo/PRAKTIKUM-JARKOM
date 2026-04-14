# LAPORAN PRAKTIKUM JARINGAN KOMPUTER - MODUL 2
## Analisis Lalu Lintas Data Menggunakan Wireshark

---

### Identitas Mahasiswa
* **Nama:** Jevico Royvaldo Febriliansyah
* **NIM:** 103072400151
* **Kelas:** IF-04-01

---

## A. Tujuan Praktikum
1. Melakukan instalasi dan konfigurasi aplikasi Wireshark sebagai *packet sniffer*.
2. Mengamati dan mengidentifikasi struktur paket data yang bertukar dalam jaringan.

## B. Metodologi
Praktikum dilakukan dengan memantau *interface* jaringan aktif (Wi-Fi) saat mengakses situs web `gaia.cs.umass.edu`. Pencarian paket dipermudah dengan menggunakan fitur **Display Filter** dengan *keyword* `http`.

---

## C. Hasil Analisis Paket
Berdasarkan pengamatan pada jendela *Packet-Listing* dan *Packet-Contents*, ditemukan rincian sebagai berikut:

### 1. Identifikasi HTTP GET (Request)
* **Nomor Paket:** 391
* **Alamat IP Sumber:** `192.168.100.113` (Perangkat Praktikan) 
* **Alamat IP Tujuan:** `128.119.245.12` (Server UMass)
* **Protokol:** HTTP
* **Informasi:** `GET /wiresharklabs/INTRO-wireshark-file1.html HTTP/1.1`
![Filter HTTP Berhasil](<Screenshot 2026-04-13 183053.png>)

### 2. Identifikasi HTTP Response
* **Nomor Paket:** 397
* **Status:** `301 Moved Permanently`
* **Analisis:** Server memberitahukan bahwa lokasi file yang diminta telah berpindah secara permanen.
![Detail Paket GET](<Screenshot 2026-04-13 183654.png>)

---

## D. Analisis Data Payload
Pada bagian **Packet-Contents Window**, data mentah ditampilkan dalam format **Heksadesimal** dan **ASCII**. 
* Di sisi kanan (ASCII), terlihat teks permintaan browser secara transparan.
* Detail seperti `Host` dan `User-Agent` dapat dibaca dengan jelas, menunjukkan bahwa protokol HTTP (tanpa enkripsi) mengirimkan data dalam bentuk teks biasa.

---

## E. Kesimpulan
1. Wireshark berhasil digunakan untuk menangkap paket data secara pasif tanpa mengganggu koneksi.
2. Penggunaan filter `http` sangat membantu dalam memisahkan paket spesifik dari git add .ribuan lalu lintas data lainnya.
3. Analisis paket nomor 391 membuktikan adanya pengiriman data dari komputer praktikan ke server tujuan dengan rincian IP dan metode request yang valid.