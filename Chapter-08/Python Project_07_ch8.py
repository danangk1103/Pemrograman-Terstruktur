buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('Data buah dan harga:',buah)

hargamax = max(buah.values())

for x in buah.keys():
    if (buah[x]==hargamax):
        print('Buah dengan harga tertinggi adalah',x)
        break
        
