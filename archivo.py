import csv 

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    """

    if not inventario:
        print("El inventario esta vacio, no se puede guardar")
        return
    
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:

            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print("Error: no tienes permiso para escribir el archivo")

    except Exception as e:
        print("Error al guardar:", e)


def cargar_csv(ruta):
    """
    Carga productos desde un archivo CSV.

    Retorna:
    lista de productos
    """

    inventario =[]
    errores = 0

    try:
        with open(ruta,"r", encoding= "utf-8") as archivo:

            reader = csv.reader(archivo)

            header = next(reader)

            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado invalido.")
                return []
            
            for fila in reader:

                if len(fila) != 3:
                    errores += 1
                    continue

                nombre, precio, cantidad = fila

            try:
                precio = float(precio)
                cantidad = int(cantidad)

                if precio < 0 or cantidad < 0:
                    raise ValueError
                
                inventario.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })

            except ValueError:
                errores += 1

        print(f"{errores}filas invalidad omitidas")

        return inventario
    except FileNotFoundError:
        print("Archivo no encontrado")

    except UnicodeDecodeError:
        print("Error de codificacion del archivo")

    except Exception as e:
        print("Error:", e)

    
    return []