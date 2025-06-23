from produk.Croissant import Croissant
from produk.Roti_Manis import Roti_Manis
from produk.Kue_Kering import Kue_Kering
from produk.Muffin import Muffin
from produk.Butter_Cookies import Butter_Cookies

produk_list = []

def tambah_produk():
    print("\n=== Tambah Produk Baru ===")
    print("1. Croissant")
    print("2. Roti Manis")
    print("3. Kue Kering - Muffin")
    print("4. Kue Kering - Butter Cookies")
    pilihan = input("Pilih jenis produk (1-4): ")

    nama = input("Nama Produk: ")
    kode = input("Kode Produk: ")
    while True:
        bahan_input = input("Daftar bahan baku dan jumlah (format: Nama=Jumlah, pisahkan dengan koma): ")
        try:
            bahan = dict(item.strip().split("=") for item in bahan_input.split(","))
            if not all(bahan.values()):
                raise ValueError
            break
        except ValueError:
         print("⚠ Format salah! Gunakan format seperti: Tepung=250g, Gula=100g")
    biaya = list(map(int, input("Biaya produksi per bahan (pisahkan dengan koma): ").split(",")))
    harga = int(input("Harga jual per-n pcs: "))

    if pilihan == "1":
        produk = Croissant(nama, kode, bahan, biaya, harga)
    elif pilihan == "2":
        produk = Roti_Manis(nama, kode, bahan, biaya, harga)
    elif pilihan == "3":
        produk = Muffin(nama, kode, bahan, biaya, harga)
    elif pilihan == "4":
        produk = Butter_Cookies(nama, kode, bahan, biaya, harga)
    else:
        print("Pilihan tidak valid.")
        return

    produk_list.append(produk)
    print("Produk berhasil ditambahkan!\n")

def tampilkan_produk():
    print("\n=== Daftar Produk ===")
    if not produk_list:
        print("Belum ada produk.")
    for p in produk_list:
        p.tampilkan_data()

def estimasi_profit():
    print("\n=== Estimasi Profit ===")
    if not produk_list:
        print("Belum ada produk.")
        return
    for idx, p in enumerate(produk_list):
        print(f"{idx+1}. {p.nama_product}")
    idx = int(input("Pilih produk: ")) - 1
    jumlah = int(input("Jumlah pcs yang akan diproduksi: "))
    produk = produk_list[idx]
    total_biaya = produk.kalkulasi_biaya_produksi() * jumlah
    total_jual = produk.harga_jual * jumlah
    profit = total_jual - total_biaya
    print(f"Estimasi Profit: Rp{profit}")

def simulasi_produksi():
    print("\n=== Simulasi Produksi ===")
    if not produk_list:
        print("Belum ada produk.")
        return
    for idx, p in enumerate(produk_list):
        print(f"{idx+1}. {p.nama_product}")
    idx = int(input("Pilih produk: ")) - 1
    produk = produk_list[idx]
    produk.pengadonan()
    if hasattr(produk, 'pengembangan'):
        produk.pengembangan()
    produk.pemanggangan()
    if hasattr(produk, 'tambah_topping'):
        produk.tambah_topping()

def main():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah Produk")
        print("2. Tampilkan Produk")
        print("3. Estimasi Profit")
        print("4. Simulasi Produksi")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            tampilkan_produk()
        elif pilihan == "3":
            estimasi_profit()
        elif pilihan == "4":
            simulasi_produksi()
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
main()
