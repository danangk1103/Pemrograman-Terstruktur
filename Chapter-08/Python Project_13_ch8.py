nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def nilaitertinggi(x):
    nilaiakhir=[]
    for i in x:
        nilaiakhir.append((i['mid']+2*i['uas'])/3)
    for i in x:
        if (max(nilaiakhir)==(i['mid']+2*i['uas'])/3):
                print('NIM :',i['nim'],',nama :',i['nama'])
                break

print('Data mahasiswa dengan nilai akhir tertinggi:')
nilaitertinggi(nilaiMhs)
    
