# 1. Ingreso de edad
edad = int(input("Ingrese su edad: "))

# 2. Condición anidada
if edad < 18:
    print("Eres menor de edad")
elif 18 <= edad <= 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
