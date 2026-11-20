# 01-writing-files.py
# Crear archivos de texto y agregar contenido de forma segura -> Create text files and append content safely

# 1. Crear y escribir un archivo nuevo usando modo "w (Write / Escribir)" (sobrescribe si ya existe) -> Create and write a new file using "w" mode (overwrites if it already exists)
file_name: str = "notas_python.txt"

with open(file_name, mode="w", encoding="utf-8") as file:
    file.write("Hola desde Python 3.12 -> Hello from Python 3.12\n")
    file.write("Esta es mi primera nota guardada en disco -> This is my first note saved on disk\n")

print(f"Archivo '{file_name}' creado con éxito -> File '{file_name}' created successfully.")

# 2. Agregar más líneas al final sin borrar lo anterior usando modo "a (Append / Agregar)" -> Append more lines at the end without deleting previous content using "a" mode
with open(file_name, mode="a", encoding="utf-8") as file:
    file.write("Línea agregada después sin borrar nada -> Line appended later without deleting anything\n")

print("Nueva línea agregada correctamente -> New line appended successfully.")
