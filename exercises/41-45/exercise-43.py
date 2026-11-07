"""
CALCULAR EL FACTORIAL DE UN NÚMERO N -> CALCULATE THE FACTORIAL OF A NUMBER N
"""

try:
    user_input = input("Ingresa un número para calcular su factorial -> Enter a number to calculate its factorial: ").strip()
    number = int(user_input) if user_input else 5

    if number < 0:
        print("El factorial no está definido para números negativos -> Factorial is not defined for negative numbers")
    else:
        factorial = 1
        counter = 1

        # Cálculo de factorial acumulativo -> Cumulative factorial calculation
        while counter <= number:
            factorial *= counter
            counter += 1

        print(f"El factorial de {number}! es -> The factorial of {number}! is: {factorial}")

except ValueError:
    print("Error: Ingresa un número entero no negativo válido -> Error: Please enter a valid non-negative integer")
