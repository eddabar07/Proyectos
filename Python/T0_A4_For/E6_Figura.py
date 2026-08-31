"""
Programa que imprima una figura similar al ejercicio 5, 
pero con ALTURA indicada por el usuario.
"""

filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

for i in range(filas):
    for j in range(columnas):
        print("@", end="")
    print()
        