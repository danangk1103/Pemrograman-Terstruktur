def sum(*myData):

    # init values
    sum = 0
    i = 0

    # menjumlahkan semua data dalam myData
    for data in myData:
        sum += data
        i += 1

    # hitung jumlah
    jumlah = sum
    return jumlah
        


def average(*myData):

    # init values
    i = 0

    # menjumlahkan banyak data dalam myData
    for data in myData:
        i += 1

    # hitung rata-rata
    rata2 = sum(*myData)/i
    print('Rata-ratanya     :',rata2)

def maks(*myData):

    # menentukan nilai maksimum
    hasil = [*myData]
    print('Nilai maksimumnya:',max(hasil))

def min_(*myData):

    # menentukan nilai maksimum
    hasil = [*myData]
    print('Nilai minimumnya :',min(hasil))
        







    
    

    
