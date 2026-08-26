"""
Crear un programa que calcule el salario neto de una persona con base en las
siguientes características:
    Salario Bruto = horas trabajadas * precio por hora + horas Extras
    Horas extras = horas extra trabajadas * (precio por hora * 2)
    Salario Neto = salario bruto - IVA - impuestos
"""

print("==========================================")
print("-----------------SALARIOS-----------------")
print("==========================================")

nombre = input("Ingresa el nombre del trabajador: ")
hrs_trabajadas = float(input("Ingresa el Numero de horas trabajadas: "))
precio_hora = float(input("Ingresa el precio por hora: $"))
hrs_extras_trab = float(input("Ingresa el numero de horas extras trabajadas: "))
impuesto = float(input("ingresa el Impuesto agregado en pesos: $"))

hrs_extras = hrs_extras_trab * (precio_hora * 2)
salario_bruto = hrs_trabajadas * precio_hora + hrs_extras
iva = salario_bruto * 0.16
salario_neto = salario_bruto - iva - impuesto

print(f"El salario de {nombre} es de ${salario_neto:.2f}")