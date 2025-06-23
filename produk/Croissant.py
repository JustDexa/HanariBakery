from produk.Produk import Produk
from interface.Pengembang import Pengembang

class Croissant(Produk, Pengembang):
    def pengembangan(self):
        print("Croissant mengalami proses pengembangan.")
