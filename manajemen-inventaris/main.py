# # menjalankan apk tinker pada python

import tkinter as tk
from tkinter import messagebox
from inventaris import Inventaris

# # Membuat objek
# app = Inventaris()

# # Membuat jendela
# window = tk.Tk()
# window.title("Manajemen Inventaris Sekolah")
# window.geometry("600x500")
# window.configure(bg="white")

# # Judul
# judul = tk.Label(
#     window,
#     text="MANAJEMEN INVENTARIS SEKOLAH",
#     font=("Arial", 16, "bold"),
#     bg="white"
# )
# judul.pack(pady=20)

# # Input nama barang
# tk.Label(window, text="Nama Barang", bg="white").pack()

# nama = tk.Entry(window, width=35)
# nama.pack(pady=5)

# # Input stok
# tk.Label(window, text="Jumlah Stok", bg="white").pack()

# stok = tk.Entry(window, width=35)
# stok.pack(pady=5)

# # Daftar barang
# daftar = tk.Listbox(window, width=65, height=12)
# daftar.pack(pady=15)

# # Menampilkan barang
# def tampilkan():
#     daftar.delete(0, tk.END)

#     for barang in app.data:
#         daftar.insert(
#             tk.END,
#             barang["nama"] + " - Stok: " + str(barang["stok"])
#         )

# # Menambah barang
# def tambah():
#     nama_barang = nama.get()
#     jumlah = stok.get()

#     if nama_barang == "" or jumlah == "":
#         messagebox.showwarning("Peringatan", "Data harus diisi!")
#     elif not jumlah.isdigit():
#         messagebox.showwarning("Peringatan", "Stok harus angka!")
#     else:
#         app.tambah_barang(nama_barang, int(jumlah))

#         tampilkan()

#         nama.delete(0, tk.END)
#         stok.delete(0, tk.END)

#         messagebox.showinfo("Berhasil", "Barang berhasil ditambahkan!")

# # Mengubah stok
# def ubah():
#     pilihan = daftar.curselection()

#     if pilihan:
#         jumlah = stok.get()

#         if jumlah.isdigit():
#             nomor = pilihan[0]
#             app.ubah_stok(nomor, int(jumlah))
#             tampilkan()
#             messagebox.showinfo("Berhasil", "Stok berhasil diubah!")
#         else:
#             messagebox.showwarning("Peringatan", "Masukkan stok berupa angka!")
#     else:
#         messagebox.showwarning("Peringatan", "Pilih barang terlebih dahulu!")

# # Menghapus barang
# def hapus():
#     pilihan = daftar.curselection()

#     if pilihan:
#         nomor = pilihan[0]

#         app.hapus_barang(nomor)
#         tampilkan()

#         messagebox.showinfo("Berhasil", "Barang berhasil dihapus!")
#     else:
#         messagebox.showwarning("Peringatan", "Pilih barang terlebih dahulu!")

# # Tombol aplikasi
# tk.Button(
#     window,
#     text="Tambah Barang",
#     bg="green",
#     fg="white",
#     command=tambah
# ).pack(pady=3)

# tk.Button(
#     window,
#     text="Ubah Stok",
#     bg="blue",
#     fg="white",
#     command=ubah
# ).pack(pady=3)

# tk.Button(
#     window,
#     text="Hapus Barang",
#     bg="red",
#     fg="white",
#     command=hapus
# ).pack(pady=3)

# # Menampilkan data awal
# tampilkan()

# # Menjalankan aplikasi
# window.mainloop()
