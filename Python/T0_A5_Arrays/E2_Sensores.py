"""
Programa que llena de forma aleatoria un vector de tipo BOOLEAN con 24
datos, estos simulan la activacion e inactivacion de sensores. Obtener:

-> Si cada dato simula una lectura por hora, indicar si hubo 
mas abiertos o cerrados en el dia (primeras 12 horas) y en
la noche (segundas 12 horas)
"""

import random

sensores = []
abiertos_dia = 0
cerrados_dia = 0
abiertos_noche = 0
cerrados_noche = 0

# Generar y llenar sensores[] con valores random de True o False 
for i in range(24):
    sensores.append(random.choice([True, False]))

# Lectura por hora
for hora in range(24):

    if sensores[hora]:
        estado = "Abierto"
    else:
        estado = "Cerrado"

    print(f"{hora:02d}:00: {estado}")

# Separar el array en dia (horas 0-11) y noche (horas 12-23)
dia = sensores[0:12]
noche = sensores[12:24]

# Contar abiertos y cerrados en el dia
for valor_dia in dia:
    if valor_dia:
        abiertos_dia += 1
    else:
        cerrados_dia += 1

# Contar abiertos y cerrados en la noche
for valor_noche in noche:
    if valor_noche:
        abiertos_noche += 1
    else:
        cerrados_noche += 1

# Resultados del dia
print("\n========== Resultados del DIA ==========")
print(f"Sensores abiertos: {abiertos_dia}")
print(f"Sensores cerrados: {cerrados_dia}")

if abiertos_dia > cerrados_dia:
    print("Hubo más sensores ABIERTOS durante el dia.")

elif cerrados_dia > abiertos_dia:
    print("Hubo más sensores CERRADOS durante el dia.")

else:
    print("Hubo la misma cantidad de sensores abiertos y cerrados durante el dia.")

# Resultados de la noche
print("\n========== Resultados del la NOCHE ==========")
print(f"Sensores abiertos: {abiertos_noche}")
print(f"Sensores cerrados: {cerrados_noche}")

if abiertos_noche > cerrados_noche:
    print("Hubo mas sensores ABIERTOS durante la noche.")
    
elif cerrados_noche > abiertos_noche:
    print("Hubo mas sensores CERRADOS durante la noche.")

else:
    print("Hubo la misma cantidad de sensores abiertos y cerrados durante la noche.")