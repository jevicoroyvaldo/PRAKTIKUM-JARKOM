markdown_content = """# LAPORAN PRAKTIKUM JARINGAN KOMPUTER - MODUL 7
## SOCKET PROGRAMMING: MEMBUAT APLIKASI JARINGAN

### Identitas Mahasiswa
* **Nama:** Jevico Royvaldo
* **NIM:** 103072400151
* **Kelas:** IF-04-01

---

## A. Tujuan Praktikum
1. Memahami arsitektur komunikasi *Client-Server* pada lapisan aplikasi (*Application Layer*).
2. Mampu mengimplementasikan pemrograman jaringan berbasis *Socket* menggunakan protokol UDP (*User Datagram Protocol*).
3. Mampu mengimplementasikan pemrograman jaringan berbasis *Socket* menggunakan protokol TCP (*Transmission Control Protocol*).

---

## B. Dasar Teori
### 1. Definisi dan Alur Kerja Socket
*Socket* merupakan sebuah abstraksi perangkat lunak yang bertindak sebagai antarmuka (*endpoint*) komunikasi logis antar proses atau aplikasi yang berjalan di dalam jaringan. Dalam arsitektur *Client-Server*, terdapat fungsi standar penyusun jaringan:
* **Bind:** Mengikat objek *socket* dengan kombinasi alamat IP lokal dan nomor *port* spesifik agar server bisa dikenali.
* **Listen (Khusus TCP):** Mengondisikan *socket* server agar masuk ke mode siaga menunggu datangnya permintaan koneksi dari luar.
* **Accept (Khusus TCP):** Menyetujui permintaan jabat tangan dari klien dan melahirkan sebuah objek *socket* baru yang didedikasikan khusus untuk melayani sesi komunikasi klien tersebut.
* **Connect (Khusus TCP):** Instruksi aktif dari sisi klien untuk menginisiasi pembuatan sesi interaktif penuh dengan pihak server tujuan.

### 2. Matriks Komparasi Protokol UDP vs TCP
Berdasarkan standar pemodelan transportasi data, berikut perbedaan mendasar kedua protokol:

| Parameter | UDP (*User Datagram Protocol*) | TCP (*Transmission Control Protocol*) |
| :--- | :--- | :--- |
| **Konektivitas** | *Connectionless* (Tanpa pembuatan sesi) | *Connection-oriented* (Berbasis koneksi) |
| **Keandalan** | Tidak andal (*Unreliable* / *Best Effort*) | Sangat Andal (*Reliable Transmission*) |
| **Mekanisme Umpan Balik** | Tidak memerlukan ACK (*Acknowledgement*) | Wajib menggunakan ACK dan kontrol aliran |
| **Integritas Data** | Paket berisiko hilang atau tidak berurutan | Paket dijamin berurutan dan bebas galat |
| **Metode Pengiriman** | Berbasis Pesan Terpisah (*Datagram*) | Berbasis Aliran Data Berkelanjutan (*Byte Stream*) |

---

## C. Implementasi Socket UDP

### 1. Kode Program Server UDP (`UDPServer.py`)
Berikut adalah baris instruksi untuk mengaktifkan layanan penerima pesan berbasis UDP pada port `12000`: