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

print('dataMhs='+str(dataMhs))
dataFile.close()
