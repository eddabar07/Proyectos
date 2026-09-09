class Alumno:
    # Variables de clase (no atributos)

    # Constructor
    def __init__ (self, nombre = "-", carrera = "-"):
        # Atributos
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = [100, 90, 80]
        x = 10 # Variable local dentro del constructor

    def metodoX(self):
        pass

    def obtenerPromedio(self, limite):
        suma = 0
        for cal in self.calificaciones:
            suma += cal
        return suma / len(self.calificaciones)
    

print("========== PRUEBA OBJETOS =========")
a1 = Alumno("Luke Skywalker", "ISC")
print(f"El promedio es: {a1.obtenerPromedio(10)}")
print(a1.nombre)