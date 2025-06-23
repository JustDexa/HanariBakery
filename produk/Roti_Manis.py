from produk.Produk import Produk
from interface.Pengembang import Pengembang

class Roti_Manis(Produk, Pengembang):
    def pengembangan(self):
        print("Roti Manis mengalami proses pengembangan.")
