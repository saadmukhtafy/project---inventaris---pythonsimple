# project---inventaris---pythonsimple
## 🚀 Cara Menjalankan Aplikasi

Ada dua cara untuk mendapatkan aplikasi ini, yaitu melalui Download ZIP atau Git Clone.

### 1. Persiapan

Sebelum menjalankan aplikasi, pastikan komputer sudah memiliki:

- Python (disarankan Python 3).
- Tkinter sebagai library untuk tampilan aplikasi.
- Editor kode seperti Visual Studio Code (opsional).

### 2. Download Aplikasi dari GitHub (Tanpa Clone)

1. Buka halaman repositori GitHub.
2. Klik tombol **Code**.
3. Pilih **Download ZIP**.
4. Tunggu hingga proses download selesai.
5. Ekstrak file ZIP yang sudah diunduh.
6. Buka folder hasil ekstraksi.
7. Jalankan terminal atau CMD di dalam folder tersebut.

Kemudian jalankan:

```bash
python main.py
```

### 3. Menggunakan Git Clone

Jika Git sudah terinstal, aplikasi juga bisa diunduh menggunakan perintah berikut:

```bash
git clone URL_REPOSITORY
```

Masuk ke folder aplikasi:

```bash
cd Manajemen-Inventaris
```

Jalankan aplikasi:

```bash
python main.py
```

### 4. Instalasi Tkinter

Tkinter merupakan library Python yang digunakan untuk membuat tampilan antarmuka grafis (GUI).

Apabila Tkinter belum tersedia di komputer, ikuti langkah instalasi sesuai sistem operasi yang digunakan.

#### A. Windows

Pada Windows, Tkinter biasanya sudah tersedia ketika menginstal Python dari situs resminya.

Langkah-langkah:

1. Download Python melalui https://www.python.org/downloads/
2. Jalankan installer Python.
3. Pastikan komponen **Tcl/Tk and IDLE** dipilih.
4. Selesaikan proses instalasi.
5. Buka CMD atau terminal.
6. Periksa apakah Tkinter sudah tersedia dengan perintah:

```bash
python -m tkinter
```

Jika berhasil, akan muncul jendela kecil Tkinter.

Jika Tkinter belum tersedia, jalankan kembali installer Python, pilih **Modify**, kemudian pastikan komponen Tcl/Tk sudah dipilih.

#### B. Linux (Ubuntu/Debian)

Pada beberapa distribusi Linux, Tkinter perlu diinstal secara terpisah.

Buka terminal dan jalankan:

```bash
sudo apt update
```

Kemudian instal Tkinter:

```bash
sudo apt install python3-tk
```

Setelah instalasi selesai, periksa dengan perintah:

```bash
python3 -m tkinter
```

Jika muncul jendela Tkinter, berarti instalasi berhasil.

#### C. Fedora Linux

Buka terminal dan jalankan:

```bash
sudo dnf install python3-tkinter
```

Kemudian periksa instalasi:

```bash
python3 -m tkinter
```

#### D. macOS

Pada macOS, Tkinter umumnya tersedia melalui instalasi Python resmi dari python.org.

Langkah-langkah:

1. Download Python dari https://www.python.org/downloads/macos/
2. Instal Python.
3. Buka Terminal.
4. Jalankan perintah:

```bash
python3 -m tkinter
```

Jika muncul jendela Tkinter, berarti library sudah tersedia.

Jika tidak tersedia, gunakan instalasi Python resmi yang menyertakan dukungan Tcl/Tk.

### 5. Menjalankan Aplikasi

Setelah Python dan Tkinter tersedia, buka terminal pada folder aplikasi.

Jalankan perintah berikut:

```bash
python main.py
```

Pada Linux atau macOS, gunakan:

```bash
python3 main.py
```

Jika berhasil, jendela **Manajemen Inventaris Sekolah** akan terbuka.

### 6. Struktur Folder

Pastikan seluruh file aplikasi berada dalam satu folder:

```text
Manajemen-Inventaris/
│
├── main.py
├── inventaris.py
└── inventaris.json
```

Keterangan:

- `main.py` : File utama untuk menjalankan aplikasi dan menampilkan GUI.
- `inventaris.py` : Mengelola data barang, stok, dan proses penyimpanan.
- `inventaris.json` : Menyimpan data inventaris dalam format JSON.

### 7. Troubleshooting

Jika aplikasi mengalami kendala, berikut beberapa solusi yang dapat dicoba:

| Kendala | Solusi |
|---|---|
| Python tidak dikenali | Instal Python dan aktifkan PATH |
| No module named tkinter | Instal Tkinter sesuai sistem operasi |
| File inventaris.json tidak ditemukan | Pastikan file berada dalam folder aplikasi |
| File inventaris.py tidak ditemukan | Pastikan semua file sudah diekstrak |
| Aplikasi tidak terbuka | Periksa pesan error pada terminal |

### 8. Persyaratan Sistem

- Sistem operasi Windows, Linux, atau macOS.
- Python 3.
- Library Tkinter.
- File aplikasi lengkap (`main.py`, `inventaris.py`, dan `inventaris.json`).

---

**Catatan:** Aplikasi ini tidak memerlukan instalasi database tambahan karena penyimpanan data menggunakan file JSON.
