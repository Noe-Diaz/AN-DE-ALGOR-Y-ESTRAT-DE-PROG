# Pedir frase al usuario.

frase = input("\nIngrese una frase: ")

# Contar las palabras.

palabras = frase.split()
cantidad_palabras = len(palabras)

# Contar letras 'a' o 'A'
cantidad_a = frase.lower().count("a")

print(f"Nùmero de palabras: {cantidad_palabras}")
print(f"Nùmero de veces que aparece la letra 'a': {cantidad_a}")
print("\n")