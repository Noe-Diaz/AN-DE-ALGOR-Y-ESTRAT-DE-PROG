from dataclasses import dataclass

# Definimos 
@dataclass

class Estudiante:
    nombre: str
    edad: int
    carrera: str

# Creamos la lista de estudiantes
estudiantes = [
    Estudiante("Ana", 20, "Ingeniería de Sistemas"),
    Estudiante("Luis", 22, "Administración"),
    Estudiante("María", 21, "Psicología")
]

#Mostrar

print("\nLista de estudiantes: ")
print("")
for est in estudiantes:
    print(f"Nombre: {est.nombre}, Edad: {est.edad}, Carrera: {est.carrera}")
print("\n")