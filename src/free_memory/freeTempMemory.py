# pip install humanize

import os
import shutil
from pathlib import Path
import humanize  # Para mostrar el tamaño en formato legible (MB, GB)
import logging


# Configuración básica del logging
logging.basicConfig(
    filename="free_memory.log",  # Archivo donde se guardan los logs
    level=logging.INFO,  # Nivel mínimo de mensajes que se registran
    format="%(asctime)s - %(levelname)s - %(message)s"  # Formato de los mensajes
)

# Configuración básica
temp_dirs = [
    Path.home() /  r"AppData/Local/Temp",  # Carpeta de archivos temporales en Windows
    Path.home() /  r".cache",             # Carpeta de caché en Linux/macOS
    Path.home() /  r"AppData\Local\Google\Chrome\User Data\Default\Cache",
    Path.home() /  r"AppData\Local\Microsoft\Edge\User Data\Default\Cache",
]

large_file_threshold = 500 * 1024 * 1024  # Archivos mayores a 500 MB

# Función para limpiar directorios de archivos temporales
def clean_temp_directories(temp_dirs):
    total_deleted = 0
    for temp_dir in temp_dirs:
        if temp_dir.exists():
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = Path(root) / file
                    try:
                        total_deleted += file_path.stat().st_size
                        os.remove(file_path)
                        logging.info(f"Removiendo archivo: {file_path}")
                    except Exception as e:
                        logging.error(f"Error al eliminar: {file_path}: {e}")
            logging.info(f"Limpiada la carpeta {temp_dir}")
    logging.info(f"Espacio liberado de archivos temporales: {humanize.naturalsize(total_deleted)}")
    

# Función para buscar archivos grandes
def find_large_files(folder, threshold):
    large_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = Path(root) / file
            try:
                if file_path.stat().st_size > threshold:
                    large_files.append(file_path)
            except Exception as e:
                print(f"Error al procesar {file_path}: {e}")
    return large_files

# Función para eliminar archivos seleccionados
def delete_files(file_list):
    for file_path in file_list:
        try:
            os.remove(file_path)
            print(f"Eliminado: {file_path}")
        except Exception as e:
            print(f"Error al eliminar {file_path}: {e}")

# Menú principal
def main():
    print("Herramienta para liberar espacio en disco")
    print("1. Limpiar archivos temporales")
    print("2. Buscar archivos grandes")
    print("3. Salir")
    choice = input("Elige una opción: ")
    
    if choice == "1":
        clean_temp_directories(temp_dirs)
    elif choice == "2":
        search_folder = input("Introduce la ruta para buscar archivos grandes (ej. C:\\): ")
        threshold = input(f"Tamaño mínimo del archivo para considerar (en MB, por defecto {large_file_threshold // (1024*1024)} MB): ")
        threshold = int(threshold) * 1024 * 1024 if threshold else large_file_threshold
        large_files = find_large_files(Path(search_folder), threshold)
        print(f"Archivos grandes encontrados ({len(large_files)}):")
        for file in large_files:
            print(f"{file} ({humanize.naturalsize(file.stat().st_size)})")
        
        confirm = input("¿Deseas eliminar estos archivos? (s/n): ").lower()
        if confirm == "s":
            delete_files(large_files)
        else:
            print("No se eliminó ningún archivo.")
    elif choice == "3":
        print("Saliendo...")
    else:
        print("Opción no válida.")

# if __name__ == "__main__":
#    main()


 # -------------------------------------------------------- #
clean_temp_directories(temp_dirs)