## Guia de Intalacion

para poder ver el proyecto primero deberas seguir estos pasos para descargar y ejecutar el programa en tu computadora.

### 1. primero debes tener python
como descargas python facil y sencillo aqui mismo te indico.

* vez a la página oficial: https://www.python.org

* Haz clic en Download Python.

* Descarga la versión recomendada.

* Ejecuta el instalador.

despues de intalar python, deberas abrir la terminal o tambien conocido como simbolo de sistema.

    python --version

si se instalo correctamente, te aparecera la version

    python 3.12.0

⚠️ Muy importante: si tienes windown lo abres con **windown + R**

y si tienes Linux lo abres con **Ctrl-Alt-T**

### 2. Descargar el repositorio

puedes hacerlo de dos formas como mas te convenga

#### La opcion mas facil

* Ve a la página del repositorio en GitHub.

* Haz clic en el botón verde Code.

* Haz clic en Download ZIP.

* Extrae el archivo ZIP en tu computadora.

#### La otra opcion seria *(usando git)*.

Si tienes Git instalado, abre la terminar y copias este url

    ...

#### Despues abres la carpeta del proyecto

    cd inventario.py

#### Ejecutas el programa 
para que se ejecute escribes:

    python inventario.py

el programa iniciara y te pedira ingresar:

* Nombre del producto
* Precio
* cantidad

### Ejemplo de como usarlo
Entrada:

    Ingrese el nombre del producto: Manzana
    Ingrese el precio del producto: 2000
    Ingrese la cantidad: 10


Salida:

    Producto: Manzana
    Precio: 2000
    Cantidad: 10
    Costo total del inventario: 20000
### Descripcion 

Este programa permite registrar la infomacion basica de un producto. El usuario debe ingresar el nombre del __producto, el precio y la cantidad__. 
El programa valida que el precio sea un numero valido y no negativo, si el producto es un valor negativo retorna al comienzo del bucle, y tambien valida que la cantidad sea un numero entero no negativo. Finalmente se calcula el costo total del inventario del producto.


### Funcionamiento 

##### 1. El programa solicita al usuario el *nombre del producto. 

##### 2. Luego pide el precio del producto y verifica que: 

* Sea un numero. 
* No sea negativo.

##### 3. Despues solicita la cantidad del producto y valida que: 

* Sea un numero entero. 
* No sea negativo. 
##### 4. cuando los datos sean correctos, el programa calcula el costo total del inventario multiplicando el precio por la cantidad. 

##### 5. Finalmente muestra en pantalla los datos del producto y el costo final. 

------------------- 

### Resultado Al finalizar la ejecucion, el programa muestra en pantalla la informacion ingresada y el calculo realizado. 

----------------------- 

### Programa 

PYTHON
