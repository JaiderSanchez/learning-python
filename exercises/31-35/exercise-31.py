"""
PEDIR UN NÚMERO Y VERIFICAR SI ES POSITIVO, NEGATIVO O CERO -> ASK FOR A NUMBER AND CHECK IF IT IS POSITIVE, NEGATIVE, OR ZERO
"""

try:
    # Captura de número convirtiendo a float para admitir decimales -> Number capture converting to float to support decimals
    user_input = input("Introduce un número por favor -> Please enter a number: ").strip()
    number = float(user_input) if user_input else 0.0

    # Condicionales para clasificar el número -> Conditionals to classify the number
    if number > 0:
        print(f"El número {number} es positivo -> The number {number} is positive")
    elif number < 0:
        print(f"El número {number} es negativo -> The number {number} is negative")
    else:
        print("El número es cero -> The number is zero")

except ValueError:
    print("Error: Ingresa un número válido -> Error: Please enter a valid number")
