from cryptography.fernet import Fernet
from pathlib import Path
import os


# Ruta donde se almacenarán las claves
KEYS_DIR = Path(__file__).parent / "keys"
KEYS_DIR.mkdir(exist_ok=True)  # Crear la carpeta si no existe


# Función para generar y guardar una clave única para cada archivo
def generate_and_save_key(file_name):
    key = Fernet.generate_key()  # Generar una clave única
    key_file_path = KEYS_DIR / f"{file_name}.key"  # Guardar clave en src/encrypt_files/keys/<nombre_archivo>.key
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)  # Guardar la clave en un archivo
    return key

# Función para cargar la clave correspondiente a un archivo
def load_key(file_name):
    key_file_path = KEYS_DIR / f"{file_name}.key"  # Buscar clave en src/encrypt_files/keys/<nombre_archivo>.key
    if not key_file_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de clave: {key_file_path}")
    with open(key_file_path, "rb") as key_file:
        return key_file.read()

# Función para encriptar un archivo
def encrypt_file(file_path):
    file_path = Path(file_path)  # Convertir a objeto Path
    if not file_path.exists():
        print(f"El archivo {file_path} no existe.")
        return

    # Generar y guardar clave
    key = generate_and_save_key(file_path.stem)  # Guardar clave con nombre basado en el archivo
    fernet = Fernet(key)

    # Leer y encriptar el contenido del archivo
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)

    # Guardar el archivo encriptado
    encrypted_file_path = file_path.with_suffix(".encrypted")
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"Archivo encriptado guardado como: {encrypted_file_path}")
    print(f"Clave guardada en: {file_path.stem}.key")

# Función para desencriptar un archivo
def decrypt_file(encrypted_file_path):
    encrypted_file_path = Path(encrypted_file_path)  # Convertir a objeto Path
    if not encrypted_file_path.exists():
        print(f"El archivo {encrypted_file_path} no existe.")
        return

    # Cargar clave correspondiente
    key = load_key(encrypted_file_path.stem)  # Asumimos que <archivo>.encrypted usa <archivo>.key
    fernet = Fernet(key)

    # Leer y desencriptar el contenido del archivo
    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)

    # Guardar el archivo desencriptado
    original_file_path = encrypted_file_path.with_suffix(".decrypted")
    with open(original_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Archivo desencriptado guardado como: {original_file_path}")


print("Ruta actual:", os.getcwd())

archivo = "C:/Users/valen/Downloads/TEMPORAL.pdf"
archivo_encrypted = "C:/Users/valen/Downloads/TEMPORAL.encrypted"

encrypt_file(archivo)
decrypt_file(archivo_encrypted)

