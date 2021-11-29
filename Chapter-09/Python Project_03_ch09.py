def bintang(n):
    if (n%2!=0):
        space = 2*n-1
        if (n==1):
            print('*'.center(space))
        for i in range(round(n/2)):
            print(('*'*(2*i+1)).center(space))
        for i in range(n-round(n/2)):
            print(('*'*(n-(i*2+2))).center(space))
          
bintang(7)

#Jika ingin memasukan bilangan yang genap,copas script di bawah ke dalam fungsi
#Kemudian setelah di copas jangan lupa hilangkan tanda '#'
#Lalu tab bagian bawah if supaya menjorok

#if(n%2==0):
    #space = 2*n-1
    #for i in range(round(n/2)):
        #print(('*'*(2*i+1)).center(space))
    #for i in range(n-round(n/2)):
        #print(('*'*(n-(i*2+3))).center(space))
