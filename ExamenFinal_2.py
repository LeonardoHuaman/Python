#Solucion de ecuaciones
import numpy as np
coefi =np.array([[4 , 6, 2, -2],
                 [8 ,-2, 3, 2],
                 [5,  2, 3, -1],
                 [3, -2, 4, 1]])

print(coefi)
const=np.array([150,130,120,100]) 
solucion=np.linalg.solve(coefi,const)
print(solucion)
 
print("x=",round(solucion[0],2))
print("y=",round(solucion[1],2))
print("z=",round(solucion[2],2))
print("w=",round(solucion[3],2))
