"""
Crear un programa que llene un vector de temperaturas, con el formato
34.12. Preguntar al usuario cuantas temperaturas desea ingresar, leer dichas
temperaturas y una vez llenado el vector, mostrar las temperaturas mayores y
menores al promedio.
"""
temperaturas = []
mayores_promedio = []
menores_promedio = []
iguales_promedio = []
suma = 0

# Solicitar el limite
limite = int(input("¿Cuántas temperaturas deseas guardar?: "))

# Lenar array
for i in range(limite):
    cantidad = temperaturas.append(float(input(f"Ingresa la temperatura {i + 1}: ")))

# Sumar los datos del array
for temp in temperaturas:
    suma += temp

# Calcular el Promedio
promedio = suma / len(temperaturas)

# Determinar las temperaturas mayores, menores o iguales al promedio
for temp in temperaturas:
    if temp > promedio:
        mayores_promedio.append(temp)
    elif temp < promedio:
        menores_promedio.append(temp)
    else:
        iguales_promedio.append(temp)

# Resultados
print(f"\nTemperaturas Ingresadas: {temperaturas}")
print(f"Promedio general: {promedio:.2f}")
print(f"Temperaturas MAYORES al promedio general: {mayores_promedio}")
print(f"Temperaturas MENORES al promedio general: {menores_promedio}")
print(f"Temperaturas IGUALES al promedio general: {iguales_promedio}")