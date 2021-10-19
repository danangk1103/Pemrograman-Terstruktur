from random import randint
hitung=0
while True:
    bil = randint(0, 10)
    print(bil)
    hitung+=1
    if bil == 5:
        break
print('Jumlah perulangan : ',hitung)
