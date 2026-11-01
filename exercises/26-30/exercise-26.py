"""
INTERCAMBIAR LOS VALORES DE DOS VARIABLES CON ASIGNACIÓN MÚLTIPLE -> SWAP THE VALUES OF TWO VARIABLES USING MULTIPLE ASSIGNMENT
"""

# Entrada opcional por consola o valores por defecto -> Optional console input or default values
input_a = input("Ingresa el primer valor (o Enter para usar el predeterminado) -> Enter first value (or Enter for default): ").strip()
input_b = input("Ingresa el segundo valor (o Enter para usar el predeterminado) -> Enter second value (or Enter for default): ").strip()

var_a: str | int = input_a if input_a else 26
var_b: str | int = input_b if input_b else 23

print(f"Valores originales -> Original values: var_a = {var_a}, var_b = {var_b}")

# Intercambio de variables mediante desempaquetado de tuplas -> Variable swap using tuple unpacking
var_a, var_b = var_b, var_a

print(f"Valores intercambiados -> Swapped values: var_a = {var_a}, var_b = {var_b}")
