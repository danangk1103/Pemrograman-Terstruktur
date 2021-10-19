#Menghitung gaji pokok dan gaji bersih karyawan
kode=str(input("Masukkan kode karyawan              :"))
nama=str(input("Masukkan nama karyawan              :"))
gol=str(input("Masukkan golongan                   :"))
status=int(input("Masukkan status (1: menikah, 2: blm):"))
if(status==1):
    jumlahanak=int(input("Masukkan jumlah anak                :"))
print("")
print("========================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("----------------------------------------")
print("Nama karyawan          :"+nama+"(kode:"+kode+")")
print("Golongan               :"+gol)
if(status==1):
    print("Status menikah         :menikah")
    print("Jumlah anak            :"+str(jumlahanak))
elif(status==2):
    print("Status menikah         :belum menikah")
    print("Jumlah anak            :"+str(0))
print("----------------------------------------")
if(gol=='A'):
    gajipokok=10000000
elif(gol=='B'):
    gajipokok=8500000
elif(gol=='C'):
    gajipokok=7000000
elif(gol=='D'):
    gajipokok=5500000
print("Gaji pokok             :Rp",gajipokok)
if(status==1):
    tunjanganpasutri=round(gajipokok*(10/100))
    tunjangananak=round(jumlahanak*(5/100)*gajipokok)
elif(status==2):
    tunjanganpasutri=gajipokok*0
    tunjangananak=gajipokok*0
print("Tunjangan suami/istri  :Rp",tunjanganpasutri)
print("Tunjangan anak         :Rp",tunjangananak)
print("---------------------------------------+")
gajikotor=gajipokok+tunjanganpasutri+tunjangananak
print("Gaji kotor:Rp",gajikotor)
if(gol=='A'):
    potongan=round(gajikotor*(2.5/100))
    persenpotongan=2.5
elif(gol=='B'):
    potongan=round(gajikotor*(2.0/100))
    persenpotongan=2.0
elif(gol=='C'):
    potongan=round(gajikotor*(1.5/100))
    persenpotongan=1.5
elif(gol=='D'):
    potongan=round(gajikotor*(1.0/100))
    persenpotongan=1.0
print("Potongan ("+str(persenpotongan)+"%)"+"        :Rp",potongan)
print("----------------------------------------")
print("Gaji bersih            :Rp",round(gajikotor-potongan))
