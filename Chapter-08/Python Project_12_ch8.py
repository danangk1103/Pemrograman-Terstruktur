print('Menu:')
print('A. Tambah data buah')
print('B. Beli buah')
print('C. Hapus data buah')
print()
pilih=str(input('Pilihan menu: '))
print()

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
if (pilih=='A'):
    namabuah2=str(input('Masukkan nama buah       : '))
    hargakg=int(input('Masukkan harga satuan    : '))
    if namabuah2 in buah:
        print('nama buah sudah ada di dalam dictionary')
        print('')
        print('Data buah:')
        print('')

        for x in buah.keys():
            print('-    '+x+' (Harga Rp '+str(buah[x])+')')

    else:
        buah[namabuah2] = hargakg
        print('')
        print('Data buah:')
        print('')
   
        for x in buah.keys():
            print('-    '+x+' (Harga Rp '+str(buah[x])+')')
    
if (pilih=='B'):
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

if (pilih=='C'):
    namabuah2=str(input('Masukkan nama buah       : '))
    if namabuah2 not in buah:
        print('nama buah sudah ada di dalam dictionary')
        print('')
        print('Data buah:')
        print('')

        for x in buah.keys():
            print('-    '+x+' (Harga Rp '+str(buah[x])+')')

    else:
        del buah[namabuah2]
        print('')
        print('Data buah:')
        print('')
   
        for x in buah.keys():
            print('-    '+x+' (Harga Rp '+str(buah[x])+')')
