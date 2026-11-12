"""
CONTAR CUÁNTOS DÍGITOS TIENE UN NÚMERO INGRESADO POR EL USUARIO -> COUNT HOW MANY DIGITS A USER-ENTERED NUMBER HAS
"""

try:
    user_input = input("Ingresa un número entero por favor -> Please enter an integer: ").strip()
    number: int = int(user_input) if user_input else 12345

    # Usamos abs() para evitar bucles infinitos con números negativos -> Use abs() to prevent infinite loops with negative numbers
    temp_number: int = abs(number)
    digit_count: int = 0

    # Caso especial para el número 0 -> Special edge case for number 0
    if temp_number == 0:
        digit_count = 1
    else:
        # División entera sucesiva entre 10 -> Successive integer division by 10
        while temp_number != 0:
            temp_number //= 10
            digit_count += 1

    print(f"El número {number} tiene {digit_count} dígito(s) -> The number {number} has {digit_count} digit(s).")

except ValueError:
    print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer")
