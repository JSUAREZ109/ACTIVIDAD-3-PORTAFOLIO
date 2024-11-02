def mostrar_productos(productos):
    if not productos:
        print("No hay productos disponibles.")
        return
    print("Productos disponibles:")
    for nombre, precio in productos.items():
        print(f"- {nombre}: ${precio:.2f}")
