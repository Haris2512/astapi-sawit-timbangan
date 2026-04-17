# Timbangan Sawit API - Manajemen Logistik Hasil Panen

**Proyek Ujian Tengah Semester (UTS)**

- **Mata Kuliah:** Pemrograman Web Lanjutan
- **Nama:** Haris
- **NIM:** H071241070

---

## Deskripsi Proyek

**Timbangan Sawit API** adalah layanan *backend* RESTful API berbasis modular yang dibangun menggunakan *framework* **FastAPI**. Sistem ini dirancang untuk mendigitalisasi pencatatan hasil panen sawit, mulai dari manajemen data petani hingga laporan timbangan harian.

Sistem ini menerapkan relasi database *One-to-Many* antara entitas `Petani` dan `Transaksi` serta dilengkapi dengan fitur **Dashboard Statistik** untuk analisis data secara cepat.

## Fitur Utama

- **Manajemen Petani (CRUD):** Tambah, lihat, dan kelola data petani sawit.
- **Catatan Timbangan:** Input berat tonase dan kualitas sawit yang terhubung otomatis ke ID petani.
- **Dashboard Statistik:** Fitur agregasi (Nilai Tambah) yang menampilkan total tonase masuk, jumlah petani, dan rata-rata berat timbangan.
- **Keamanan JWT:** Sistem *login* admin menggunakan token Bearer (JWT) untuk melindungi akses ke *endpoint* krusial.
- **Dokumentasi Interaktif:** Swagger UI aktif secara otomatis di rute `/docs` untuk pengujian API secara instan.

## Struktur Direktori

Sistem dirancang menggunakan arsitektur modular untuk memisahkan domain layanan:

```text
sawit_api/
├── main.py              # Entry point aplikasi & Logika Dashboard
├── database.py          # Konfigurasi engine dan session SQLite
├── models.py            # Definisi tabel (User, Petani, Transaksi)
├── routers/
│   ├── auth.py          # Router Autentikasi (Register/Login)
│   ├── petani.py        # Router CRUD Manajemen Petani
│   └── transaksi.py     # Router Catatan Timbangan
├── requirements.txt      # Daftar pustaka/library Python
└── README.md            # Dokumentasi proyek
```
## Instalasi dan Setup
### 1. Clone Repositori
```
git clone https://github.com/Haris2512/astapi-sawit-timbangan.git
cd astapi-sawit-timbangan
```
### 2. Instal Dependensi
```
pip install -r requirements.txt
```
### 3. Jalankan Aplikasi
```
uvicorn main:app --reload
```
### 4. Akses Dokumentasi
```
http://localhost:8000/docs
```
