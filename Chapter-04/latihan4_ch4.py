#Menghitung jumlah waktu perjalanan
print('__________Menghitung lama waktu perjalanan__________')
jarakAB=float(input('Jarak kota A ke B (km):'))
kecepatanAB=float(input('Kecepatan rata-rata dari kota A ke B (km/jam):'))
print('Total waktu perjalanan kota A ke B:',round(jarakAB//kecepatanAB),'Jam',round((jarakAB/kecepatanAB-jarakAB//kecepatanAB)*60),'menit')
jarakBC=float(input('Jarak kota B ke C (km):'))
kecepatanBC=float(input('Kecepatan rata-rata dari kota B ke C (km/jam):'))
print('Total waktu perjalanan kota B ke C:',round(jarakBC//kecepatanBC),'Jam',round((jarakBC/kecepatanBC-jarakBC//kecepatanBC)*60),'menit')
print('-----------------------------------------------')

#Menghitung waktu tiba pukul berapa?
print('__________Menghitung waktu tiba__________')
print('Waktu berangkat dari kota A:')
jam1=int(input('Jam:'))
menit1=int(input('Menit:'))
print('Waktu tiba di kota B:')
print('Jam:',jam1+round(jarakAB//kecepatanAB))
print('menit:',menit1+round((jarakAB/kecepatanAB-jarakAB//kecepatanAB)*60))
rest1=int(input('Istirahat di kota B (jam):'))
rest2=float(input('Istirahat di kota B (menit):'))
print('Waktu tiba di kota C:',)
waktujamtotalC=jam1+round(jarakAB//kecepatanAB)+round(jarakBC//kecepatanBC)+rest1
waktumenittotalC=menit1+round((jarakAB/kecepatanAB-jarakAB//kecepatanAB)*60)+round(((jarakBC/kecepatanBC-jarakBC//kecepatanBC)*60)+rest2)
if(waktujamtotalC > 24):
    print('Jam:',waktujamtotalC-24)
elif(waktumenittotalC > 59):
    print('Jam:',waktujamtotalC+1)
    print('menit:',waktumenittotalC-60)
else:
    print('Jam:',waktujamtotalC)
    print('menit:',waktumenittotalC)
