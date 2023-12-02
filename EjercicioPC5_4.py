def calcular_volumen_cilindro():
    r=float(input("Ingrese radio: "))
    h=float(input("Ingrese altura: "))
    pi=3.14159
    volumen=pi*(r**2)*h
    return volumen

print("Volumen:",calcular_volumen_cilindro())
