# membuka dan mau membaca file d:/data.txt
try:
    file = open("c:/data.txt", "r")
except FileNotFoundError:
    print('\'File tidak ditemukan\'')
# baca baris pertama dari file
# simpan ke dalam variabel bil1 sbg integer
try:
    bil1 = int(file.readline())
except NameError:
    print('\'File tidak ditemukan\'')

# baca baris pertama dari file
# simpan ke dalam variabel bil2 sbg integer
try:
    bil2 = int(file.readline())
except NameError:
    print('\'File tidak ditemukan\'')

# hitung dan tampilan hasil bagi
try:
    hasil = bil1/bil2
    print(bil1, ' dibagi ', bil2, ' sama dengan ', hasil)
except NameError:
    print('\'File tidak ditemukan\'')
except ZeroDivisionError:
    print('\'Tidak boleh pembagian dengan nol\'')
