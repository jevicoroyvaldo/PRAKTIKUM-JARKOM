# LAPORAN PRAKTIKUM JARINGAN KOMPUTER
## Modul 3: Analisis Protokol Lapisan Aplikasi (HTTP)

---

### Profil Praktikan
* **Nama:** Jevico Royvaldo Febriliansyah
* **NIM:** 103072400151
* **Kelas:** IF-04-01

---

## A. Deskripsi Praktikum
Praktikum ini bertujuan untuk menganalisis mekanisme kerja protokol HTTP (*Hypertext Transfer Protocol*) menggunakan perangkat lunak Wireshark. Fokus analisis meliputi interaksi dasar, optimasi cache, segmentasi data pada layer transport, serta aspek keamanan pada transmisi kredensial.

---

## B. Hasil Eksperimen & Analisis

### 1. Interaksi Dasar HTTP GET & Response
**Langkah:** Mengakses file HTML statis pertama untuk melihat header standar.
* **Hasil:** Client mengirim `GET` (Paket #279) dan server merespons dengan `200 OK` (Paket #288).
* **Analisis:** Header `User-Agent` menunjukkan identitas browser yang digunakan dalam sesi ini.

![Basic GET](<W3/1. Basic GET.png>)

### 2. Mekanisme Conditional GET (Caching)
**Langkah:** Melakukan refresh pada browser untuk memicu validasi cache.
* **Hasil:** Server mengirimkan status **304 Not Modified** (Paket #769).
* **Analisis:** Header `If-Modified-Since` pada permintaan kedua membuktikan browser mencoba menggunakan data lokal untuk menghemat bandwidth.

![Conditial GET](<W3/2. Conditional GET.png>)

### 3. Penanganan Dokumen Berukuran Besar (Long Document)
**Langkah:** Mengambil dokumen yang ukurannya melebihi kapasitas standar segmen jaringan.
* **Hasil:** Terdeteksi keterangan **[3 Reassembled TCP Segments]**.
* **Analisis:** File berukuran 4864 bytes dipecah menjadi 3 segmen TCP (#372, #374, #375) sebelum akhirnya disatukan kembali oleh protokol HTTP.

![Long Document](<W3/3. Long Document.png>)

### 4. Objek Tersemat (Embedded Objects)
**Langkah:** Mengakses halaman yang mengandung beberapa file gambar.
* **Hasil:** Terjadi beberapa permintaan `GET` terpisah untuk file `.html`, `.png`, dan `.jpg`.
* **Analisis:** Browser secara otomatis melakukan *request* tambahan untuk setiap elemen visual yang tersemat dalam kode HTML.

![Embedded Objects](Screenshot 2026-04-13 195004.png)

### 5. Investigasi Keamanan Autentikasi HTTP
**Langkah:** Mengamati transmisi login pada halaman yang diproteksi password.
* **Hasil:** Kredensial login dapat terlihat jelas pada header `Authorization`.
* **Analisis:** HTTP mengirimkan data `wireshark-students:network` dalam format Base64 yang tidak terenkripsi, sehingga sangat rentan terhadap penyadapan.

![HTTP Authentication](authentication.png)

---

## C. Kesimpulan    
1. **Request-Response:** Protokol HTTP bekerja secara sinkron di mana setiap permintaan klien mendapatkan kepastian status dari server (seperti 200 OK atau 304).
2. **Efisiensi:** Fitur *Conditional GET* secara efektif mengurangi beban server dengan memanfaatkan cache browser.
3. **Ketergantungan TCP:** Keberhasilan transmisi file besar sangat bergantung pada kemampuan TCP dalam melakukan segmentasi dan penyusunan kembali (*reassembly*).
4. **Keamanan:** Penggunaan HTTP murni tanpa enkripsi (TLS/SSL) memiliki risiko keamanan tinggi karena data sensitif terkirim secara terbuka.