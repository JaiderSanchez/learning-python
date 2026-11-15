# 05-sys-path-and-builtins.py
# Explorando cómo Python busca módulos y usa herramientas internas -> Exploring how Python finds modules and uses built-in tools

import sys
import os

# 1. Ver en qué carpeta de la computadora estoy actualmente ->See which folder on the computer I am currently in
current_folder: str = os.getcwd()
print(f"Carpeta actual -> Current folder:\n{current_folder}\n")

# 2. Ver la versión exacta de Python que estoy usando -> See the exact version of Python I am using
print(f"Versión de Python -> Python version:\n{sys.version.split()[0]}\n")

# 3. Ver el "mapa del tesoro" (sys.path) donde Python busca los módulos -> View the "treasure map" (sys.path) where Python searches for modules
print("Carpetas donde Python busca mis imports -> Folders where Python looks for my imports")
search_paths: list[str] = sys.path

for index, folder in enumerate(search_paths, start=1):
    print(f"{index}. {folder}")

# 4. Ver algunos módulos que ya vienen pegados dentro de Python -> View some modules already built inside Python
built_in_tools = sys.builtin_module_names
print(f"\nPrimeros 8 módulos internos de Python -> First 8 built-in Python modules:")
print(built_in_tools[:8])
