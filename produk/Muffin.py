from produk.Kue_Kering import Kue_Kering
from interface.Pengembang import Pengembang
from interface.Topping import Topping

class Muffin(Kue_Kering, Pengembang, Topping):
    def pengembangan(self):
        print("Muffin mengalami proses pengembangan.")

    def tambah_topping(self):
        print("Topping ditambahkan ke Muffin.")
