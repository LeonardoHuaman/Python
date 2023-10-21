#
#   1.	(5P) Solicitar un número de 5 dígitos (Validar). El programa deberá mostrar la descomposición polinómica del número.
#   Ejemplo: 
#   Ingrese número: 12345
#   Resultado: 10000 + 2000 + 300 + 40 + 5
for i in range(5):
    numero = int(input("Numero 5 digitos: "))

    while numero <= 9999 or numero >= 100000: 
        numero = int(input("Numero 5 digitos: "))

    d_m = numero // 10000
    d_m = d_m * 10000
    numero = numero % 10000

    u_m = numero // 1000
    u_m = u_m * 1000
    numero = numero % 1000

    centena = numero // 100
    centena = centena * 100
    numero = numero % 100

    decena = numero // 10
    decena = decena * 10
    numero = numero % 10

    unidad = numero

    print(d_m, "+", u_m, "+", centena, "+", decena, "+", unidad)



