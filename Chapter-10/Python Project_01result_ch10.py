myFile = open('D:\pp01.txt','r')
myList=myFile.readlines()

myList2=[]
for i in range(len(myList)):
    fix=myList[i].replace('\n','')
    myList2+=[fix]

ganjil=[]
genap=[]
for i in range(len(myList2)):
    angka=int(myList2[i])
    if (angka%2!=0):
        ganjil+=[angka]
    if (angka%2==0):
        genap+=[angka]

print('Banyaknya bilangan genap :'+str(len(genap)))
print('Banyaknya bilangan ganjil:'+str(len(ganjil)))
myFile.close()
