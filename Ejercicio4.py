print("Tener en cuenta: Recien Nacido = RN, Hombre = H, Mujer = M")
promedio = 0
numero_recien_nacidos = 0
mujeres_mal_saludad = 0
hombres_salud_observacion = 0

for i in range(20):
    print("Paciente", i+1)
    tipo = input("Tipo: ")
    while(tipo != "H" and tipo != "M" and tipo != "RN"):
       tipo = input("Tipo: ")
    hemoglobina = float(input("Homoglobina: "))
    hematocrito = float(input("Hematocrito: "))
    
    if(tipo == "RN"):
        promedio = promedio + hematocrito
        numero_recien_nacidos = numero_recien_nacidos + 1
    
    if (tipo == "H" and (hemoglobina < 14 or hemoglobina > 18) and (hematocrito >= 40 and hematocrito <= 54)):
        hombres_salud_observacion += 1
    elif (tipo == "H" and (hemoglobina >= 14 and hemoglobina <= 18) and (hematocrito < 40 or hematocrito > 54)):
        hombres_salud_observacion += 1

    elif (tipo == "M" and (hemoglobina < 12 or hemoglobina > 16) and (hematocrito < 37 or hematocrito > 47)):
        mujeres_mal_saludad += 1
    print("")
    
promedio = promedio/numero_recien_nacidos
print("Cantidad Mujeres 'Mal de salud':", mujeres_mal_saludad)
print("Canidad de Hombres 'Salud en observacion':",hombres_salud_observacion)
print("Promedio Hematocrito en Recien Nacidos (RN): ", promedio)

