"""
DETERMINAR SI UN NÚMERO ES DIVISIBLE ENTRE 5 Y 7 -> DETERMINE IF A NUMBER IS DIVISIBLE BY BOTH 5 AND 7
"""

try:
    user_input = input("Introduce un número entero -> Enter an integer: ").strip()
    number = int(user_input) if user_input else 35

    # Evaluación de divisibilidad simultánea usando el operador módulo (%) y 'and' -> Simultaneous divisibility evaluation using modulo operator (%) and 'and'
    if number % 5 == 0 and number % 7 == 0:
        print(f"El número {number} es divisible entre 5 y 7 -> The number {number} is divisible by 5 and 7")
    else:
        print(f"El número {number} NO es divisible entre 5 y 7 -> The number {number} is NOT divisible by 5 and 7")

except ValueError:
    print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer")
