# Comentarios en una sola linea

"""
Se puede utilizar como
comentarios multilinea, PERO REALMENTE
SON CREADOS PARA ALGO LLAMADO DOCSTRINGS
"""

"""
    FUNDAMENTOS DE PROGRAMACION

    1. Casi todo el codigo debe ir alineado a la izquierda, excepto
        estructuras de control y otras rutinas que se especifican
        con CUATRO ESPACIOS
    2. Los espacios en la parte izquierda del codigo son SINTACTICOS
    3. NO lleva punto y coma al final de cada linea
    4. Tipos de datos e Identificadores (VARIABLES)

    Python es de TIPADO DINAMICO (se infiere el tipo de dato al momento 
        de asignar us valor)

        Ejemplo: en JAVA (Tipado estatico):
            boolean sensor;
            byte edad; >= 1 byte
            int dato; >= 4 bytes

        En PYTHON
            edad = 45

    TIPOS DE DATOS EN PYTHON
            BASICOS
    - int
    - float
    - bool
    - str

            COMPUESTOS
    - List
    - Tuple
    - Dictionary

    FUNCIONES DE CONVERSION
    
    - Cadena a entero => int()
    - Cadena a real => float()
    - Cadena a booleano => bool()

    De cualquier tipo a cadena => str()
"""
print("----------Tipos de Datos----------")

print("Magia magia con PYTHON")
edad = 45
print(type(edad))
temperatua_sensor = 34.67
nombre = "Luke Skywalker"
encendido = False

edad = "Maria"
print(type(edad))

print("----------Operadores Aritmeticos----------")

a = 35
b = 67

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)

print("----------Lectura desde teclado----------")
año_nacimiento = int(input("Ingresa tu año de nacimiento: "))


print("Edad de una perosna en base a su año de nacimiento")

# año_nacimiento = 2000
edad = 2026 - año_nacimiento
print(f"Hola {nombre}, tu edad es: {edad}")

