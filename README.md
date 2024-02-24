# Limpiador de Carpetas de Descargas

Este es un proyecto en Python que te ayuda a organizar los archivos en tu carpeta de descargas según su tipo de archivo. Mueve los archivos a subcarpetas correspondientes basadas en sus extensiones de archivo.

## Uso

1. Clona este repositorio en tu máquina local:

`git clone https://github.com/valentinbellini/downloads-cleaner.git`

2. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

3. Abre el archivo `cleaner.py` y ajusta las categorías de archivos según tus necesidades. Puedes agregar, modificar o eliminar categorías y extensiones de archivos según tus preferencias.

4. Ejecuta el script `cleaner.py` desde tu terminal: `python cleaner.py`
   
Esto organizará automáticamente los archivos en tu carpeta de descargas según las categorías especificadas.

## Estructura y funcionalidad

Tenga en cuenta que el programa encuentra carpetas dentro del "folder" especificado en la función, no hará anda con ellas ya que no lo lee como archivo.
Esto quizas pueda tratarse en alguna versión futura si es que lo creo necesario o le veo utilidad.

Además, este organizador de carpetas puede utilizarse tanto para la carpeta "downloads" como para cualquiera, solo se debe enviar la ruta de la carpeta deseada en el llamado a la función organize_files().

## Automatizar tarea periodicamente

Puede utilizar el programador de tareas para automatizar la tarea de ejecutar el script según el período deseado. Dejo a continuación un ejemplo de como hacerlo en Windows.

1. Abrir el Programador de tareas: buscar "Programador de tareas" en el menú de inicio.

2. En el menú  "Acción" de la parte superior izquierda, seleccionar "Crear tarea básica".

3. Indicar nombre y descripción del evento

4. Indicar la frecuencia del evento ( En mi caso elegí semanalmente ) y configurar fechas. 

5. Cuando se llegue a la ventana "Seleccionar la acción", elegir "Iniciar un programa".

6. Seleccionar el script Python (cleaner.py) como el programa a ejecutar.

7. Completa el resto del asistente con cualquier otra configuración deseada y haz clic en "Finalizar" para guardar la tarea.


## Contribuir

Si deseas contribuir a este proyecto, ¡eres bienvenido! Siéntete libre de enviar pull requests con mejoras, sugerencias o correcciones de errores.



