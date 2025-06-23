from produk.Kue_Kering import Kue_Kering
from interface.Topping import Topping

class Butter_Cookies(Kue_Kering, Topping):
    def tambah_topping(self):
        print("Topping ditambahkan ke Butter Cookies.")
