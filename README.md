# Multi-Tools [Windows]

En este proyecto se concentran varias herramientas que utilizo personalmente en el día a día para ayudarme con mis tareas. La idea es generar un paquete de herramientas para automatizar y optimizar mi tiempo. El proyecto se encuentra en desarrollo por lo que algunas funcionalidades pueden no estar correctamente implementadas.

## Uso

1. Clona este repositorio en tu máquina local:

   `git clone https://github.com/valentinbellini/downloads-cleaner.git`

2. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

3. Personalmente me gusta crear entornos virtuales cuando trabajo con estos proyectos para instalar todas las dependencias necesarias del proyecto. Puedes instalar todas las librerías necesarias que se encuentran en `requirements.txt` con el comando:
``` bash
pip install -r requirements.txt
```
4. Ya instaladas las librerías puede ejecutar el código de la herramienta que necesites. En un futuro se plantea la implementación de un menú interactivo en una interfaz gráfica.


## Estructura y funcionalidad

Dentro de la carpeta `src` se pueden encontrar las carpetas con los códigos para cada herramienta. Actualmente las herramientas implementadas son las siguientes:

### [Folder Cleaner](src/folder_cleaner)
El programa en la última versión, toma la estructura `categories.JSON` para clasificar los archivos según su extensión en diferentes carpetas. Por ejemplo, todos los archivos con extensiones ".jpg", ".jpeg", ".png", ".gif", ".svg" se moveran a una carpeta llamada `Images` (El mismo script crea la carpeta si no existe). Además, genera un LOG que se guarda en el archivo `file_organizer-log` con el objetivo de tener un registro de lo que hace el programa ya que está diseñado para ejecutarse de manera automática.

Además, este organizador de carpetas puede utilizarse tanto para la carpeta "downloads" como para cualquier otra, solo se debe enviar la ruta de la carpeta deseada en el llamado a la función organize_files().

Para automatizar esta tarea en Windows puede verse la sección correspondiente más abajo en este documento.

### [Free memory](src/free_memory)

El script dentro de esta carpeta tiene el objetivo de eliminar archivos temporales de la PC para liberar espacio. Puede ejecutarse periodicamente para tener más espacio de almacenamiento. Dentro del script hay una lista llamada `temp_dirs` donde pueden poner las rutas a las carpetas que deseas eliminar los archivos temporales o cache.

Este script también cuenta con un log para ir rastreando y guardando un registro de los archivos que fueron eliminados así como también si hubo algun error en la ejecución.

### [Encrypt Files](src/encrypt_files)

El script `encrypt.py` contiene varias funciones.
- `generate_and_save_key` - Función para generar y guardar una clave única para cada archivo en la carpeta Keys
- `load_key` - Función para cargar la clave correspondiente a un archivo
- `encrypt_file` - Función para encriptar el archivo
- `decrypt_file` - Función para desencriptar el archivo

Ejemplo de ejecución:

``` python
archivo = "C:/Users/valen/Downloads/TEMPORAL.pdf"
archivo_encrypted = "C:/Users/valen/Downloads/TEMPORAL.encrypted"

encrypt_file(archivo)
decrypt_file(archivo_encrypted)
```

Nota: Tener en cuenta que si se pierde el archivo `.key`, no será posible volver a desencriptar el archivo.

### [PDF Password](src/pdf_password)

El script idealmente puede ponerle contraseña a varios tipos de archivos aunque personalmente lo utilizo solo para formato PDF. En la última versión cuenta con un menú en consola cuando se ejecuta el script, que solicita enviar la ruta de acceso al archivo al cuál se desea proteger y luego pide la contraseña deseada para el mismo. 

Además, se implementó una función para quitar contraseña al PDF en caso de que ya no necesitemos que se encuentre protegido.

## Automatizar tarea periodicamente

Puede utilizar el programador de tareas para automatizar la tarea de ejecutar el script según el período deseado. Dejo a continuación un ejemplo de como hacerlo en Windows.

1. Abrir el Programador de tareas: buscar "Programador de tareas" en el menú de inicio.

2. En el menú  "Acción" de la parte superior izquierda, seleccionar "Crear tarea básica".

3. Indicar nombre y descripción del evento

4. Indicar la frecuencia del evento ( En mi caso elegí semanalmente ) y configurar fechas. 

5. Cuando se llegue a la ventana "Seleccionar la acción", elegir "Iniciar un programa".

6. Seleccionar el script Python (cleaner.py) como el programa a ejecutar.

7. Completar el resto del asistente con cualquier otra configuración deseada y hacer clic en "Finalizar" para guardar la tarea.


## Contribuir

Si deseas contribuir a este proyecto, sentite libre de enviar pull requests con mejoras, sugerencias o correcciones de errores.


