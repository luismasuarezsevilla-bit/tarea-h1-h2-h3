# Este bucle se repite hasta que el usuario ingrese un nombre válido. 
while True:
    nombre = input("Ingrese el nombre del producto: ")
    if nombre.replace ("  ", "").isalpha():
        print("Error: el nombre del producto no puede ser un número.")
    else:
        break
        
# Este es el Bucle de validacion del precio. 
# Se repite hasta que el usuario ingrese un numero no negativo. 
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo, intente nuevamente.")
            continue
        break
    except ValueError:
        print("Valor invalido. Debe ingresar un numero para el precio.")

# Este es el Bucle para validar la cantidad. 
# Convierte la entrada a entero y verifica que no sea negativa. 
while True:
    try:
        cantidad = int(input("ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa. Intentelo nuevamente.")
            continue
        break
    except ValueError:
        print("Valor invalido. Debe ingresar un numero entero para la cantidad.")

# Este calcula el costo total.
costo_total = precio * cantidad

# Para imprimir los datos recopilados. 
print("\nDatos del producto:")
print("Nombre", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Costo tola del inventario", costo_total)
