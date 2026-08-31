"""
Obtener el salario de un trabajador con base en las siguientes formulas:
Salario bruto = días trabajados * pago por hora + DÍAS EXTRAS (Días extras son pagados al
doble. Si los días extras exceden de 5, se pagan al triple )
Salario neto = salario bruto - ISPT (ISPT es del 14%)
En caso de que el salario exceda de 20 mil, el ISPT será de 16%
"""

# Solicitud de datos al usuario
nombre = input("Ingresa el Nombre del Trabajador: ")
dias_trabajados = int(input("Ingresa el número de días trabajados: "))

# Validación de los días trabajados
if dias_trabajados < 0:
    print("Los días trabajados no pueden ser negativos")

elif dias_trabajados == 0:
    salario_bruto = 0
    ispt = 0
    salario_neto = 0
    print(f"\nEl Salario Bruto de {nombre} es de ${salario_bruto:.2f}")
    print(f"El Salario Neto de {nombre} es de ${salario_neto:.2f}")
    print(f"El descuento de ISPT fue de ${ispt:.2f}")

else:
    pago_hora = int(input("Ingresa el pago por hora: $"))

    # Validación de pago por hora
    if pago_hora < 0:
        print("El pago por hora no puede ser negativo")

    else:
        num_dias_extras = int(input("Ingresa el número de días extras: "))

        # Validación de días extras
        if num_dias_extras < 0:
            print("Los días extras no pueden ser negativos")

        elif num_dias_extras <= 5:
            dias_extra = num_dias_extras * pago_hora * 2
            salario_bruto = (dias_trabajados * pago_hora) + dias_extra

            if salario_bruto > 20000:
                ispt = salario_bruto * 0.16
            else:
                ispt = salario_bruto * 0.14

            salario_neto = salario_bruto - ispt

        else:
            dias_extra = num_dias_extras * pago_hora * 3

            salario_bruto = (dias_trabajados * pago_hora) + dias_extra

            if salario_bruto > 20000:
                ispt = salario_bruto * 0.16
            else:
                ispt = salario_bruto * 0.14

            salario_neto = salario_bruto - ispt

        # Mostrar resultados
        print(f"\nEl Salario Bruto de {nombre} es de ${salario_bruto:.2f}")
        print(f"El Salario Neto de {nombre} es de ${salario_neto:.2f}")
        print(f"El descuento de ISPT fue de ${ispt:.2f}")