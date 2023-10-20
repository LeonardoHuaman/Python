numero = int(input("Ingrese numero de 5 cifras: "))
while(numero<10000 or numero>99999):
    numero = int(input("Ingrese numero de 5 cifras: "))

d_m = (numero//10000) * 10000
numero = numero - d_m

u_m = (numero//1000) * 1000
numero = numero - u_m

centena = (numero//100) * 100
numero = numero - centena

decena = (numero//10) * 10 
unidad = numero - decena

print(d_m,"+" ,u_m, "+", centena , "+", decena, "+", unidad)
 