"""
CALCULAR EL MÁXIMO DE TRES NÚMEROS -> CALCULATE THE MAXIMUM OF THREE NUMBERS
"""

try:
    # Captura de números por consola con valores por defecto -> Console number capture with default values
    input_1 = input("Introduce el primer número (o Enter para el predeterminado) -> Enter first number (or Enter for default): ").strip()
    input_2 = input("Introduce el segundo número -> Enter second number: ").strip()
    input_3 = input("Introduce el tercer número -> Enter third number: ").strip()

    num_1 = float(input_1) if input_1 else 15123.0
    num_2 = float(input_2) if input_2 else 208123.0
    num_3 = float(input_3) if input_3 else 24434.0

    # Evaluación del máximo utilizando la función nativa max() -> Maximum evaluation using built-in max() function
    maximum_value = max(num_1, num_2, num_3)

    print(f"El número máximo es -> The maximum number is: {maximum_value}")

except ValueError:
    print("Error: Ingresa únicamente números válidos -> Error: Please enter valid numbers only")
    