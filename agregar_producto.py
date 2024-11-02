def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ").strip().upper()
    precio = float(input("Ingrese el precio unitario del producto: "))
    productos[nombre] = precio
