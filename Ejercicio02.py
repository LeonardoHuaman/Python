# 2.	(5P) Una distribuidora de bebidas al por mayor, ofrece un 20% de descuento a los clientes cuya compra supere los $1500. 
# Desarrollar un programa que calcule y muestre el descuento asignado y el total a pagar por el cliente. 
# Solicitar al cliente el monto de la compra. (5P)
   
monto = float(input('Monto: $'))

if monto > 1500:
    descuento = monto * 0.20
    monto_total = monto * 0.80
    print ("Descuento: ", round(descuento,2))
    print ("Total: ", round(monto_total,2))

else :
    print ("Monto total: ", monto)
