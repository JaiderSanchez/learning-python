"""
CREAR UNA FUNCIÓN PARA SUMAR DOS NÚMEROS -> CREATE A FUNCTION TO ADD TWO NUMBERS
"""

def add_numbers(number_1: float, number_2: float) -> float:
    """Retorna la suma de dos números -> Returns the sum of two numbers."""
    return number_1 + number_2


try:
    # Capturar números del usuario o usar 5 y 10 por defecto -> Capture user numbers or use 5 and 10 by default
    input_1: str = input("Ingresa el primer número (Enter para 5) -> Enter first number (Enter for 5): ").strip()
    input_2: str = input("Ingresa el segundo número (Enter para 10) -> Enter second number (Enter for 10): ").strip()

    num_1: float = float(input_1) if input_1 else 5.0
    num_2: float = float(input_2) if input_2 else 10.0

    result: float = add_numbers(num_1, num_2)
    print(f"La suma de {num_1} + {num_2} es -> The sum of {num_1} + {num_2} is: {result}")

except ValueError:
    print("Error: Ingresa únicamente valores numéricos válidos -> Error: Please enter valid numeric values only.")
    