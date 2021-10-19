# kotak bintang ajaib
kolom = 1
baris = 1

i = 0
while (i < baris):
    j = 0
    while (j < kolom):
        print('* ', end='')
        j += 1
    print('')
    i += 1
    kolom += 1
    baris += 1
    if (kolom == 6) and (baris == 6):
        break
