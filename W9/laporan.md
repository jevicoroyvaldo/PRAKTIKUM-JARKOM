# LAPORAN TUGAS PRAKTIKUM JARINGAN KOMPUTER
## MODUL 9: PENGEMBANGAN APLIKASI WEB SERVER

### Komponen Data Mahasiswa
* **Nama Lengkap:** Jevico Royvaldo
* **NIM:** 103072400151
* **Kelas:** IF-04-01

---

## A. Capaian Praktikum
1. Merancang dan mengimplementasikan program *web server* berskala mikro memanfaatkan pemrograman soket berbasis protokol TCP. 

---

## B. Analisis Teoretis
Secara prinsip, *web server* ialah aplikasi di sisi server yang bertugas memproses dan memberikan jawaban atas dokumen atau berkas yang diminta (HTTP *request*) oleh perangkat klien melalui media peramban (*web browser*). Dalam pelaksanaan praktikum ini, simulasi perangkat *web server* dibangun menggunakan skrip pemrograman Python yang berjalan di atas fondasi koneksi andal TCP.

Urutan operasional internal yang terjadi pada sistem *web server* ini meliputi langkah berikut:
1. Membentuk instansiasi soket berorientasi aliran data TCP via parameter `SOCK_STREAM`.
2. Melakukan penguncian (*binding*) soket pada kombinasi nomor port dan alamat lokal komputer.
3. Menempatkan soket ke dalam fase pasif (*listening*) untuk mengantrekan request dari luar.
4. Mengeksekusi instruksi `accept` saat klien terhubung untuk melahirkan saluran komunikasi privat berupa soket sesi khusus.
5. Membaca kiriman paket *request* HTTP yang dilepaskan oleh browser klien.
6. Membedah susunan string *request* guna mengidentifikasi berkas (*path file*) yang dicari oleh pengguna.
7. Membuka dan mengekstrak isi dokumen HTML yang ditargetkan dari media penyimpanan lokal.
8. Menyusun struktur pesan balasan (*HTTP response*) dengan menyematkan kode status formal (seperti `200 OK` jika dokumen tersedia, atau `404 Not Found` bila dokumen absen) diikuti dengan payload isi teks berkas.
9. Menyalurkan kembali paket *response* tersebut ke peramban klien melewati soket sesi privat.
10. Melakukan terminasi soket komunikasi secara bersih setelah siklus pengiriman selesai.

Logika program juga dikondisikan untuk melempar kode kegagalan standar "404 Not Found" jika berkas yang diakses oleh klien tidak dapat ditemukan di direktori penyimpanan server.

---

## C. Alur Kerja dan Implementasi Kode

**1. Pembuatan Dokumen Sumber HTML** Langkah awal adalah menyediakan file HTML sederhana yang nantinya akan menjadi objek pengetesan penarikan berkas oleh browser.

**Nama File:** `HelloWorld.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>Web server Python berhasil.</p>
</body>
</html>