# kotak bintang ajaib
kolom = 5
baris = 9

i = 0
while (i < baris):
    j = 0
    while (j < kolom):
        print('* ', end='')
        j += 1
    print('')
    i += 1
    kolom -= 1
    baris -= 1
    if (kolom == 0) and (baris == 0):
        break
