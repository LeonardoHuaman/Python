# 3.	(5P) En el departamento de ventas de MITSUI S.A. se ha diseñado el siguiente sistema de 
# comisiones para sus vendedores a fin de incentivar las ventas:

# Ventas US $	 |Comisión
# Hasta  12,000  |	1%
# Mas de 12,000 y hasta 20,000	| 1% sobre los primeros 12,000 y 2% sobre la diferencia
# Más de 20,000	 | 1% sobre los primeros 12,000,  2% sobre los siguientes 8,000, y 3.5% sobre la diferencia.

# Se solicita un programa que calcule la comisión correspondiente, si se ingresa el monto vendido. 
# El monto vendido debe ser mayor a cero de lo contrario mostrar un mensaje de error y volverlo a solicitar hasta que cumpla con la regla. (5P)
for i in range(5):
    monto_venta = float(input("Ventas: "))

    while monto_venta <= 0:
        print("ERROR - MONTO NO VALIDO")
        print(" ")
        monto_venta = float(input("Ventas: "))
        
    if monto_venta <= 12000:
        comision = 0.01 * monto_venta
        print("Comision:", comision)
    elif monto_venta > 12000 and monto_venta <= 20000:
        comision = 0.01 * 12000 + (monto_venta - 12000) * 0.02
        print("Comision:", comision)

    elif monto_venta > 20000:
        comision = 0.01 * 12000 + 8000 * 0.02  + (monto_venta - 20000) * 0.035
        print("Comision:", comision) 

