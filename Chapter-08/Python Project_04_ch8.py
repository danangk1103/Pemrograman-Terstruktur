sayur = ['bayam','kangkung','wortel','selada']
print('Data sayur awal:',sayur)
print('')
print('Menu:')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')
print('')

while True:
    pilih=str(input('Pilihan Anda: '))
    if (pilih=='A'):
        tambah=str(input('Masukkan nama sayur yang ingin ditambahkan: '))
        sayur.append(tambah)
        print('--------------------------------------------')

    elif (pilih=='B'):
        hapus=str(input('Masukkan nama sayur yang ingin dihapus: '))
        sayur.remove(hapus)
        print('--------------------------------------------')

    elif (pilih=='C'):
        print('Data sayur saat ini:',sayur)
        print('--------------------------------------------')

    else:
        print('Pilihan Anda tidak ada di menu')
        
    ulang=str(input('Ingin mengulang (y/n)? : '))
    print('--------------------------------------------')
    if (ulang=='n'):
        print('Terima kasih sudah mencoba!!!^^')
        break

