"""
CREAR UNA CLASE CÍRCULO CON MÉTODOS PARA ÁREA Y PERÍMETRO -> CREATE A CIRCLE CLASS WITH AREA AND PERIMETER METHODS
"""

import math


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        """Calcula el área (π * r²) -> Calculates area (π * r²)."""
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self) -> float:
        """Calcula el perímetro / circunferencia (2 * π * r) -> Calculates perimeter / circumference (2 * π * r)."""
        return 2 * math.pi * self.radius


try:
    # Solicitar radio o usar 5 por defecto -> Prompt for radius or use 5 by default
    radius_input: str = input("Ingresa el radio del círculo (Enter para 5) -> Enter circle radius (Enter for 5): ").strip()
    radius_val: float = float(radius_input) if radius_input else 5.0

    if radius_val <= 0:
        print("Error: El radio debe ser mayor a cero -> Error: Radius must be greater than zero.")
    else:
        circle1 = Circle(radius_val)
        print(f"El área del círculo es -> Circle area is: {circle1.calculate_area():.2f}")
        print(f"El perímetro del círculo es -> Circle perimeter is: {circle1.calculate_perimeter():.2f}")

except ValueError:
    print("Error: Ingresa un valor numérico válido -> Error: Please enter a valid numeric value.")
