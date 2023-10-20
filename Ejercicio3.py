monto = float(input("Monto de venta: "))
while (monto <= 0):
    print("ERROR - MONTO NO VALIDO")
    print("")
    monto = float(input("Monto de venta: "))
    
if monto <= 12000:
    comision = monto * 0.01
elif monto <= 20000:
    comision = 12000 * 0.01 + (monto - 12000) * 0.02
else:
    comision = 12000 * 0.01 + 8000 * 0.02 + (monto - 20000) * 0.035
    
print("Comision correspondiente:", comision)
