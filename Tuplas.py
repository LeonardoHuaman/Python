'''
- ¿QUE SON LAS TUPLAS?
  Las es igual que las listas pero no son inmutables,
  es decir, no se puede eliminar o agragar elementos
'''

tupla = ("Hola", 10, 6,12, "Luis es gay", [1,2,3])
print(tupla)

# EN TUPLAS NO SE PUEDE HACER APPEND, POP, INSERT, ETC...
# BUSQUEDAS SI ESTA PERMITIDO
# LEN TAMBIEN ESTA PERMITIDO

# TRANSFORMAR LISTA EN TUPLA

lista = list(tupla)
print(lista)

# LA TUPLA NO SE MODIFICA, SOLO SE CREA UNA COPIA PARA 
# LISTA
