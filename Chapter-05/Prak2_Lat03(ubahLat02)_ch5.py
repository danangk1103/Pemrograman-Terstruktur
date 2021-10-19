#Menampilkan bilangan bulat ganjil dari 0 sampai 100
hitung=0
sum=0
for i in range(1,100,2):
    print(i)
    hitung+=1
    sum+=i
print("Banyaknya bilangan ganjil:"+str(hitung))
print("Jumlah seluruh bilangan:"+str(sum))
