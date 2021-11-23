def sortStringByChar(x):
    x.sort(reverse=True)
    return print('Hasil:',x)

myData = ['apel','rambutan','jeruk']
print('Data yang ingin diurutkan (descending):',myData)
sortStringByChar(myData)
