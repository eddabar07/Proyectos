# Programa que muestre los DIVISORES de un número ingresado desde teclado.

numero = int(input("Escriba un número cualquiera: "))

if numero <= 0:
    print("El número debe ser mayor que cero")

else:
    print(f"Los divisores de {numero} son: ")
    
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)