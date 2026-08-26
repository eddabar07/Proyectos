# Crear un programa que pida una cantidad de grados Centígrados y los convierta en grados Fahrenheit y grados Rankine

print("=============================================")
print("-----------------TEMPERATURA-----------------")
print("=============================================")

temperatura = float(input("Ingresa la temperatura en grados centigrados: "))

grados_fahrenheit = (temperatura * 1.8) + 32
grados_rankine = (temperatura * 1.8) + 491.67

print(f"{temperatura} grados centigrados equivale a {grados_fahrenheit:.2f} grados Fahrenheit")
print(f"{temperatura} grados centigrados equivale a {grados_rankine:.2f} grados Rankie")
