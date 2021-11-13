print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

jumlah = 0
i = 0
while True:
    try:
        data=int(input('Masukkan bilangan bulat: '))
        jumlah+=data
        i+=1
        ulang=str(input('Lagi (y/n)? : '))
        if (ulang=='n'):
            break
        if (data==str(data)):
            continue
        
    except ValueError:
        print('Bukan bilangan bulat')
        ulang=str(input('Lagi (y/n)? : '))
        if (ulang=='n'):
            break

print('')
print('Rata-ratanya adalah: ',jumlah/i)
           
