"""
ESTRUCTURAS DE CONTROL
    CONDICIONALES
        1.- If - Then - Else
    SINTAXIS: if condiciones:
                  codigo del if
                  codigo del if
                  ....
                  codigo del if
              else:
                  codigo else
                  codigo else

              Codigo fuera el if - else

    OPERADORES RELACIONALES
        ==
        !=
        >=
        <=
        >
        <          

    OPERADORES LOGICOS
        and
        or
        not
    
    REPETITIVAS
        1.- For
    SINTAXIS: for variable_indice in datos:
                  codigo for
                  codigo for
                  ....
                  codigo for

              fuera del ciclo for  
        2.- While
"""
print("========== ESTRUCTURAS DE CONTROL ==========")

if True:
    print("Siempre")
if False:
    print("Nunca")

a = 324
b = 43
c = 78

if a > b and c != a or b < c:
    print("Si entra")
else:
    print("No entra")

    
if a > b and c != a and b > c:
    print("Si entra")
else:
    print("No entra")

calificacion = 100

if calificacion >= 91 and calificacion <= 100:
    print("Excelente")
elif calificacion >= 81 and calificacion <= 90:
    print("Muy bien")
elif calificacion >= 70 and calificacion <= 80:
    print("Bien")
elif calificacion >= 0 and calificacion <= 69:
    print("Terrible")
else:
    print("Calificacion Incorrecta")

print("========== CICLO FOR ==========")

for i in range (10):
    print(i)

print()
for i in range (20, 51):
    print(i)

print()
for i in range (20, 51, 5):
    print(i)

print()
for i in range (20, 0, -1):
    print(i)

# Ejercicio: Obtener el promedio de 5 calificaciones
rango = int(input("Ingresa el Numero de calificaciones a promediar: "))
suma_calif = 0

for i in range (rango):
    suma_calif += int(input(f"Ingresa la calificacion {i+1}: "))

promedio = suma_calif / rango
print(f"El promedio de calificaciones es {promedio}\n")

# Ejercicio 2a: Imprimir una tabla de multiplicar
tabla = int(input("Ingresa el numero de la tabla de multiplicar: "))

for i in range (101):
    resultado = tabla * i
    print(f"{tabla} * {i} = {resultado}")
print()

# Ejercicio 2b: Imprimir una tabla de multiplicar y preguntar el limite
tabla = int(input("Ingresa el numero de la tabla de multiplicar: "))
limite = int(input("Ingresa el limite deseado: "))

for i in range (1, limite + 1):
    resultado = tabla * i
    print(f"{tabla} * {i} = {resultado}")
print()

# Ejercicio 3: Preguntar al usuiario cuantas tablas desea imprimir (comenzando
# desde la tabla del 1, hasta la que indique el usuario) y preguntar tambien
# el limite

tablas = int(input("¿Cuantas Tabalas desea Imprimir?: "))
limite = int(input("Ingresa el limite de las tablas: "))

for i in range (1, tablas + 1):
    print()
    for j in range (1, limite + 1):
        result = i * j
        print(f"{i} * {j} = {result}")