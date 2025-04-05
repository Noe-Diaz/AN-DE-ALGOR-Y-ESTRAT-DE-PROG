#Creamos unalista para alamacenar las calificaciones de los estudiantes.

calificaciones = []

# Ingresar calificaciones.

for i in range(5):
    nota = float(input(f"Ingrese la calificación del estudiante {i+1}: "))
    calificaciones.append(nota)

# Calculamos y mostra,os el promedio

promedio = sum(calificaciones) / len(calificaciones)
print(f"\nPromedio general: {promedio:.2f}")