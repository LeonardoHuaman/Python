"""
- ¿QUE SON LAS LISTAS?
  Son estructuras de datos o un arreglo de elementos
  donde podemos ingresar cualquier tipo de dato.
  
  Se accede mediante un indice 
"""

# Ejemplo de Listas

lista = ["Leonardo", "es", "mejor", "jugando dota", 10]
print(lista)

# Accediendo mediante el indice

print(lista[0])

# Accediendo mediante un rango de indices

print(lista[0:2])
print(lista[2:4])

for i in range(len(lista)):
  print(lista[i])


# Concatenacion de Listas

lista2 = ["y", "Alejo", "es", "su", "hijo", "en", "dota"]
print(lista2)

lista3 = lista + lista2
print(lista3)

# Listas en listas

lista4 = [lista, lista2]
print(lista4)
print(lista4[0][0][0])

# Mas operaciones

frutas = ["manzana", "platano", "fresa"]
print(frutas[-1]) #Accede al ultimo valor del array

# Reemplazar un valor
frutas[0] = "mango"
print(frutas)

# Agregar un elemento al final
frutas.append("manzana")
print(frutas)

# Insertar eun elemento en una posicion en especifica
frutas.insert(0, "pera")
print(frutas)

# Cuantos valores hay en la lista
#print(len(frutas))

# Borrar un elemento de la lista
#frutas.remove("manzana")
#print(frutas)

#Borrar un elemrnto de acuerdo a su posicion
#frutas.pop(0)
#print(frutas)

#del frutas[0]
#print(frutas)

# Buscar un elemento
#print("papaya" in frutas)

#Saber el indice de un elemento
#print(frutas.index("platano"))

# El usuario ingrese su fruta

#frutas.append(input("Ingrese su fruta: "))
#print(frutas)
