#NIM MAHASISWA 2009106047 

nominal_angka = int(input("Masukan NIM Mahasiswa anda : "))
a = 1
o = 1
while a <= nominal_angka:
    print (o)
    o += 1
    if o == 10:
        o -= 9
    a += 1
