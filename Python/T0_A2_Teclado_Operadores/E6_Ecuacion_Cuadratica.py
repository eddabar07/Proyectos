# Crear un programa que solucione la ecuación cuadrática.

import cmath, math

print("=====================================================")
print("-----------------ECUACION CUADRATICA-----------------")
print("=====================================================")

a = float(input("Ingresa el valor de A: "))
b = float(input("Ingresa el valor de B: "))
c = float(input("Ingresa el valor de C: "))

d = abs(math.pow(b, 2) - (4 * a * c))

sol1 = (-b + cmath.sqrt(d)) / (2 * a)
sol2 = (-b - cmath.sqrt(d)) / (2 * a)

print(f"Las soluciones son: x = {sol1} y x = {sol2}")