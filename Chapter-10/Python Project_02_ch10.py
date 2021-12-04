#Program input data mahasiswa

dataFile = open('D:\datamahasiswa.txt', 'a')

while True:
    nim = input('Masukkan NIM       :')
    nama = input('Masukkan Nama Mhs  :')
    alamat = input('Masukkan Alamat    :')

    myString = nim+'|'+nama+'|'+alamat+'\n'

    dataFile.write(myString)

    print()
    repeat = input('Ulangi input lagi (y/n):')
    print()
    if repeat in('N','n'):
        break

dataFile.close()
