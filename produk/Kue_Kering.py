from produk.Produk import Produk
from interface.Topping import Topping

class Kue_Kering(Produk, Topping):
    def tambah_topping(self):
        print("Topping ditambahkan ke Kue Kering.")
