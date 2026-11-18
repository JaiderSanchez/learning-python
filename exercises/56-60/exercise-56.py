"""
LISTAR N NÚMEROS Y CALCULAR EL CUADRADO DE CADA UNO UTILIZANDO FOR -> LIST N NUMBERS AND CALCULATE THE SQUARE OF EACH USING FOR
"""

try:
    # Solicitar límite superior o usar 10 por defecto -> Request upper limit or use 10 by default
    user_input: str = input("¿Hasta qué número deseas calcular cuadrados? (Enter para 10) -> Up to which number? (Enter for 10): ").strip()
    limit: int = int(user_input) if user_input else 10

    if limit < 1:
        print("Por favor ingresa un número mayor o igual a 1 -> Please enter a number greater than or equal to 1.")

    else:
        print(f"\n--- Cuadrados del 1 al {limit} -> Squares from 1 to {limit} ---")

        for number in range(1, limit + 1):
            square: int = number ** 2
            print(f"El cuadrado de {number} es {square} -> The square of {number} is {square}")

except ValueError:
    print("Error: Debes ingresar un número entero válido -> Error: You must enter a valid integer.")
