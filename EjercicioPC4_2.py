def factorizacion_prima(n):
    factores=[]
    factor=2
    while factor<=n:
        if n%factor==0:
            factores.append(factor)
            
            n=n/factor
        else:
            factor+=1
    print("Los factores primos son:",factores)
    return


factorizacion_prima(666)

