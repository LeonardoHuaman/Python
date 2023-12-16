#Suma de cuadrados diagonal 
import numpy as np
matriz1 = np.random.randint(100)

diagonal= np.diag(matriz1)
print(diagonal)

diagonal_cuadrados=[]
for i in range(len(diagonal)):
    cudrado = diagonal[i] * diagonal[i]
    diagonal_cuadrados.append(cudrado)
print(diagonal_cuadrados)


suma = sum(diagonal_cuadrados)
print(suma)

determinante=np.linalg.det(matriz1) 
print(determinante)
