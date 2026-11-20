# 02-reading-files.py
# Leer archivos de texto de diferentes formas y manejar errores -> Read text files in different ways and handle errors

file_name: str = "notas_python.txt"

try:
    # 1. Leer todo el contenido de una sola vez con .read() -> Read the entire content at once using .read()
    print("--- 1. Lectura completa (.read) -> Full read (.read) ---")
    with open(file_name, mode="r", encoding="utf-8") as file:
        full_content: str = file.read()
        print(full_content)

    # 2. Leer línea por línea como una lista con .readlines() -> Read line by line as a list using .readlines()
    print("--- 2. Lectura como lista (.readlines) -> Read as a list (.readlines) ---")
    with open(file_name, mode="r", encoding="utf-8") as file:
        lines_list: list[str] = file.readlines()
        print(f"Total de líneas -> Total lines: {len(lines_list)}")
        print(lines_list)

    # 3. Iterar línea por línea (la forma más eficiente en memoria) -> Iterate line by line (most memory-efficient way)
    print("\n--- 3. Lectura renglón por renglón (for loop) -> Line-by-line reading (for loop) ---")
    with open(file_name, mode="r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            # .strip() elimina el salto de línea invisible (\n) al final -> .strip() removes the invisible newline (\n) at the end
            print(f"Línea {line_number} -> Line {line_number}: {line.strip()}")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{file_name}'. Ejecuta primero 01-writing-files.py -> Error: File '{file_name}' not found. Run 01-writing-files.py first.")
