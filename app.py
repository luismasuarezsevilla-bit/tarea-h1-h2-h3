from servicios import *
from archivo import *
inventario =[]

while True:

    print("\n====Menu inventario")
    print("1. Agregar producto     2. Mostrar inventario")
    print("3. Buscar producto      4. Actualizar producto")
    print("5. Eliminar producto    6. Estadisiticas")
    print("7. Guardar CSV          8. Cargar CSV")
    print("             9. Salir")
    

    opcion = input("Eliga una opcion==>  ")

    try:
        opcion = int(opcion)

        if opcion == 1:

            nombre = input("Nombre: ")
            precio = float(input("precio: "))
            cantidad = int(input("cantidad: "))

            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:

            nombre = input("porducto a buscar: ")
            producto = buscar_producto(inventario, nombre)

            if producto:
                print(producto)

        elif opcion == 4:
            nombre = input("producto a actualizar: ")
            precio = float("Nuevo precio: ")
            cantidad = int("Nueva cantidad: ")

            actualizar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 5:

            nombre = input("Producto a eliminar: ")
            eliminar_producto(inventario, nombre)


        elif opcion == 6:
            stats = calcular_estadisticas(inventario)

            if stats:
                print(stats)

        elif opcion == 7:
            ruta = input("Ruta del archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == 8:

            ruta = input("Ruta del CSV: ")
            nuevos = cargar_csv(ruta)

            if nuevos:
                inventario = nuevos

        elif opcion == 9:

            print("Saliendo...")
            break

        else:
            print("Opcion invalida")

    except ValueError:
        print("Error: ingrese un numero valido")
        break