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
import random

calificaciones = []
opcion = ""
suma = 0

limite = int(input("¿Cuántas calificaciones deseas ingresar?: "))

for i in range(limite):
    cantidad = calificaciones.append(random.randint(0, 100))

for j in range(0, len(calificaciones), 10):
    print(calificaciones[i:i + 10])

while opcion != "S":
    print("""
    A.- Obtener Promedio
    B.- Mostrar Cuantas Calificaciones Estan por Encima y Cuantas por Debajo del Promedio
    C.- Separar Calificaciones Aprobatorias y Reprobatorias
    S.- Salir
    """)
    opcion = input().upper()

    match opcion:
        case "A":
            for calificacion in calificaciones:
                suma += calificacion

            promedio = suma / len(calificaciones)
            print(f"Tu promedio es de: {promedio}")

        case "B":
            mayores_promedio = []
            menores_promedio = []
            iguales_promedio = []

            for calificacion in calificaciones:
                if calificacion > promedio:
                    mayores_promedio.append(calificacion)
                elif calificacion < promedio:
                    menores_promedio.append(calificacion)
                else:
                    iguales_promedio.append(calificacion)

            print(f"Calificaciones MAYORES al promedio: {mayores_promedio}")
            print(f"Calificaciones MENORES al promedio: {menores_promedio}")
            print(f"Calificaciones IGUALES al promedio: {menores_promedio}")

        case "C":
            aprobatorias = []
            reprobatorias = []

            for calificacion in calificaciones:
                if calificacion >= 70:
                    aprobatorias.append(calificacion)
                else:
                    reprobatorias.append(calificacion)

            print(f"Calificaciones aprobatorias: {aprobatorias}")
            print(f"Calificaciones reprobatorias: {reprobatorias}")

            if len(aprobatorias) > 0:
                suma_aprobatorias = 0

                for calificacion in aprobatorias:
                    suma_aprobatorias += calificacion

                promedio_aprobatorias = suma_aprobatorias / len(aprobatorias)

                print(f"Promedio de aprobatorias: {promedio_aprobatorias:.2f}")

            else:
                print("No hay calificaciones aprobatorias.")

            if len(reprobatorias) > 0:
                suma_reprobatorias = 0

                for calificacion in reprobatorias:
                    suma_reprobatorias += calificacion

                promedio_reprobatorias = suma_reprobatorias / len(reprobatorias)

                print(f"Promedio de reprobatorias: {promedio_reprobatorias:.2f}")
                
            else:
                print("No hay calificaciones reprobatorias.")

        case "S":
            print("Saliendo del programa...")

        case _:
            print("Opcion no valida, intenta de nuevo.")