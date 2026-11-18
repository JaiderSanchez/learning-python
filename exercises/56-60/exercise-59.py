"""
PEDIR AL USUARIO UN NÚMERO E IMPRIMIR SU TABLA DE MULTIPLICAR -> ASK USER FOR A NUMBER AND PRINT ITS MULTIPLICATION TABLE
"""

try:
    # Solicitar base de la tabla o usar 5 por defecto -> Request table base or use 5 by default
    num_input: str = input("Ingresa un número para ver su tabla (Enter para 5) -> Enter a number for its table (Enter for 5): ").strip()
    number: int = int(num_input) if num_input else 5

    # Solicitar límite de la tabla o usar 10 por defecto -> Request table limit or use 10 by default
    limit_input: str = input("¿Hasta qué número multiplicar? (Enter para 10) -> Multiply up to which number? (Enter for 10): ").strip()
    limit: int = int(limit_input) if limit_input else 10

    print(f"\n--- Tabla de multiplicar del {number} -> Multiplication table of {number} ---")
    for factor in range(1, limit + 1):
        result: int = number * factor
        print(f"{number} x {factor} = {result}")

except ValueError:
    print("Error: Ingresa únicamente números enteros válidos -> Error: Please enter valid integers only.")
