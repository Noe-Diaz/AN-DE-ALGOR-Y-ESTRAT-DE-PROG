# Diccionario de prodcutos y precios 

productos = {
    "manzana": 2.5,
    "pan": 1.2,
    "leche": 3.0,
    "arroz": 2.0
}

# Ingresar producto a consultar.

producto = input("\nIngrese el nombre dek producto: ").lower()

# Mostrar precio si existe el producto

if producto in productos:
    print(f"El precio de {producto} es: S/. {productos[producto]}")
else:
    print("Producto no encontrado.")