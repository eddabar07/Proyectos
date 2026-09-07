"""
Programa que pregunte al usuario cuantas calificaciones desea
ingresar, posteriormente leer dichas cailificaciones ingresadas por el usuario,
almacenarlas en un vector y obtener:

-> Promedio general del grupo
-> Promedio del grupo de calificaciones aprobatorias (70 o mayores)
-> Promedio del grupo, SOLO de calificaciones MAYORES AL PROMEDIO GENERAL
"""

calificaciones = []
aprobatorias = []
mayores_promedio = []
suma = 0
suma_aprobatorias = 0
suma_mayor_promedio = 0

# Solicitar limite de calificaciones
cantidad = int(input("¿Cuántas calificaciones deseas ingresar?: "))

# Determinar el promedio general del grupo
for i in range(cantidad):
    calificaciones.append(int(input(f"Ingresa la calificación {i + 1}: ")))

for calificacion in calificaciones:
    suma += calificacion

promedio = suma / len(calificaciones)

# Determinar el promedio de las calificaciones mayores a 70
for calificacion in calificaciones:
    if calificacion >= 70:
        aprobatorias.append(calificacion)

for calificacion in aprobatorias:
    suma_aprobatorias += calificacion

if len(aprobatorias) > 0:
    promedio_aprobatorias = suma_aprobatorias / len(aprobatorias)
    
else:
    promedio_aprobatorias = 0

# Determinar promedio de las calificaciones mayores al promedio general
for calificacion in calificaciones:
    if calificacion > promedio:
        mayores_promedio.append(calificacion)

for calificacion in mayores_promedio:
    suma_mayor_promedio += calificacion

if len(mayores_promedio) > 0:
    promedio_mayor = suma_mayor_promedio / len(mayores_promedio)

else:
    promedio_mayor = 0

print(f"El promedio general del grupo es de {promedio}")
print(f"El promedio de las calificaciones mayores a 70 es de {promedio_aprobatorias}")
print(f"El promedio de las calificaciones que son mayores al promedio general es de {promedio_mayor}")