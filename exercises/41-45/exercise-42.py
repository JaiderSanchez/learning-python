"""
SUMAR NÚMEROS DESDE 1 HASTA N -> SUM NUMBERS FROM 1 TO N
"""

try:
    user_input = input("Ingresa un número entero N por favor -> Please enter an integer N: ").strip()
    target_number = int(user_input) if user_input else 10

    if target_number < 1:
        print("El número debe ser mayor o igual a 1 -> Number must be greater than or equal to 1")
    else:
        total_sum = 0
        current = 1

        # Acumulador con bucle while -> Accumulator using while loop
        while current <= target_number:
            total_sum += current
            current += 1

        print(f"La suma de los números desde 1 hasta {target_number} es -> The sum of numbers from 1 to {target_number} is: {total_sum}")

except ValueError:
    print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer")
