mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*62)
print('NIM        NAMA MAHASISWA        TGL LAHIR        TEMPAT LAHIR')
print('-'*62)

for i in range(len(mhs)):
    print((mhs[i].split(":")[0]).ljust(11), end='')
    print((mhs[i].split(":")[1]).ljust(22), end='')
    tgl=(mhs[i].split(":")[2]).split('-')
    print((str(tgl[-1]+'/'+tgl[-2]+'/'+tgl[-3])).ljust(17), end='')
    print((mhs[i].split(":")[3]).ljust(20))

print('-'*62)


