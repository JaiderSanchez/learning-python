"""
ESCRIBIR UNA FUNCIÓN PARA CALCULAR EL PROMEDIO DE UNA LISTA DE NÚMEROS -> WRITE A FUNCTION TO CALCULATE THE AVERAGE OF A LIST OF NUMBERS
"""

def calculate_average(numbers: list[float]) -> float:
    """Calcula el promedio evitando división por cero -> Calculates average avoiding division by zero."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


try:
    # Solicitar números separados por coma o usar [4, 6, 8, 10] por defecto -> Request comma-separated numbers or use [4, 6, 8, 10] by default
    user_input: str = input("Ingresa números separados por coma (Enter para 4, 6, 8, 10) -> Enter comma-separated numbers (Enter for 4, 6, 8, 10): ").strip()

    if user_input:
        numbers_list: list[float] = [float(item.strip()) for item in user_input.split(",")]
    else:
        numbers_list = [4.0, 6.0, 8.0, 10.0]

    average_result: float = calculate_average(numbers_list)
    print(f"Lista evaluada -> Evaluated list: {numbers_list}")
    print(f"El promedio es -> The average is: {average_result:.2f}")

except ValueError:
    print("Error: Ingresa únicamente números separados por comas -> Error: Please enter valid numbers separated by commas.")

