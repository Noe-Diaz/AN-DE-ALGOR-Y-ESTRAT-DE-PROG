# 1. Ingreso de calificación
calificacion = int(input("Ingrese su calificación (0-100): "))

# 2. Clasificación con if-elif-else
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")

# 3. Operador ternario
mensaje = "Aprobado" if calificacion >= 70 else "Reprobado"
print(mensaje)

# 4. Uso de match-case
match calificacion:
    case _ if calificacion >= 90:
        print("Sobresaliente")
    case _ if 70 <= calificacion < 90:
        print("Bueno")
    case _ if 50 <= calificacion < 70:
        print("Regular")
    case _:
        print("Deficiente")
