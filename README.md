# Limpiador de Carpetas de Descargas [Windows]

Este es un proyecto en Python que te ayuda a organizar los archivos en tu carpeta de descargas según su tipo de archivo. Mueve los archivos a subcarpetas correspondientes basadas en sus extensiones de archivo. Personalmente lo utilizo para acomodar esta carpeta una vez por semana con el programador de tareas.

## Uso

1. Clona este repositorio en tu máquina local:

   `git clone https://github.com/valentinbellini/downloads-cleaner.git`

2. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

3. Abrir el archivo `categories.json` y ajustar las categorías de archivos según necesidades. Se puede agregar, modificar o eliminar categorías y extensiones de archivos según las preferencias. Si se sigue la estructura del json no debería haber problemas con agregar o quitar categorías.

4. Ejecutar el script `cleaner.py` desde tu terminal: `python cleaner.py`
   
Esto organizará automáticamente los archivos en tu carpeta de descargas según las categorías especificadas.

## Estructura y funcionalidad

El programa en la última versión, toma la estructura `categories.JSON` para clasificar los archivos según su extensión en diferentes carpetas. Por ejemplo, todos los archivos con extensiones ".jpg", ".jpeg", ".png", ".gif", ".svg" se moveran a una carpeta llamada 'Images' (El mismo script crea la carpeta si no existe). Además, genera un LOG que se guarda en el archivo `file_organizer-log` con el objetivo de tener un registro de lo que hace el programa ya que está diseñado para ejecutarse de manera automática.

Además, este organizador de carpetas puede utilizarse tanto para la carpeta "downloads" como para cualquier otra, solo se debe enviar la ruta de la carpeta deseada en el llamado a la función organize_files().

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



