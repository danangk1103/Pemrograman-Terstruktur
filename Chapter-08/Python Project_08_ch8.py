buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('Data buah dan harga:',buah)
buah2 = []
for x in buah.values():
    buah2 = buah2 + [x]

print('Rata-rata harga dari seluruh data:',(sum(buah2)/len(buah2)))
