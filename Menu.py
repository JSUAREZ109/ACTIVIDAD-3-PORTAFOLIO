from agregar_producto import agregar_producto
from mostrar_productos import mostrar_productos
from calcular_total import calcular_total

def menu():
    productos = {}
    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Calcular total")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto(productos)
        elif opcion == '2':
            mostrar_productos(productos)
        elif opcion == '3':
            calcular_total(productos)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()
