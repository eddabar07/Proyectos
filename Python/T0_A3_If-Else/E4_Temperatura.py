# Leer una cantidad de grados FAHRENHEIT y convertirlos a CENTÍGRADOS, si la temperatura
# convertida es menor a 0, mostrar "CONGELANTE", en caso contrario mostrar "NORMAL"

temperatura = float(input("Ingresa la Temperatura en grados FHARENHEIT: "))

conversion_centigrados = (temperatura - 32) / 1.8

if conversion_centigrados < 0:
    print(f"{temperatura} grados fharenheit equivalen a {conversion_centigrados:.2f}, la temperatura es CONGELANTE")
else:
    print(f"{temperatura} grados fharenheit equivalen a {conversion_centigrados:.2f}, la temperatura es NORMAL")