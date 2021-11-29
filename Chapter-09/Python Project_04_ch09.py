def shuffleString(x, n):
    import random

    hasil=[]
    while True:
        masuk=''.join(random.sample(x,len(x)))
        if masuk not in hasil:
            hasil+=[(str(masuk))]

        if (len(hasil)==n):
            break

        
    print(hasil)

shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)

