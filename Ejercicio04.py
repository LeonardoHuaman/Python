#4.	(5P) Se desea diagnosticar a 20 pacientes sobre su hemoglobina y hematocrito en la costa (nivel del mar), tomando en cuenta la tabla que se muestra, 
# el programa debe hacer reportes:

#•	“Bien de salud”: Si está en el rango permisible de hemoglobina y hematocrito. 
#•	“Salud en observación”: Si solo uno de ellos (hemoglobina y hematocrito) está en el rango.
#•	“Mal de salud”: Si ninguno de ellos (hemoglobina y hematocrito) está en el rango.

# Cifras normales de hemoglobina y hematocrito al nivel del mar (Wintrobe)
#   	        Hemoglobina	   Hematocrito
# Recién nacido	19.5 +/- 5.0	54 +/- 10
# Mujeres	    14.0 +/- 2.0    42 +/- 5
# Hombres	    16.0 +/- 2.0    47 +/- 7

# El programa deberá solicitar el tipo de paciente (“Recién nacido”, “Mujer” u “Hombre”), solicitar su nivel de Hemoglobina y de Hematocrito.

# Se solicita:
# a)	Cantidad de pacientes Mujeres “Mal de salud”
# b)	Cantidad de pacientes Hombres con “Salud en Observación”
# c)	Promedio de Hematocrito en Recién Nacidos

print("Tener en cuenta: Recien Nacido = RN, Hombre = H, Mujer = M")
suma_hematocrito = 0
numero_recien_nacidos = 0
mujeres_mal_saludad = 0
hombres_salud_observacion = 0

for i in range(5):
    print("Paciente", i+1)
    
    tipo = input("Tipo: ")
    while(tipo != "H" and tipo != "M" and tipo != "RN"):
       tipo = input("Tipo: ")


    hemoglobina = float(input("Homoglobina: "))
    hematocrito = float(input("Hematocrito: "))
    
    if(tipo == "RN"):
        suma_hematocrito = suma_hematocrito + hematocrito
        numero_recien_nacidos = numero_recien_nacidos + 1
    
    elif (tipo == "H" and (hemoglobina < 14 or hemoglobina > 18) and (hematocrito >= 40 and hematocrito <= 54)):
        hombres_salud_observacion += 1

    elif (tipo == "H" and (hemoglobina >= 14 and hemoglobina <= 18) and (hematocrito < 40 or hematocrito > 54)):
        hombres_salud_observacion += 1

    elif (tipo == "M" and (hemoglobina < 12 or hemoglobina > 16) and (hematocrito < 37 or hematocrito > 47)):
        mujeres_mal_saludad += 1
    print("")
    
promedio = suma_hematocrito/numero_recien_nacidos
print("Cantidad Mujeres 'Mal de salud':", mujeres_mal_saludad)
print("Canidad de Hombres 'Salud en observacion':",hombres_salud_observacion)
print("Promedio Hematocrito en Recien Nacidos (RN): ", promedio)
