material = open('D:\pp06.txt', 'r')
result = open('D:\hasilpp06.txt', 'a')

myFile = material.read()

mySet = set(myFile)

mySet.remove(' ')

myList = list(mySet)

myList.sort(reverse=True)

n=2

file=myFile.replace(myList[0], chr(ord(myList[0])+n))
i = 1
while True:
    file = file.replace(myList[i], chr(ord(myList[i])+n))
    i += 1
    if (i==10):
        break

file = file.replace(chr(91), chr(65))
file = file.replace(chr(92), chr(66))

result.write(file)
material.close()
result.close()
