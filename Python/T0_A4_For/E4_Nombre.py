"""
Programa que lea un nombre y después 
imprima el nombre la cantidad de veces
que mida de longitud dicho nombre.
"""

nombre = input("Ingresa un Nombre Cualquiera: ")

if nombre == "":
    print("Debes escribir un nombre")

else:
    print()
    for i in range (len(nombre)):
        i = nombre
        print(i)