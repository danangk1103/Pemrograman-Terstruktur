# membuat formasi bintang pertama
print('Formasi bintang pertama:')
def starFormation(n):
    kolom = n
    baris = n

    i = 3
    while (i < baris):
        j = 3
        while (j < kolom):
            print('* ', end=',')
            j += 1
        print('')
        i += 1
        kolom += 1
        baris += 1
        if (kolom == 8) and (baris == 8):
            break

starFormation(4)
print('')

# membuat formasi bintang kedua
print('Formasi bintang kedua:')
def starFormation2(n):
    kolom = n
    baris = n

    i = 3
    while (i < baris):
        j = 0
        while (j < kolom):
            print('* ', end='')
            j += 1
        print('')
        i += 1
        kolom -= 1
        baris += 1
        if (kolom == 0) and (baris == 8):
            break

starFormation2(4)
print('')

# membuat formasi bintang ketiga (gabungan)
print('Formasi bintang ketiga (gabungan):')
def starFormation3(n):
    kolom = n
    baris = n

    i = 6
    while (i < baris):
        j = 6
        while (j < kolom):
            print('* ', end='')
            j += 1
        print('')
        i += 1
        kolom += 1
        baris += 1
        if (kolom == 11) and (baris == 11):
            break
    kolom = n
    baris = n

    i = 6
    while (i < baris):
        j = 4
        while (j < kolom):
            print('* ', end='')
            j += 1
        print('')
        i += 1
        kolom -= 1
        baris += 1
        if (kolom == 3) and (baris == 11):
            break

starFormation3(7)
