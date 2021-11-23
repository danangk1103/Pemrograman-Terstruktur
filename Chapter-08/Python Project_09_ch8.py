buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('Data buah dan harga:',buah)
print('')

while True:
    namabuah=str(input('Nama buah yang dibeli   : '))
    jumlahkg=int(input('Berapa Kg               : '))

    if namabuah in buah:
        print('-------------------------------------------')
        print('Total harga             :',(buah[namabuah]*jumlahkg))

    if namabuah not in buah:
        print('-------------------------------------------')
        print('Nama buah tidak ada di data')

    print('===============================================')
    ulang=str(input('Lagi (y/n)?             : '))
    print('===============================================')
    if (ulang == 'n'):
        print('Terimakasih telah mencoba!!!^^')
        break
