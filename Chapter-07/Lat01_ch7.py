namafile = str(input("Masukkan nama file: "))
print('Isi file',namafile,'adalah:')
try:
    file = open(namafile, "r")
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
