# 04-packages-and-init.py
# Usamos nuestra caja de herramientas (paquete math_box) -> Using our toolbox (math_box package)

# Forma 1: Sacar una herramienta de una bolsita específica -> Way 1: Take a tool from a specific bag
from math_box.suma_resta import sumar

# Forma 2: Sacar herramientas directo de la caja gracias a __init__.py -> Way 2: Take tools directly from the box thanks to __init__.py
from math_box import restar, multiplicar, dividir

print("--- Probando nuestra caja de herramientas -> Testing our toolbox ---")
print(f"Suma (5 + 3) -> Addition (5 + 3): {sumar(5, 3)}")
print(f"Resta (10 - 4) -> Subtraction (10 - 4): {restar(10, 4)}")
print(f"Multiplicación (6 * 2) -> Multiplication (6 * 2): {multiplicar(6, 2)}")
print(f"División (2048 / 1024) -> (2048 / 1024): {dividir(2048, 1024)}")
