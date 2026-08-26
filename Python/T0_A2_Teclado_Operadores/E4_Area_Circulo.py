# Crear un programa para obtener el área de un círculo.

import math

print("==============================================")
print("-----------------AREA CIRCULO-----------------")
print("==============================================")

radio = float(input("Ingresa el Valor del Radio del Circulo: "))

area = (math.pi * math.pow(radio, 2))

print(f"El Area del Circulo es de: {area}")