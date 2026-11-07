"""
IMPRIMIR LA TABLA DE MULTIPLICAR DE UN NÚMERO -> PRINT THE MULTIPLICATION TABLE OF A NUMBER
"""

try:
    user_input = input("Ingresa un número para ver su tabla de multiplicar -> Enter a number to view its multiplication table: ").strip()
    number = int(user_input) if user_input else 7

    multiplier = 1

    print(f"\n--- Tabla del {number} -> Table of {number} ---")

    # Bucle while para generar la tabla del 1 al 10 -> While loop to generate table from 1 to 10
    while multiplier <= 10:
        product = number * multiplier
        print(f"{number} x {multiplier} = {product}")
        multiplier += 1

except ValueError:
    print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer")
