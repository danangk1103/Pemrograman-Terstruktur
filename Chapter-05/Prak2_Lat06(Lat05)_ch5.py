#Game menebak angka
from random import randint
angkapc=randint(1,100)

score=100
print("“Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!”")
while True:
    tebak=int(input("Tebakan Anda:"))
    if (tebak < angkapc):
        print("Hehehe... Bilangan anda terlalu kecil")
        score-=2
    elif (tebak > angkapc):
        print("Hehehe... Bilangan anda terlalu besar")
        score-=2        
    else:
        print("Yeeee... Bilangan tebakan anda BENAR :-)")
        break
if (score>=0)and(score<=100):
    print("Score Anda:"+str(score))
elif (score<0):
    print("Score Anda:0")
