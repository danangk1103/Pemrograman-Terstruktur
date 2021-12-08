from datetime import *
create = open('D:\hasilpp02_ch11.txt', 'a')

while True:
    kode = input('Masukkan kode member  :')
    nama = input('Masukkan nama member  :')
    buku = input('Masukkan judul buku   :')
    x = datetime.date(datetime.now())
    y = x + timedelta(days=7)
    hasil = str(kode)+'|'+str(nama)+'|'+str(buku)+'|'+str(x)+'|'+str(y)+'\n'
    create.write(hasil)

    print()
    ulang = input('Ulangi lagi (y/n)    :')
    print()
    if ulang in ('N','n'):
        break

create.close()
