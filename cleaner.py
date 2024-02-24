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
    count = 0
    for item in os.listdir(folder): # para cada archivo de la carpeta (folder)
        if os.path.isfile(folder / item): # Usamos os.path.isfile() para asegurarnos de que el elemento sea un archivo y no un subdirectorio.
            file_extension = Path(item).suffix.lower()  # Utilizamos el método suffix de la clase Path para obtener la extensión del archivo en minúsculas.
            count += 1
            print(file_extension)
        else: count +=1
    print(count)

organize_files(download_folder, categories)