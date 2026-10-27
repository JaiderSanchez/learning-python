"""
ORDENAR UNA LISTA DE NÚMEROS DE MENOR A MAYOR -> SORT A LIST OF NUMBERS FROM SMALLEST TO LARGEST
"""

raw_input = input("Ingresa números separados por espacios (o presiona Enter para usar la lista predeterminada) -> Enter numbers separated by spaces (or press Enter for default list): ").strip()

try:
    if raw_input:
        # Parseo de lista usando list comprehension -> List parsing using list comprehension
        numbers_list: list[float] = [float(num) for num in raw_input.split()]
    else:
        numbers_list = [7, 2, 5, 1, 9, 15, 20, 26, 126, 40, 512, 200, 157, 987, 777]

    print(f"Lista original -> Original list: {numbers_list}")

    # Ordenamiento in-place con .sort() -> In-place sorting with .sort()
    numbers_list.sort()

    print(f"Lista ordenada de menor a mayor -> Sorted list from smallest to largest: {numbers_list}")

except ValueError:
    print("Error: Asegúrate de ingresar únicamente números separados por espacios -> Error: Make sure to enter numbers separated by spaces only")
    