"""
CREAR UNA FUNCIÓN PARA CALCULAR EL ÁREA DE UN CÍRCULO -> CREATE A FUNCTION TO CALCULATE THE AREA OF A CIRCLE
"""

import math


def calculate_circle_area(radius: float) -> float:
    """Calcula el área usando pi * radio^2 -> Calculates the area using pi * radius^2."""
    return math.pi * (radius ** 2)


try:
    # Solicitar radio o usar 5 por defecto -> Request radius or use 5 by default
    radius_input: str = input("Ingresa el radio del círculo (Enter para 5) -> Enter circle radius (Enter for 5): ").strip()
    circle_radius: float = float(radius_input) if radius_input else 5.0

    if circle_radius < 0:
        print("Error: El radio no puede ser negativo -> Error: Radius cannot be negative.")
    else:
        area: float = calculate_circle_area(circle_radius)
        print(f"El área del círculo con radio {circle_radius} es -> The area of the circle with radius {circle_radius} is: {area:.2f}")

except ValueError:
    print("Error: Ingresa un número válido para el radio -> Error: Please enter a valid number for the radius.")
