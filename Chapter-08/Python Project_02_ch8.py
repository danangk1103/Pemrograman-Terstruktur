def dataStat(x):

    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    data = []
    data.append(a)
    data.append(b)
    data.append(c)
    
    return print(data)

y = [5,67,10,24,7]
dataStat(y)
