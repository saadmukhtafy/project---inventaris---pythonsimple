# mengatur Class, Object, dan pengelolaan barang.

import json

class Inventaris:

    def __init__(self):
        self.data = []
        self.baca_data()

    # Membaca data JSON
    def baca_data(self):
        with open("inventaris.json", "r") as file:
            self.data = json.load(file)

    # Menyimpan data JSON
    def simpan_data(self):
        with open("inventaris.json", "w") as file:
            json.dump(self.data, file, indent=4)

    # Menambah barang
    def tambah_barang(self, nama, stok):
        barang = {
            "nama": nama,
            "stok": stok
        }

        self.data.append(barang)
        self.simpan_data()

    # Mengubah stok
    def ubah_stok(self, nomor, stok):
        self.data[nomor]["stok"] = stok
        self.simpan_data()

    # Menghapus barang
    def hapus_barang(self, nomor):
        del self.data[nomor]
        self.simpan_data()
