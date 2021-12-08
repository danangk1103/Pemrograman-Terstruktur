from PythonProject_01_ch11 import diffDate
from datetime import *
dataFile = open('D:\hasilpp02_ch11.txt', 'r')
data = dataFile.readlines()

dataMhs=[]
for i in range(len(data)):
    datafinal={}
    fix=data[i].split('|')
    fix[4]=fix[4].replace('\n','')
    datafinal['kode']=fix[0]
    datafinal['nama']=fix[1]
    datafinal['judul buku']=fix[2]
    datafinal['tglmulai'] = fix[3]
    datafinal['tglakhir'] = fix[4]

    dataMhs.append(datafinal)

while True:
    katakunci = input('Masukkan kode member: ')

    for i in range(len(dataMhs)):
        if katakunci in dataMhs[i]['kode']:
            print()
            print('Data Mahasiswa')
            print('kode                     :' + str(dataMhs[i]['kode']))
            print('Nama                     :' + str(dataMhs[i]['nama']))
            print('Judul buku               :' + str(dataMhs[i]['judul buku']))
            print('Tanggal mulai peminjaman :' + str(dataMhs[i]['tglmulai']))
            print('Tanggal maks pengembalian:' + str(dataMhs[i]['tglakhir']))
            x = diffDate(str(dataMhs[i]['tglakhir']))
            if (x<0):
                print('Tanggal pengembalian     :'+str(datetime.date(datetime.now())))
                print('Terlambat                :'+str((x)*-1)+' hari')
                print('Denda                    :'+str((x)*-1*2000))
            if (x>=0):
                print('Tanggal pengembalian     :'+str(datetime.date(datetime.now())))
                print('Terlambat                :'+'-')
                print('Denda                    :'+'-')

    if katakunci not in dataMhs[0]['kode']:
        if katakunci not in dataMhs[1]['kode']:
            print('\"Data mahasiswa tidak ditemukan\"')

    print()
    repeat = input('Ingin mencari lagi? (y/n): ')
    print()
    if repeat in ('N', 'n'):
        print('Terimakasih telah mencoba!!!^^')
        break

dataFile.close()
