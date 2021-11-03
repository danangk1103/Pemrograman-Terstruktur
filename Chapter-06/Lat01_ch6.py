# menentukan ketiga sisi segitiga merupakan triple phytagoras atau bukan
while True:
    print('Masukkan nilai pada keterangan di bawah ini:')
    a=int(input('sisi a (alas)   = '))
    b=int(input('sisi b (tinggi) = '))
    c=int(input('sisi c (miring) = '))

    def isPythagoras(a, b, c):
        kuadratsisic = (a**2)+(b**2)
        kuadratsisia = (c**2)-(b**2)
        kuadratsisib = (c**2)-(a**2)
        if (a==kuadratsisia/a):
            if(b==kuadratsisib/b):
                if(c==kuadratsisic/c):
                    print('a =', a,'b =',b,'c =',c,'->',bool(bool(a==kuadratsisia/a)and(b==kuadratsisib/b))and(c==kuadratsisic/c))
        else:
             print('a =', a,'b =',b,'c =',c,'->',bool(bool(a==kuadratsisia/a)and(b==kuadratsisib/b))and(c==kuadratsisic/c))
    
    isPythagoras(a, b, c)
    print("----------------------------------------")
    ulang=str(input("Ingin mengulang?(y/n) : "))
    print("----------------------------------------")
    if(ulang=='n'):
        print("Terima kasih sudah mencoba!^^")
        break
