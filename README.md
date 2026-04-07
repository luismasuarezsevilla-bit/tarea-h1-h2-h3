# 📦 Sistema de Gestión de Inventario

Aplicación en Python para gestionar inventarios de productos con funcionalidades de almacenamiento en CSV.

---

## 🐍 Instalación de Python

### Windows
1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. Ejecuta el instalador y **marca la casilla "Add Python to PATH"**
3. Haz clic en "Install Now"
4. Verifica la instalación abriendo una terminal y escribiendo:
   ```bash
   python --version
   ```

### macOS / Linux
Abre una terminal y ejecuta:
```bash
# macOS (con Homebrew)
brew install python3

# Linux (Debian/Ubuntu)
sudo apt-get install python3
```

Verifica con:
```bash
python3 --version
```

---

## 📋 Descripción de Archivos

### **app.py** - Aplicación Principal
Interfaz de menú interactivo que gestiona el inventario con las siguientes opciones:
- ✅ Agregar productos (con validación de nombre, precio y cantidad)
- ✅ Mostrar inventario completo
- ✅ Buscar productos por nombre
- ✅ Actualizar precio y cantidad de productos
- ✅ Eliminar productos
- ✅ Ver estadísticas del inventario
- ✅ Guardar/Cargar inventarios desde archivos CSV

### **archivo.py** - Gestión de Archivos CSV
Módulo para importar y exportar datos:
- `guardar_csv()`: Guarda el inventario en un archivo CSV con encabezados
- `cargar_csv()`: Carga productos desde un CSV con validación de datos
- Maneja errores de permisos, codificación y formato inválido

### **servicios.py** - Funciones del Negocio
Contiene las operaciones principales del inventario:
- `agregar_producto()`: Añade nuevos productos
- `mostrar_inventario()`: Muestra todos los productos en formato tabla
- `buscar_producto()`: Busca por nombre (case-insensitive)
- `actualizar_producto()`: Modifica precio y/o cantidad
- `eliminar_producto()`: Remueve productos
- `calcular_estadisticas()`: Genera reportes de valor total y productos destacados

---

## � Diagrama de Flujo

```mermaid
graph TD
    A["📱 <b>app.py</b><br/>Menú Principal"] -->|loop| B{"¿Qué opción?"}
    
    B -->|1| C["Agregar Producto"]
    B -->|2| D["Mostrar Inventario"]
    B -->|3| E["Buscar Producto"]
    B -->|4| F["Actualizar Producto"]
    B -->|5| G["Eliminar Producto"]
    B -->|6| H["Estadísticas"]
    B -->|7| I["Guardar CSV"]
    B -->|8| J["Cargar CSV"]
    B -->|9| K["Salir"]
    
    C -->|llama| L["servicios.py<br/>agregar_producto"]
    D -->|llama| M["servicios.py<br/>mostrar_inventario"]
    E -->|llama| N["servicios.py<br/>buscar_producto"]
    F -->|llama| O["servicios.py<br/>actualizar_producto"]
    G -->|llama| P["servicios.py<br/>eliminar_producto"]
    H -->|llama| Q["servicios.py<br/>calcular_estadisticas"]
    I -->|llama| R["archivo.py<br/>guardar_csv"]
    J -->|llama| S["archivo.py<br/>cargar_csv"]
    
    L --> T["Base de Datos<br/>inventario[]"]
    M --> T
    N --> T
    O --> T
    P --> T
    Q --> T
    R --> U["📄 Archivo CSV"]
    S --> U
    
    L -->|retorna| A
    M -->|retorna| A
    N -->|retorna| A
    O -->|retorna| A
    P -->|retorna| A
    Q -->|retorna| A
    R -->|retorna| A
    S -->|actualiza| T
    S -->|retorna| A
    
    K --> V["Fin"]
    
    style A fill:#4CAF50,color:#fff,stroke:#2E7D32,stroke-width:3px
    style L fill:#2196F3,color:#fff,stroke:#1565C0,stroke-width:2px
    style M fill:#2196F3,color:#fff,stroke:#1565C0,stroke-width:2px
    style N fill:#2196F3,color:#fff,stroke:#1565C0,stroke-width:2px
    style O fill:#2196F3,color:#fff,stroke:#1565C0,stroke-width:2px
    style P fill:#2196F3,color:#fff,stroke:#1565C0,stroke-width:2px
    style Q fill:#2196F3,color:#fff,stroke:#1565C0,stroke-width:2px
    style R fill:#FF9800,color:#fff,stroke:#E65100,stroke-width:2px
    style S fill:#FF9800,color:#fff,stroke:#E65100,stroke-width:2px
    style T fill:#9C27B0,color:#fff,stroke:#6A1B9A,stroke-width:2px
    style U fill:#9C27B0,color:#fff,stroke:#6A1B9A,stroke-width:2px
    style V fill:#f44336,color:#fff,stroke:#C62828,stroke-width:2px
    style B fill:#FFC107,color:#000,stroke:#F57F17,stroke-width:2px
```

---

## �🚀 Cómo Usar

1. Abre una terminal en la carpeta del proyecto
2. Ejecuta:
   ```bash
   python app.py
   ```
3. Selecciona una opción del menú (1-9)
4. Sigue las instrucciones en pantalla

---

## 📝 Notas
- Los productos se validan antes de ser agregados
- Los archivos CSV deben tener el formato: `nombre,precio,cantidad`
- Las operaciones incluyen manejo de errores para entradas inválidas
