def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario.

    Parámetros:
    inventario (list): lista de productos
    nombre (str): nombre del producto
    precio (float): precio del producto
    cantidad (int): cantidad disponible

    Retorna:
    None
    """

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """

    if not inventario:
        print("Invertario vacio")
        return
    
    for p in inventario:
        print(f"producto: {p['nombre']} | Precio: {p['precio']} | cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.

    Retorna:
    dict si lo encuentra
    None si no existe
    """

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
        
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio o cantidad de un producto.
    """

    producto = buscar_producto(inventario, nombre)

    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio

        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        
        return True
    return False

def eliminar_producto(inventario, nombre):
    """
    Eliminar un producto del inventario
    """
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        return True
    
    return False


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Retorna un diccionario con:
    unidades_totales
    valor_total
    producto_mas_caro
    producto_mayor_stock
    """

    if not inventario:
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }