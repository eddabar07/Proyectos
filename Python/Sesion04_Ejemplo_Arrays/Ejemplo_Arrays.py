"""
Estructura de DATOS que permite almacenar informacon del 
mismo tipo en conjunto

En Java los arrays son inmutables

En Python no existen como tal los Arrays (inmutables), las
estructuras de datos son mutables (List, Tuple, Dictionart)

Podemos simular el comportamiento de un Array estilo Java con
un List en Python
"""

array_vacio = []
array_temperaturas = [23.5, 34.7, 12.67, 90.8]
array_nombres = ["Luke", "Leia", "Han"]
array_edades = [45, 23, 20, 58]
array_objetos = ["Magia", 678, 0.1, True]

print(array_nombres)
print(array_nombres[2])

for dato in array_temperaturas:
    print(dato)

for i in range(len(array_edades)):
    print(array_edades [i])

# Obtener el promedio de temperaturas
suma_total = 0

for temp in array_temperaturas:
    suma_total += temp

promedio = suma_total / len(array_temperaturas)
print(promedio)

array_temperaturas[0] = 100.0
print(array_temperaturas)

array_calificaciones = []

cantidad = int(input("Cuantas calificaciones deseas ingresar: "))

for i in range(cantidad):
    array_calificaciones.append(int(input(f"Ingresa la calificacion {i+1}: ")))
print(array_calificaciones)

# Obtener el promedio de calificaciones, cuantas por encima del promedio y cuantas por debajo
array_calificaciones2 = []
suma = 0
cantidad = int(input("Cuantas calificaciones deseas ingresar: "))

for i in range(cantidad):
    array_calificaciones2.append(int(input(f"Ingresa la calificacion {i+1}: ")))

for j in array_calificaciones2:
    suma += j

promedio = suma / len(array_calificaciones2)

encima = 0
debajo = 0

for calificacion in array_calificaciones2:
    if calificacion > promedio:
        encima += 1
    elif calificacion < promedio:
        debajo += 1

print(f"\nPromedio: {promedio:.2f}")
print(f"Calificaciones por encima del promedio: {encima}")
print(f"Calificaciones por debajo del promedio: {debajo}")