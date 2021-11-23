buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('Data buah dan harga:',buah)
print('')

hargatotal=[]
while True:
    namabuah=str(input('Nama buah yang dibeli   : '))
    jumlahkg=int(input('Berapa Kg               : '))

    if namabuah in buah:
        hargatotal.append(buah[namabuah]*jumlahkg)

    if namabuah not in buah:
        print('-------------------------------------------')
        print('Nama buah tidak ada di data')

    print('')
    ulang=str(input('Lagi (y/n)?             : '))
    print('')
    if (ulang == 'n'):
        print('-------------------------------------------')
        print('Total harga             :',sum(hargatotal))
        print('Terimakasih telah mencoba!!!^^')
        break
