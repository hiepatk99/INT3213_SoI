def EratosTable(n):
    Prime = []
    for i in range(2,n+1):
        Prime.append(i)
    del i

    for i in Prime:
        z = i
        j = 2
        while z*j < n:
            try:
                Prime.remove(z*j)
                j+=1
            except:
                j+=1
    return Prime