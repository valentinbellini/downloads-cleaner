import os
import shutil
from pathlib import Path
import logging
import json

# Cargar las categorías desde el archivo JSON
with open("categories.json", "r") as file:
    categories = json.load(file)

# Ruta de la carpeta de descargas
download_folder = Path.home() / "Downloads"  

# Configuración básica del logging
logging.basicConfig(
    filename="file_organizer.log",  # Archivo donde se guardan los logs
    level=logging.INFO,  # Nivel mínimo de mensajes que se registran
    format="%(asctime)s - %(levelname)s - %(message)s"  # Formato de los mensajes
)



def organize_files(folder, categories):
    logging.info(f"Iniciando la organización de archivos en la carpeta: {folder}")
    
    for item in os.listdir(folder): # para cada archivo de la carpeta (folder)
        if os.path.isfile(folder / item): # Usamos os.path.isfile() para asegurarnos de que el elemento sea un archivo y no un subdirectorio.
            file_extension = Path(item).suffix.lower()  # Utilizamos el método suffix de la clase Path para obtener la extensión del archivo en minúsculas.
            logging.info(f"Procesando archivo: {item} (Extension: {file_extension})")
            
            destination_folder = None
            
            # Buscar categoría correspondiente
            for category, extensions in categories.items():
                if file_extension in extensions:  # Si la extensión del archivo coincide con alguna de las extensiones en una categoría, movemos el archivo a la carpeta de esa categoría.
                    destination_folder = folder / category
                    logging.info(f"Archivo '{item}' categorizado como '{category}'")
                    break
            else:
                # Si no coincide con ninguna categoría, mover a la carpeta 'Others'
                destination_folder = folder / "Others"
                logging.info(f"Archivo '{item}' no coincide con ninguna categoria. Moviendo a 'Others'")
                
            destination_folder.mkdir(exist_ok=True)  # Crear la carpeta si no existe
            destination_file = destination_folder / item
            if not destination_file.exists():  # Verificar si el archivo ya existe en la carpeta de destino
                try:
                    shutil.move(folder / item, destination_file)
                    logging.info(f"Archivo '{item}' movido a: {destination_folder}")
                except Exception as e:
                    logging.error(f"Error moviendo el archivo '{item}' a '{destination_folder}': {e}")
            else:
                logging.warning(f"El archivo '{item}' ya existe en la carpeta destino: {destination_folder}")
    
    logging.info("Organizacion de archivos completada.")

# Llamada a la función
logging.info("El script comenzo a ejecutarse.")  # Mensaje inicial
try:
    organize_files(download_folder, categories)
except Exception as e:
    logging.critical(f"Error critico en la ejecucion del script: {e}")
logging.info("El script finalizo correctamente.")  # Mensaje final

