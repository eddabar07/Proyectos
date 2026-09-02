"""
CADENAS o STRINGS (en Python Str)

    Es un cojunto de 0-N caracteres formado por
    LETRAS, NUMEROS y/o CARACTERES ESPECIALES

"""
cadena_vacia = ""
nombre = "Luke Skywalker"
edad = "30"
temperatura1 = "45.8 C"
temperatura2 = "23.1 F"

print(temperatura1 + temperatura2)

cad = "Ingenieria en Sistemas Computacionales"

print(cad.upper())
print(f"Total de caracteres en una cadena: {len(cad)}")
print(cad.find("a"))
print(cad.find("en"))
print(cad.find("Sistemas"))

print(cad.count("a"))
print(cad.count("t"))
print(cad.count("C"))
print("magia7".isalnum())
print("magia".isalpha())
print("7".isnumeric())
print("7.2".isnumeric())

print(cad.replace("a", "@"))
print(cad.replace(" ", ""))

print("========== TECNICA de SLICING ==========")
print(cad[5:10])
print(cad[:])
print(cad[20:])
print(cad[:15])
print(cad[::-1])
print(cad[3])

print("========== ANALISIS DE CADENAS ==========")

vocales = 0
for i in range(len(cad)):
    cad2 = cad.upper()
    if cad2[i] == "A" or cad2[i] == "E" or cad2[i] == "I" or cad2[i] == "O" or cad2[i] == "U":
        vocales += 1

print(vocales)

for i in range(65000):
    print(chr(i), end='\n' if (i + 1) % 50 == 0 else ' ')   
       