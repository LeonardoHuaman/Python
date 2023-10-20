compra = int(input("Ingrese monto de compra: $"))
while (compra<0):
    compra = int(input("Ingrese monto de compra: $"))

if(compra <= 1500):
    descuento = 0
    monto_total = compra
else:
    descuento = compra*0.20
    monto_total = compra - descuento
    
print("El descuento es: ", round(descuento,2))
print("El monto toal es: ", round(monto_total,2))