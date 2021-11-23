n = int(input('Masukkan jumlah bilangan bulat yang diperlukan: '))

dataNilai = []
i=1
while True:
    print('Masukkan data ke-'+str(i)+' : ',end='')
    x=int(input())
    if (i==n):
        dataNilai = dataNilai+[x]
        break
    else:
        dataNilai = dataNilai+[x]
    i+=1

dataNilai.sort(reverse=True)
print('Bilangan diurutkan dari yang terbesar =',dataNilai)
