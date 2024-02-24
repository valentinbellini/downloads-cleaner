import os
import shutil
from pathlib import Path

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".epub",".xlsx",".pptx",".csv"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Matlab": [".m",".slx"],
    "Python": [".py",".ipynb"],
    "Others": []  # Aquí se colocarán los archivos que no pertenecen a ninguna categoría específica
}

download_folder = Path.home() / "Downloads"  # Ruta de la carpeta de descargas

def organize_files(folder, categories):
    for item in os.listdir(folder): # para cada archivo de la carpeta (folder)
        if os.path.isfile(folder / item): # Usamos os.path.isfile() para asegurarnos de que el elemento sea un archivo y no un subdirectorio.
            file_extension = Path(item).suffix.lower()  # Utilizamos el método suffix de la clase Path para obtener la extensión del archivo en minúsculas.
            destination_folder = None
            # Iteramos sobre el diccionario categories, que contiene las categorías como claves 
            # y las extensiones de archivo correspondientes como valores. 
            for category, extensions in categories.items():
                if file_extension in extensions:  # Si la extensión del archivo coincide con alguna de las extensiones en una categoría, movemos el archivo a la carpeta de esa categoría.
                    destination_folder = folder / category
                    break
            else:
                # Si no coincide con ninguna categoría, mover a la carpeta 'Others'
                destination_folder = folder / "Others"
                
            destination_folder.mkdir(exist_ok=True)  # Crear la carpeta si no existe
            destination_file = destination_folder / item
            if not destination_file.exists():  # Verificar si el archivo ya existe en la carpeta de destino
                shutil.move(folder / item, destination_file)

            
organize_files(download_folder, categories)