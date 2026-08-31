"""
Programa que lea una cadena e indique CUANTAS 
letras son VOCALES, cuantas sonCONSONANTES, 
cuantas son NÚMEROS y cuantas CARACTERES ESPECIALES.
"""

cadena = input("Ingresa una cadena: ")

vocales = 0
consonantes = 0
numeros = 0
especiales = 0

for caracter in cadena:

    ascii = ord(caracter)

    # Vocales: A, E, I, O, U
    if ascii == 65 or ascii == 69 or ascii == 73 or ascii == 79 or ascii == 85 or \
       ascii == 97 or ascii == 101 or ascii == 105 or ascii == 111 or ascii == 117:
        vocales += 1

    # Consonantes: A-Z y a-z, excepto vocales
    elif (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        consonantes += 1

    # Números: 0-9
    elif ascii >= 48 and ascii <= 57:
        numeros += 1

    # Caracteres especiales
    else:
        especiales += 1

print(f"Cantidad de vocales: {vocales}")
print(f"Cantidad de consonantes: {consonantes}")
print(f"Cantidad de números: {numeros}")
print(f"Cantidad de especiales: {especiales}")