# Programa que lea tres números e indicar cual es el mayor.

numero1 = int(input("Ingresa el Primer Número: "))
numero2 = int(input("Ingresa el Segundo Número: "))
numero3 = int(input("Ingresa el Tercer Número: "))

if numero1 >= numero2 and numero1 >= numero3:
    print(f"\nEl número mayor es {numero1}")

elif numero2 >= numero1 and numero2 >= numero3:
    print(f"\nEl número mayor es {numero2}")

else:
    print(f"\nEl número mayor es el {numero3}")
