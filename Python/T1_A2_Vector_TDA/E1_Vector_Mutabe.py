"""
Crear nuesra propia implementacion de VECTOR MUTABLE

1 -> Crear y llenar el arreglo
2 -> Obtener posición inicial 
3 -> Obtener posición final
4 -> Obtener cantidad de elementos
5 -> Mostrar todos los elementos
6 -> Mostrar elemento del inicio
7 -> Mostrar elemento del final
8 -> Aumentar tamaño del arreglo
9 -> Disminuir tamaño del arreglo
10 -> Insertar elemento en posición especifica
11 -> Insertar elemento en al inicio
12 -> Insertar elemento al final
13 -> Eliminar elemento de posición especifica
14 -> Eliminar elemento del inicio
15 -> Eliminar elemento del final
16 -> Invertir el vector
17 -> Buscar elemento
0 -> Salir del Programa
"""

class Vector:
    # Crear
    def __init__(self):
        self.datos = []

    # Llenar arreglo
    def llenar(self):
        cantidad = int(input("Ingresa el Tamaño deseado para el arreglo: "))
        for i in range (cantidad):
            valor = int(input(f"Ingresa el elemento {i + 1}: "))
            self.datos.append(valor)

    # Obtener posicion inicial
    def obtener_posicion_inicial(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return
        
        print("La posicion inicial es 0")

    # Obtener la posicion final
    def obtener_posicion_final(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return
        
        posicion_final = len(self.datos) - 1
        print(f"La posicion final es: {posicion_final}")

    # Obtener cantidad de elementos
    def obtener_cantidad_elementos(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return
        
        print(f"El arreglo tiene {len(self.datos)} elementos")

    # Mostrar todos los elementos
    def mostrar_todos_elementos(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return
        
        print(f"Elementos del arreglo: {self.datos}")

    # Mostrar el elemento del inicio
    def mostrar_elemento_inicio(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return
        
        print(f"El elemento INICIAL es: {self.datos[0]}")

    # Mostrar el elemento final
    def mostrar_elemento_final(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return
        
        print(f"El elemento FINAL es: {self.datos[-1]}")

    # Aumentar el tamaño del arreglo
    def aumentar_tamaño(self):
        cantidad = int(input("¿Cuántos lugares mas deseas agregar?: "))

        if cantidad <= 0:
            print("Cantidad invalida")
            return

        for i in range (cantidad):
            valor = int(input(f"Ingresa el elemento {i + 1}: "))
            self.datos.append(valor)

    # Disminuir el tamaño del arreglo
    def disminuir_tamaño(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return
        
        cantidad = int(input("¿Cuántos lugares mas deseas quitar?: "))
        
        if 0 < cantidad <= len(self.datos):
            del self.datos[-cantidad:]
            print(f"Se quitaron {cantidad} elementos.")
        else:
            print("Cantidad invalida.")

    # Insertar elemento en posicion especifica
    def insertar_posicion_especifica(self):
        nuevo_elemento = int(input("Ingresa el elemento: "))
        indice = int(input("¿En qué posicion lo deseas agregar? "))
        
        if 0 <= indice <= len(self.datos):
            self.datos.insert(indice, nuevo_elemento)
            print(f"Elemento {nuevo_elemento} insertado en la posicion {indice}.")
        else:
            print("Posicion invalida.")
            print(f"Debe estar entre 0 y {len(self.datos)}.")

    # Insertar elemento en la posicion inicial
    def insertar_posicion_inicial(self):
        nuevo_elemento = int(input("Ingresa el elemento: "))
        self.datos.insert(0, nuevo_elemento)
        print(f"Elemento {nuevo_elemento} insertado en la posicion 0.")

    # Insertar elemento en la posicion final
    def insertar_posicion_final(self):
        nuevo_elemento = int(input("Ingresa el elemento: "))
        self.datos.append(nuevo_elemento)
        print(f"Elemento {nuevo_elemento} insertado en la posicion {len(self.datos) - 1}.")

    # Eliminar elemento en una posicion especifica
    def eliminar_posicion_especifica(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return
        
        indice = int(input("¿Qué posicion deseas eliminar?: "))
        
        if 0 <= indice < len(self.datos):
            eliminado = self.datos.pop(indice)
            print(f"El elemento {eliminado} fue eliminado con éxito")
        else:
            print("Posicion invalida.")
            print(f"Debe estar entre 0 y {len(self.datos) - 1}.")

    # Eliminar elemento en la posicion inicial
    def eliminar_posicion_inicial(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return

        eliminado = self.datos[0]
        del self.datos[0]
        print(f"El elemento inicial {eliminado} se elimino con éxito")

    # Eliminar elemento en la posicion final
    def eliminar_posicion_final(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return

        eliminado =  self.datos[-1]
        del self.datos[-1]
        print(f"El elemento final {eliminado} se elimino con éxito")

    # Invertir el arreglo
    def invertir_arreglo(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return

        self.datos.reverse()
        print(f"Vector Invertido: {self.datos}")

    # Buscar elemento en el arreglo
    def buscar_elemento(self):
        if not self.datos:
            print("El arreglo esta vacio")
            return

        elemento = int(input("Ingresa el elemento a buscar: "))

        if elemento in self.datos:
            posicion = self.datos.index(elemento)
            print(f"El elemento {elemento} esta en la posicion {posicion}")

        else:
            print(f"El elemento {elemento} no existe")

# Instanciar la clase Vector()
v = Vector()

# Menu de opciones
opcion = -1
while opcion != 0:
    print("========== MENU DE OPCIONES AREGLOS ==========\n")
    print("""
    1 -> Crear y llenar el arreglo
    2 -> Obtener posición inicial 
    3 -> Obtener posición final
    4 -> Obtener cantidad de elementos
    5 -> Mostrar todos los elementos
    6 -> Mostrar elemento del inicio
    7 -> Mostrar elemento del final
    8 -> Aumentar tamaño del arreglo
    9 -> Disminuir tamaño del arreglo
    10 -> Insertar elemento en una posición especifica
    11 -> Insertar elemento al inicio
    12 -> Insertar elemento al final
    13 -> Eliminar elemento de una posición especifica
    14 -> Eliminar elemento del inicio
    15 -> Eliminar elemento del final
    16 -> Invertir el arreglo
    17 -> Buscar elemento
    0 -> Salir del Programa
    """)
    opcion = int(input())

    match opcion:
        case 1:
            v.llenar()
        case 2:
            v.obtener_posicion_inicial()
        case 3:
            v.obtener_posicion_final()
        case 4:
            v.obtener_cantidad_elementos()
        case 5:
            v.mostrar_todos_elementos()
        case 6:
            v.mostrar_elemento_inicio()
        case 7:
            v.mostrar_elemento_final()
        case 8:
            v.aumentar_tamaño()
        case 9: 
            v.disminuir_tamaño()
        case 10:
            v.insertar_posicion_especifica()
        case 11:
            v.insertar_posicion_inicial()
        case 12:
            v.insertar_posicion_final()
        case 13:
            v.eliminar_posicion_especifica()
        case 14:
            v.eliminar_posicion_inicial()
        case 15:
            v.eliminar_posicion_final()
        case 16:
            v.invertir_arreglo()
        case 17:
            v.buscar_elemento()
        case 0:
            print("Saliendo del programa...")
        case _:
            print("Opcion Invalida")