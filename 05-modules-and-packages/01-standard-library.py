# 01-standard-library.py

# El módulo estándar de Python incluye herramientas preinstaladas para tareas comunes -> Python's standard library includes pre-installed tools for common tasks
# Se importan usando la palabra clave 'import' -> They are imported using the 'import' keyword

import math
import random as rnd
from datetime import datetime

# 1. Uso del módulo math para operaciones matemáticas avanzadas -> 1. Using the math module for advanced math operations
radius: float = 5.0
area: float = math.pi * math.pow(radius, 2)
print(f"Área del círculo (r={radius}) -> Circle area (r={radius}): {area:.2f}")

# 2. Uso de alias con random (import random as rnd) -> 2. Using aliases with random (import random as rnd)
random_score: int = rnd.randint(1, 100)
print(f"Puntuación aleatoria obtenida -> Random score obtained: {random_score}")

# 3. Importación específica con 'from ... import ...' -> 3. Specific import using 'from ... import ...'
current_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Fecha y hora actual -> Current date and time: {current_time}")
