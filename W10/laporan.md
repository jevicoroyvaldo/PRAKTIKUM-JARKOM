# LAPORAN TUGAS PRAKTIKUM JARINGAN KOMPUTER
## MODUL 10: ANALISIS INTERNET PROTOCOL (IP)

### Komponen Data Mahasiswa
* **Nama Lengkap:** Jevico Royvaldo
* **NIM:** 103072400151
* **Kelas:** IF-04-01

---

## A. Capaian Praktikum
1. Mampu mengamati, membedah, dan menganalisis mekanisme kerja serta anatomi protokol IP (Internet Protocol) menggunakan perangkat lunak Wireshark.

---

## B. Ringkasan Materi
Secara garis besar, materi pada modul ini dibagi ke dalam tiga tahapan analisis. Tahap pertama difokuskan pada pelacakan struktur paket IPv4 yang dipicu oleh operasional utilitas penelusuran rute jaringan (*traceroute*). Tahap kedua membahas secara mendalam perilaku pemecahan paket data (*IP fragmentation*) ketika muatan melebihi ambang batas fisik saluran transmisi. Tahap akhir akan mengulas karakteristik arsitektur pengalamatan generasi terbaru, yakni IPv6.

---

## C. Hasil Pengamatan dan Bedah Paket

### 1. Eksplorasi Fondasi IPv4 (Traceroute & TTL)
**Tujuan Kegiatan:** Mengamati susunan field pada header paket IPv4 serta menganalisis peran fungsional parameter *Time-to-Live* (TTL) dalam menentukan batas masa aktif paket lewat perintah *traceroute*/*tracert*.

**Analisis & Ulasan:**
Program *traceroute* bekerja dengan cara memetakan rentetan lompatan (*hop*) dari komputer pengirim menuju host target. Mekanisme pelacakan ini memanfaatkan manipulasi nilai *Time-to-Live* (TTL) pada lapisan header IPv4 yang dinaikkan secara bertahap mulai dari angka 1. Setiap kali paket melintasi sebuah perangkat *router*, nilai TTL tersebut akan dipotong (dikurangi) sebesar 1 angka. Jika nilai TTL habis (mencapai angka 0) sebelum paket sukses menyentuh komputer tujuan, *router* di lokasi tersebut terpaksa membuang paket data itu dan mengirimkan sinyal notifikasi kesalahan berupa *ICMP Time-to-live exceeded* kembali ke komputer asal. Melalui respons balik inilah, aplikasi Wireshark dan terminal klien dapat mengidentifikasi serta mencatat barisan alamat IP *router* perantara secara berurutan.

---

### 2. Mekanisme Pemecahan Paket (IP Fragmentation)
**Tujuan Kegiatan:** Menginvestigasi perilaku protokol IPv4 dalam mengelola fragmentasi data ketika ukuran datagram yang dikirimkan melampaui batasan kapasitas angkut maksimum jaringan atau *Maximum Transmission Unit* (MTU).

**Analisis & Ulasan:**
Apabila jaringan dipaksa mentransmisikan sebuah datagram berukuran masif (misalkan bermuatan 3000 *byte*), data tersebut tidak dapat dikirim secara utuh akibat batasan *Maximum Transmission Unit* (MTU) pada tautan fisik yang umumnya mentok di angka 1500 *byte*. Berdasarkan pengamatan log paket di Wireshark, *router* secara otomatis akan membagi dokumen besar tersebut menjadi beberapa fragmen kecil terpisah. 

Pada struktur header IPv4 fragmen awal, parameter *field* **Flags** pada bit **More fragments** akan berstatus **Set (1)**, yang mengindikasikan bahwa paket ini merupakan serpihan pecahan dan masih ada potongan data selanjutnya yang akan menyusul. Kolom **Fragment Offset** yang menunjukkan angka 0 menandakan posisinya sebagai blok pembuka (himpunan *byte* pertama). Agar seluruh pecahan ini tidak tertukar saat dirakit ulang (*reassembly*) di sisi penerima, setiap potongan dibekali nilai penanda yang sama pada kolom **Identification** (contohnya `0x0045`), sehingga komputer tujuan dapat menyatukannya kembali menjadi dokumen utuh yang valid.

---

### 3. Karakteristik Protokol IPv6
**Tujuan Kegiatan:** Menganalisis susunan struktur header, format skema pengalamatan baru, serta proses resolusi nama domain yang dikembangkan pada Internet Protocol version 6 (IPv6).

**Analisis & Ulasan:**
Analisis paket IPv6 ini ditinjau dari lalu lintas penarikan data DNS tipe *Standard Query AAAA* untuk memetakan domain seperti `youtube.com`. Berbeda dengan IPv4 yang mengandalkan query *record A*, infrastruktur jaringan berbasis IPv6 membutuhkan *record AAAA* agar nama domain dapat diterjemahkan ke dalam bentuk alamat IP generasi keenam. 

Bila diteliti melalui jendela rincian header IPv6, tampak perbedaan arsitektur yang sangat radikal pada kolom *Source Address* dan *Destination Address*. Format alamat tidak lagi menggunakan susunan angka desimal 32-bit yang dipisahkan titik, melainkan barisan string panjang 128-bit yang ditulis menggunakan kombinasi karakter heksadesimal dan dipisahkan oleh tanda titik dua (*colon*). Desain header IPv6 ini dibuat lebih efisien dan ringkas dari segi struktur, namun menawarkan ruang alokasi alamat yang sangat luas demi mengatasi krisis habisnya kuota alamat IP global pada sistem IPv4 konvensional.

---

## D. Kesimpulan Akhir
Berdasarkan aktivitas pengujian dan pembedahan lalu lintas data IP (IPv4 & IPv6) menggunakan Wireshark, dapat diambil kesimpulan sebagai berikut:

1. **Kendali Perputaran Paket:** Protokol IP memanfaatkan kolom *Time-to-Live* (TTL) sebagai instrumen pengontrol agar paket tidak berputar selamanya di dalam jaringan jika terjadi malfungsi rute. Pola peningkatan TTL secara bertahap oleh utilitas *traceroute* terbukti efektif merangsang *router* memicu pesan *ICMP Time-to-live exceeded (Type 11)* guna memetakan topologi jalur koneksi.
2. **Pemicu Fragmentasi:** Pembagian paket data (*fragmentation*) secara otomatis diinisiasi oleh sistem manakala ukuran data payload yang dikirimkan melebihi ambang batas kapasitas fisik saluran (*link* MTU). Proses pemotongan berkas ini dieksekusi secara mandiri oleh perangkat *router* yang menjembatani jalur tersebut.
3. **Penyusunan Ulang Dokumen:** Proses rekonstruksi serpihan data di sisi komputer penerima sangat bergantung pada tiga parameter utama di dalam header IPv4, yaitu *Identification* (kode pencocokan fragmen), *Flags* (indikator keberadaan pecahan lanjutan), serta *Fragment Offset* (penunjuk posisi urutan *byte* data).
4. **Revolusi Arsitektur IPv6:** Peralihan menuju sistem IPv6 merombak total identitas penomoran komputer dari format lama 32-bit menjadi 128-bit berbasis heksadesimal, menyajikan solusi jangka panjang terhadap keterbatasan jumlah IP di era modern.
5. **Konektivitas DNS Global:** Layanan penamaan domain (DNS) telah terintegrasi penuh mendukung ekosistem IPv6 melalui penyediaan kueri *record AAAA*, yang bekerja mirip dengan *record A* standar namun khusus memetakan domain ke bentuk rantai alamat heksadesimal 128-bit.