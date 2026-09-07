"""
Crear un programa que llene un vector de temperaturas, con el formato
"34.12 °C" o "78.4 °F". Preguntar al usuario cuantas temperaturas desea
ingresar, leer dichas temperaturas y una vez llenado el vector, mostrar el
promedio de las temperaturas en grados Centigrados y el promedio de las
temperaturas en grados Fahrenheit.
"""

temperaturas_originales = []
celsius = []
fahrenheit = []

# Solicitar limite de temperaturas
limite = int(input("¿Cuántas temperaturas deseas guardar?: "))

# Llenar array
for i in range(limite):
    dato = temperaturas_originales.append(input(f"Ingresa la temperatura {i + 1} (ejemplo: 34.12 C o 78.4 F): "))

    # Separar el valor numerico de la unidad
    partes = dato.split()
    valor = float(partes[0])
    unidad = partes[1]

# Realizar operacion segun el tipo de temperatura
    match unidad:
        case "C":
            valor_c = valor
            valor_f = (valor_c * 9 / 5) + 32
        case "F":
            valor_f = valor
            valor_c = (valor_f - 32) * 5 / 9
        case _:
            print("Unidad no reconocida, se omitira este dato")
            continue

# Agregar temperatura al array segun corresponda
    celsius.append(valor_c)
    fahrenheit.append(valor_f)

# Calcular promedios
suma_c = 0
for temp in celsius:
    suma_c += temp
promedio_c = suma_c / len(celsius)

suma_f = 0
for temp in fahrenheit:
    suma_f += temp
promedio_f = suma_f / len(fahrenheit)

# Resultados
print(f"\nTemperaturas ingresadas: {temperaturas_originales}")
print(f"Promedio en grados Centigrados: {promedio_c:.2f} °C")
print(f"Promedio en grados Fahrenheit: {promedio_f:.2f} °F")