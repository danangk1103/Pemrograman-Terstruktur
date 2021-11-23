def kuadrat(bil):
    hasil = []
    for i in range(len(bil)):
        hasil = hasil + [bil[i]**2]

    print('Hasil bilangan yang telah dikuadratkan:',hasil)

angka = [2,4,5,6]
print('Bilangan yang ingin dikuadratkan:',angka)
kuadrat(angka)        

