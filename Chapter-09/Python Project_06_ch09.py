nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("="*53)
print("NIM     NAMA MHS         MID   UAS   NA     STATUS")
print("-"*53)

na=[]
status=[]
for i in range(len(nilai)):
    hitung=round((nilai[i]['mid']+2*nilai[i]['uas'])/3)
    if (hitung >= 60):
        status += ['LULUS']
    if (hitung < 60):
        status += ['   TIDAK LULUS']
    na += [hitung]

for i in range(len(nilai)):
    nilai[i]['NA'] = na[i]
    nilai[i]['STATUS'] = status[i]

for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(8), end='')
    print(nilai[i]['nama'].ljust(14), end='')
    print(str(nilai[i]['mid']).rjust(6), end='')
    print(str(nilai[i]['uas']).rjust(6), end='')
    print(str(nilai[i]['NA']).rjust(5), end='')
    print(str(nilai[i]['STATUS']).rjust(10))

print("="*53)
