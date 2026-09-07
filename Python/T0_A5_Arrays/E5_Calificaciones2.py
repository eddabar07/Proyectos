"""
Llenar un arreglo de tamaño indicado por el usuario, con números
aleatorios del 0 al 100, los cuales representan calificaciones. Mostrar al usuario
el siguiente menú:
1) Obtener el promedio de calificaciones

2) Mostrar cuantas calificaciones están por encima del promedio y cuantas
por debajo.

3) Separar calificaciones aprobatorias y reprobatorias (almacenarlas en
otros vectores)
    3a) Mostrar promedio de calificaciones aprobatorias
    3b) Mostrar promedio de calificaciones reprobatorias
"""
# Importacion de la libreria 'random'
import random

# Declaracion de variables
calificaciones = []
mayores_promedio = []
menores_promedio = []
iguales_promedio = []
aprobatorias = []
reprobatorias = []
opcion = ""
suma = 0
suma_aprobatorias = 0
suma_reprobatorias = 0

# Solicitar limite
limite = int(input("¿Cuántas calificaciones deseas generar?: "))

# Rellenar array con respecto al limite
for i in range(limite):
    cantidad = calificaciones.append(random.randint(0, 100))

# Acomodar datos de 10 en 10
for j in range(0, len(calificaciones), 10):
    print(calificaciones[j:j + 10])

# Menu de opciones (Consola)
while opcion != "S":
    print("""
    A.- Obtener Promedio
    B.- Mostrar Cuantas Calificaciones Estan por Encima y Cuantas por Debajo del Promedio
    C.- Separar Calificaciones Aprobatorias y Reprobatorias
    S.- Salir
    """)
    opcion = input().upper()

# Menu de opciones (logica)
    match opcion:
        case "A":
            # Definir el promedio
            if len(calificaciones) > 0:

                for calificacion in calificaciones:
                    suma += calificacion

                promedio = suma / len(calificaciones)
                print(f"Tu promedio es de: {promedio}")

            else:
                print("No se genero ninguna calificación")

        case "B":
            # Definir el promedio
            if len(calificaciones) > 0:
            
                for calificacion in calificaciones:
                    suma += calificacion
            
                promedio = suma / len(calificaciones)
                print(f"Tu promedio es de: {promedio}")

            # Determinar calificaciones por encima del promedio
                for calificacion in calificaciones:
                    if calificacion > promedio:
                        mayores_promedio.append(calificacion)

            # Determinar calificaciones por debajo del promedio
                    elif calificacion < promedio:
                        menores_promedio.append(calificacion)

            # Determinar calificaciones iguales al promedio
                    else:
                        iguales_promedio.append(calificacion)

            # Impresion de resultados
                print(f"Calificaciones MAYORES al promedio: {mayores_promedio}")
                print(f"Calificaciones MENORES al promedio: {menores_promedio}")
                print(f"Calificaciones IGUALES al promedio: {iguales_promedio}")

            else:
                print("No se genero ninguna calificación")

        case "C":
            # Determinar califiaciones aprobatorias y reprobatorias
            for calificacion in calificaciones:
                if calificacion >= 70:
                    aprobatorias.append(calificacion)
                else:
                    reprobatorias.append(calificacion)

        # Impresion de calificaciones
            print(f"Calificaciones aprobatorias: {aprobatorias}")
            print(f"Calificaciones reprobatorias: {reprobatorias}")

        # Determinar el promedio de las calificaciones aprobatorias
            if len(aprobatorias) > 0:

                for calificacion in aprobatorias:
                    suma_aprobatorias += calificacion

                promedio_aprobatorias = suma_aprobatorias / len(aprobatorias)

                print(f"Promedio de aprobatorias: {promedio_aprobatorias:.2f}")

            else:
                print("No hay calificaciones aprobatorias.")

            # Definir el promedio de las calificaciones reprobatorias
            if len(reprobatorias) > 0:

                for calificacion in reprobatorias:
                    suma_reprobatorias += calificacion

                promedio_reprobatorias = suma_reprobatorias / len(reprobatorias)

                print(f"Promedio de reprobatorias: {promedio_reprobatorias:.2f}")
                
            else:
                print("No hay calificaciones reprobatorias.")

        # Opcion para salir del programa
        case "S":
            print("Saliendo del programa...")

        # Default
        case _:
            print("Opcion no valida, intenta de nuevo.")