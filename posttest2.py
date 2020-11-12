def star(func):
    def inner(*args, **kwargs):
        print("=" * 20)
        func(*args, **kwargs)
        print("<>" * 10)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("-" * 30)
        func(*args, **kwargs)
        print("-" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hallo Kak")

print('{:^100}'.format('Selamat Datang di Kopi Chuseyo'))
print('{:^100}'.format('____________________________________'))

nama = input("Masukan nama pelanggan : ")
tanggal = input("Masukan Nomor Member : ")

print("         ~~~==== MENU ====~~~")
print("1. Iced Tea              @6000")
print("2. Caramel Machiato      @30000")
print("3. Green Tea Latte       @25000")
print("4. Milkshake chocolate   @15000")
print("5. Chocolate Hazelnut    @25000")
print("6. Chocolate Summer      @20000")
print("7. Kopi Unnie            @19000")
print("8. Kopi Oppa             @19000")
print("9. Caramel Latte         @25000")
print("10.Espresso              @10000")
print("         ~~~==== MENU ====~~~")

menu_pesanan = int(input("Masukan nomor pesanan  : "))

if menu_pesanan==1:
    harga = 6000
elif menu_pesanan==2:
    harga = 30000
elif menu_pesanan==3:
    harga = 25000
elif menu_pesanan==4:
    harga = 15000
elif menu_pesanan==5:
    harga = 25000
elif menu_pesanan==6:
    harga = 20000
elif menu_pesanan==7:
    harga = 19000
elif menu_pesanan==8:
    harga = 19000
elif menu_pesanan==9:
    harga = 25000
elif menu_pesanan==10:
    harga = 10000
else :    
    while True:
        print("=====Menu Tidak Tersedia,Silahkan Pilih Menu Lainnya!!=====")
        menu_pesanan = int(input("Masukan nomor pesanan  : "))
        if menu_pesanan== 1 or menu_pesanan== 2 or menu_pesanan== 3 or menu_pesanan== 4 or menu_pesanan== 5:
            if menu_pesanan==1:
                harga = 6000
            elif menu_pesanan==2:
                harga = 30000
            elif menu_pesanan==3:
                harga = 25000
            elif menu_pesanan==4:
                harga = 15000
            elif menu_pesanan==5:
                harga = 25000
            elif menu_pesanan==6:
                harga = 20000
            elif menu_pesanan==7:
                harga = 19000
            elif menu_pesanan==8:
                harga = 19000
            elif menu_pesanan==9:
                harga = 25000
            elif menu_pesanan==10:
                harga = 10000
        

jumlah_pembelian = int(input("Masukan Jumlah Pembelian : "))

bayar = jumlah_pembelian * harga

print("Anda Harus Membayar : Rp.{}".format(bayar))
