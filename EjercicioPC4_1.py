def combinaciones(n,r):
    factn=1
    for i in range(1,n+1):
        factn = factn * i
        
    factr=1
    for i in range(1,r+1):
        factr=factr * i
        
    factnr=1
    for i in range(1,n-r+1):
        factnr=factnr * i
        
    combinatoria= factn/(factnr*factr)
    return combinatoria

def permutaciones(n,r):
    factn=1
    for i in range(1,n+1):
        factn*=i
        
    factnr=1
    for i in range(1,n-r+1):
        factnr*=i
        
    permutacion=factn/factnr
    return permutacion


print("La combinatoria:",combinaciones(10,5))
print("La permutacion:",permutaciones(10,5))