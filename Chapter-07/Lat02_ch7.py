namafile = str(input("Masukkan nama file: "))
while True:
    file = open(namafile, "a")
    file.write(input('Data yang mau ditambahkan: '))
    file.close()
    ulang = str(input('Mau lagi(y/n): '))
    if (ulang=='n'):
        break
