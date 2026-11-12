
import tkinter as tk

# Membuat jendela
root = tk.Tk()
root.title("Input Nama")
root.geometry("400x250")

# Label
label = tk.Label(root, text="Masukkan Nama:")
label.pack(pady=10)

# Kolom input nama
input_nama = tk.Entry(root, width=30)
input_nama.pack(pady=10)

# Fungsi tombol
def tampilkan():
    nama = input_nama.get()
    hasil.config(text="Halo, " + nama)

# Tombol
tombol = tk.Button(
    root,
    text="Kirim",
    command=tampilkan
)
tombol.pack(pady=10)

# Hasil
hasil = tk.Label(root, text="")
hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
