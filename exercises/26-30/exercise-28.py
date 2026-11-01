"""
EXTRAER UN ELEMENTO ESPECÍFICO DE UNA TUPLA -> EXTRACT A SPECIFIC ELEMENT FROM A TUPLE
"""

numbers_tuple: tuple[int, ...] = (10, 20, 30, 40, 50)

print(f"Tupla disponible -> Available tuple: {numbers_tuple}")

try:
    user_input = input("Ingresa el índice a extraer (0 a 4) [Enter para usar índice 1] -> Enter index to extract (0 to 4) [Enter for index 1]: ").strip()
    index = int(user_input) if user_input else 1

    # Extracción por índice -> Extraction by index
    selected_element = numbers_tuple[index]
    print(f"El elemento en el índice {index} es -> Element at index {index} is: {selected_element}")

except IndexError:
    print("Error: El índice ingresado está fuera del rango de la tupla -> Error: Index out of tuple range")
except ValueError:
    print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer")
    