class Produk:
    def __init__(self, nama_product, kode_product, bahan_baku, biaya_produksi, harga_jual):
        self.nama_product = nama_product
        self.kode_product = kode_product
        self.bahan_baku = bahan_baku
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual

    def tampilkan_data(self):
        print(f"Nama: {self.nama_product}, Kode: {self.kode_product}, Harga Jual: {self.harga_jual}")
        print("Bahan Baku = ")
        for bahan, jumlah in self.bahan_baku.items():
            print(f" - {bahan}:{jumlah}")

    def kalkulasi_biaya_produksi(self):
        return sum(self.biaya_produksi)

    def kalkulasi_harga_jual(self):
        return self.kalkulasi_biaya_produksi() * 1.5

    def pengadonan(self):
        print("Proses pengadonan dimulai...")

    def pemanggangan(self):
        print("Proses pemanggangan dimulai...")
