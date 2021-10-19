#Game menebak angka
from random import randint
angkapc=randint(1,100)

print("“Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!”")
while True:
    tebak=int(input("Tebakan Anda:"))
    if (tebak < angkapc):
        print("Hehehe... Bilangan anda terlalu kecil")
    elif (tebak > angkapc):
        print("Hehehe... Bilangan anda terlalu besar")
    else:
        print("Yeeee... Bilangan tebakan anda BENAR :-)")
        break
