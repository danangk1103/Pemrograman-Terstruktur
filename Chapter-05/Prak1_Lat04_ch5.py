#Menghitung gaji pokok dan gaji bersih karyawan
kode=str(input("Masukkan kode karyawan  :"))
nama=str(input("Masukkan nama karyawan  :"))
gol=str(input("Masukkan golongan       :"))
print("")
print("===================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------")
print("Nama karyawan           :"+nama+"(kode:"+kode+")")
print("Golongan                :"+gol)
print("-----------------------------------")
if(gol=='A'):
    gajipokok=100000000
    potongan=round(gajipokok*(2.5/100))
    persenpotongan=2.5
elif(gol=='B'):
    gajipokok=8500000
    potongan=round(gajipokok*(2.0/100))
    persenpotongan=2.0
elif(gol=='C'):
    gajipokok=7000000
    potongan=round(gajipokok*(1.5/100))
    persenpotongan=1.5
elif(gol=='D'):
    gajipokok=5500000
    potongan=round(gajipokok*(1.0/100))
    persenpotongan=1.0
print("Gaji pokok              :Rp",gajipokok)
print("Potongan ("+str(persenpotongan)+"%)"+"         :Rp",potongan)
print("-----------------------------------")
print("Gaji bersih             :Rp",gajipokok-potongan)
