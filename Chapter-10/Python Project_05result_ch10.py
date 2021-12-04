createfile = open('D:\dataangka.txt', 'r')
fileresult = open('D:\hasilangka.txt', 'a')

file=createfile.readlines()
data=[]
for i in range(len(file)):
    fix=file[i].split('|')
    fix2=fix[1].replace('\n', '')
    fix3=int(fix[0])+int(fix2)
    data+=[fix3]
    
for i in range(len(data)):
    fileresult.write(str(data[i])+'\n')

createfile.close()
fileresult.close()
