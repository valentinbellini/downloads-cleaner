from PyPDF2 import PdfReader, PdfWriter

# Función para proteger un archivo PDF con una contraseña
def protect_pdf(input_pdf, output_pdf, password):
    """
    Aplica una contraseña a un archivo PDF para proteger su contenido.
    """
    pdf_writer = PdfWriter()  # Crea un escritor para manejar el PDF
    pdf_reader = PdfReader(input_pdf)  # Lee el archivo PDF de entrada

    # Añade todas las páginas del archivo original al nuevo archivo
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    # Aplica la contraseña al PDF
    pdf_writer.encrypt(password)

    # Guarda el archivo PDF protegido con contraseña
    with open(output_pdf, "wb") as file:
        pdf_writer.write(file)
    print(f"El archivo '{output_pdf}' ha sido protegido con contraseña.")

# Función para verificar si un archivo PDF ya está protegido
def check_protection(input_pdf):
    """
    Verifica si un archivo PDF tiene protección con contraseña.
    """
    pdf_reader = PdfReader(input_pdf)  # Lee el archivo PDF
    if pdf_reader.is_encrypted:
        print(f"El archivo '{input_pdf}' ya está protegido.")
    else:
        print(f"El archivo '{input_pdf}' no tiene protección.")

# Programa principal
if __name__ == "__main__":
    choice = input("¿Qué deseas hacer? (1: Proteger PDF, 2: Verificar protección): ")
    if choice == "1":
        input_pdf = input("Introduce la ruta completa del archivo PDF de entrada: ")
        output_pdf = input("Introduce la ruta completa del archivo PDF de salida (protegido): ")
        password = input("Introduce la contraseña: ")
        protect_pdf(input_pdf, output_pdf, password)
    elif choice == "2":
        input_pdf = input("Introduce la ruta completa del archivo PDF: ")
        check_protection(input_pdf)
    else:
        print("Opción no válida.")
