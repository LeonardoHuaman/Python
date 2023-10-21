print("Tipo de uva -> 1: Borgona,  2: Italia")

contador_toneladas_borgona = 0
numero_pedidos_italia = 0
for i in range(7):
    tipo_uva = int(input(f"Tipo de uva: {i + 1}: "))
    while tipo_uva != 1 and tipo_uva !=2:
        tipo_uva = input('Tipo de uva: ')
    
    peso_tonelada = int(input('Ingrese el peso en toneladas: '))
    while peso_tonelada <= 0:
        peso_tonelada = int(input('Ingrese el peso en toneladas: '))

    if tipo_uva == 1:
        contador_toneladas_borgona = contador_toneladas_borgona + peso_tonelada

    elif tipo_uva == 2:
        numero_pedidos_italia = numero_pedidos_italia + 1

    print("")

cantidad_viajes = contador_toneladas_borgona // 40


if contador_toneladas_borgona % 40 > 0:
    cantidad_viajes += 1

print("La empresa requerira: ", cantidad_viajes, "viajes.")
print("Numero de pedidos Italia: ", numero_pedidos_italia)

