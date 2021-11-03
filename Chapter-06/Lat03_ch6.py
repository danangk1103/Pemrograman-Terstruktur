def faktorial(n):
    if (n==1)or(n==-1):
        hasil = n
    elif (n==0):
        hasil = "1"
    elif (n<0):
        n = n * -1
        o = n
        while True:
            n = n - 1
            o *= n
            if (n==1):
                hasil = o*-1
                break
    else:
        o = n
        while True:
            n = n - 1
            o *= n
            if (n==1):
                hasil = o
                break
    return hasil

print('Rumus permutasi:')
print('P(n,r) = n!/(n-r)!')
print('Rumus kombinasi:')
print('P(n,r) = n!/r!(n-r)!')
print('=========================')
print('Contoh soal:')
print('a. C(5,3)  = 5!/(5-3)! =',round(faktorial(5)/(faktorial(3)*faktorial(5-3))))
print('b. P(10,7) = 10!/7!(10-7)! =',round(faktorial(10)/faktorial(7)))
