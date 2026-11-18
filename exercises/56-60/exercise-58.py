"""
MULTIPLICAR TODOS LOS ELEMENTOS DE UNA LISTA POR UN FACTOR -> MULTIPLY ALL ELEMENTS OF A LIST BY A FACTOR
"""

numbers_list: list[int] = [3, 6, 9, 12]

try:
    # Solicitar multiplicador o usar 2 por defecto -> Request multiplier or use 2 by default
    user_input: str = input("Ingresa el número multiplicador (Enter para 2) -> Enter multiplier number (Enter for 2): ").strip()
    multiplier: int = int(user_input) if user_input else 2

    print(f"\nLista original -> Original list: {numbers_list}")
    print(f"--- Resultados multiplicados por {multiplier} -> Results multiplied by {multiplier} ---")

    # Iteración directa sobre los elementos -> Direct iteration over elements
    for element in numbers_list:
        print(f"{element} x {multiplier} = {element * multiplier}")

except ValueError:
    print("Error: Debes ingresar un número entero válido -> Error: You must enter a valid integer.")
