dataFile = open('D:\datamahasiswa.txt','r')

data = dataFile.readlines()

dataMhs=[]
for i in range(len(data)):
    datafinal={}
    fix=data[i].split('|')
    fix[2]=fix[2].replace('\n','')
    datafinal['nim']=fix[0]
    datafinal['nama']=fix[1]
    datafinal['alamat']=fix[2]
    dataMhs.append(datafinal)

while True:
    katakunci=input('Masukkan NIM yang mau dicari: ')

    for i in range(len(dataMhs)):              
        if katakunci in dataMhs[i]['nim']:
            print()
            print('Data Mahasiswa')
            print('NIM   :'+str(dataMhs[i]['nim']))
            print('Nama  :'+str(dataMhs[i]['nama']))
            print('Alamat:'+str(dataMhs[i]['alamat']))

    if katakunci not in dataMhs[0]['nim']:
        if katakunci not in dataMhs[1]['nim']:
            if katakunci not in dataMhs[2]['nim']:
                print('\"Data mahasiswa tidak ditemukan\"')
            
    print()
    repeat=input('Ingin mencari lagi? (y/n): ')
    print()
    if repeat in ('N','n'):
        print('Terimakasih telah mencoba!!!^^')
        break
    
dataFile.close()
