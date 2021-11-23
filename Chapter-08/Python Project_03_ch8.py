n = int(input('Masukkan jumlah nama yang akan diinput: '))

dataNama = []
i=1
while True:
    print('Masukkan data ke-'+str(i)+' : ',end='')
    x=str(input())
    if (i==n):
        dataNama = dataNama+[x]
        break
    else:
        dataNama = dataNama+[x]
    i+=1
print('---------------------------------------')
for i in range(len(dataNama)):
    print(dataNama[i]+' ('+str(len(dataNama[i][0:]))+' karakter)')
