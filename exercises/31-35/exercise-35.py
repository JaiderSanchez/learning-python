"""
COMPROBAR SI UN NÚMERO ESTÁ EN EL RANGO DE 1 A 100 -> CHECK IF A NUMBER IS WITHIN THE RANGE OF 1 TO 100
"""

try:
    user_input = input("Introduce un número -> Enter a number: ").strip()
    number = int(user_input) if user_input else 50

    # Comparación encadenada idiomática de Python (1 <= number <= 100) -> Idiomatic Python chained comparison (1 <= number <= 100)
    if 1 <= number <= 100:
        print(f"El número {number} está en el rango de 1 a 100 -> The number {number} is within the range of 1 to 100")
    else:
        print(f"El número {number} NO está en el rango de 1 a 100 -> The number {number} is NOT within the range of 1 to 100")

except ValueError:
    print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer")
