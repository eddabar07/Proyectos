"""
Crear un programa que pida al usuario una temperatura en grados centígrados y después
pregunte al usuario si desea convertir a grados Fahrenheit o grados Kelvin; dependiendo de
la opción elegida,pedir los datos necesarios para obtener dicha conversión y mostrar le
resultado en pantalla.
"""

tempt_deseada = input("Ingresa el simbolo de la temperatura a convertir (Fharenheit - F, Kelvin - K): ").upper()

if tempt_deseada == "F":
    temp_cent = float(input("Ingresa la temperatura en grados centigrados: "))
    grados_f = (temp_cent * 1.8) + 32
    print(f"\n{temp_cent}° Centigrados = {grados_f}° Fharenheit")

elif tempt_deseada == "K":
    temp_cent = float(input("Ingresa la temperatura en grados centigrados: "))
    grados_k = temp_cent +  273.15
    print(f"\n{temp_cent}° Centigrados = {grados_k}° Kelvin")

else:
    print("Simbolo Incorrecto")