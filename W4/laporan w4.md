# LAPORAN PRAKTIKUM JARINGAN KOMPUTER - MODUL 4

## Domain Name System (DNS)

### Identitas Mahasiswa
* **Nama:** Jevico Royvaldo Febriliansyah
* **NIM:** 103072400151
* **Kelas:** IF - 04 - 01

---

### A. Tujuan Praktikum
Dapat menginvestigasi cara kerja protokol DNS (Domain Name System) menggunakan alat bantu nslookup dan Packet Sniffer (Wireshark).

### B. Pengantar
DNS memegang peranan penting di internet sebagai penerjemah nama host ke alamat IP agar lebih mudah diingat oleh manusia. Modul ini membahas cara kerja DNS secara khusus di sisi klien. Secara garis besar, tugas klien adalah mengirimkan permintaan (query) ke server DNS lokal dan menerima hasilnya (response). Klien tidak perlu mengetahui kerumitan yang terjadi di baliknya, yaitu ketika server-server DNS hierarkis saling berkomunikasi secara rekursif atau iteratif untuk meresolusi alamat IP yang diminta.

---

### C. Hasil dan Pembahasan

#### 1. Nslookup
Nslookup adalah alat yang memungkinkan sebuah host untuk meminta dan mendapatkan data dari server DNS. Server yang dituju bisa bermacam-macam tingkatan, seperti server DNS root, top-level domain (TLD), atau otoritatif.

**a. nslookup www.mit.edu**
![1a. Resolusi Dasar](1a.%20Resolusi%20Dasar.png)
**Analisis:**
Jawaban dari perintah ini menunjukkan dua hal:
1. Nama dan alamat IP server DNS lokal yang memberikan jawaban (dalam kasus ini router lokal).
2. Jawaban dari perintah tersebut, berupa CNAME (alias) `e9566.dscb.akamaiedge.net` dan alamat IP asli `23.217.163.122`.

**b. nslookup –type=NS mit.edu**
![1b. Mencari Name Server](1b.%20Mencari%20Name%20Server.png)
**Analisis:**
Perintah ini meminta server DNS lokal untuk mencari Name Server (NS) otoritatif milik MIT. "Non-authoritative answer" artinya informasi didapatkan dari cache server DNS perantara. Hasil menampilkan daftar server seperti `asia1.akam.net` yang bertanggung jawab atas domain tersebut.

**c. Query ke DNS Server Tertentu (Google DNS)**
![1c. Mencari Server Korea](1c.%20Mencari%20Server%20Korea.png)
**Analisis:**
Eksekusi `nslookup www.aiit.or.kr 8.8.8.8` memaksa laptop mengirim query langsung ke server Google, mengabaikan DNS lokal. Hal ini berguna untuk memastikan resolusi domain dari sudut pandang server DNS publik global.

**d. Query DNS Otoritatif Oxford (NS Record)**
![1d. Mencari Name Server Oxford](1d.%20Mencari%20Name%20Server%20Oxford.png)
**Analisis:**
Query ini menghasilkan daftar 6 (enam) server DNS otoritatif yang mengelola domain `ox.ac.uk`. Server-server inilah yang memegang database asli alamat IP untuk universitas tersebut.

**e. Query MX Record (Server Email)**
![1e. Mencari Server Email](1e.%20Mencari%20Server%20Email.png)
**Analisis:**
Parameter `-type=MX` digunakan untuk mencari Mail Exchanger. Terlihat MX preference = 4 yang menentukan prioritas server email `oxforduni.in.tmes.trendmicro.eu`. Semakin kecil angkanya, semakin tinggi prioritasnya.

---

#### 2. Ipconfig
Perintah ini menyajikan detail konfigurasi TCP/IP yang aktif pada sistem.

**a. ipconfig /all**
![2a (Detail Jaringan)](2a%20(Detail%20Jaringan).png)
**Analisis:**
Melalui perintah ini, praktikan dapat mengidentifikasi alamat IPv4 laptop (`192.168.100.113`) dan alamat DNS Server lokal (`192.168.100.1`) yang digunakan untuk meneruskan query DNS.

**b. ipconfig /displaydns**
![2b (Cek Cache DNS)](2b%20(Cek%20Cache%20DNS).png)
**Analisis:**
Menampilkan record DNS yang tersimpan di memori lokal laptop. Terdapat nilai TTL (Time to Live) dalam satuan detik yang menunjukkan kapan data tersebut akan dihapus dari cache.

---

#### 3. Tracing DNS dengan Wireshark

**a. DNS Query (Permintaan)**
![3a Detail DNS Query](3a%20Detail%20DNS%20Query.png)

**Pertanyaan dan Jawaban:**
* **Apakah pesan tersebut dikirimkan melalui UDP atau TCP?**
  Pesan permintaan DNS dikirimkan melalui protokol **UDP**.
* **Apa port tujuan pada pesan permintaan DNS?**
  Port tujuan (Destination Port) pada pesan permintaan (Frame 1128) adalah **53** (port standar DNS).
* **Berapa banyak "jawaban" pada pesan permintaan?**
  Pesan permintaan tidak mengandung jawaban (Answers: 0), karena ini adalah tahap bertanya.
* **Apa "jenis" pesan tersebut?**
  Jenis (type) adalah **Tipe A**, yang berarti laptop meminta alamat IPv4 untuk domain `www.google-analytics.com`.

**b. DNS Response (Jawaban)**
![3b. Wireshark Response](3b.%20Wireshark%20Response.png)

**Pertanyaan dan Jawaban:**
* **Berapa banyak "jawaban" atau "answers" yang terdapat di dalamnya?**
  Terdapat **6 jawaban** (Answer RRs: 6).
* **Apa saja isi yang terkandung dalam setiap jawaban tersebut?**
  Isi jawaban berupa daftar alamat IPv4 untuk domain yang diminta, salah satunya adalah `142.251.10.102`.
* **Apakah host perlu mengirimkan permintaan DNS baru setiap kali ingin mengakses suatu gambar?**
  Tidak perlu. Alamat IP akan disimpan dalam cache lokal selama durasi TTL masih berlaku, sehingga permintaan berikutnya akan mengambil data dari memori laptop tanpa harus bertanya ke server lagi.

---

### D. Kesimpulan
Praktikum ini berhasil memvisualisasikan cara kerja DNS sebagai protokol krusial dalam jaringan. Melalui `nslookup`, praktikan dapat membedakan berbagai tipe record (A, NS, MX). Analisis Wireshark menunjukkan bahwa DNS beroperasi pada layer aplikasi menggunakan protokol transpor UDP demi kecepatan, di mana setiap jawaban dilengkapi dengan TTL untuk efisiensi melalui mekanisme caching.