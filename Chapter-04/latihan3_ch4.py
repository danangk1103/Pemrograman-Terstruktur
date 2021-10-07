#Menghitung jumlah liter bensin untuk menempuh jarak
print('Menghitung banyak liter bensin yang diperlukan:')
print('_______________________________________________')
Jarak=float(input('Jarak (km):'))
liter=float(input('Jarak yang dapat ditempuh per liter:'))
print('Jumlah liter bensin yang diperlukan:',Jarak/liter,'liter')
print('-----------------------------------------------')

#Menghitung berapa kali isi bensin hingga penuh
print('Menghitung banyak isi bensin sampai full:')
print('_______________________________________________')
dayatampung=float(input('Daya tampung mobil (liter):'))
print('Banyak isi bensin sampai full:',round((Jarak/liter)//dayatampung),'kali')
print('Banyak isi bensin total (tidak harus full):',round((Jarak/liter)//dayatampung+1),'kali')
