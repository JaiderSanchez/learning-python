"""
CREAR UNA CLASE RECTÁNGULO CON MÉTODOS PARA ÁREA Y PERÍMETRO -> CREATE A RECTANGLE CLASS WITH AREA AND PERIMETER METHODS
"""

class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        """Calcula el área (base * altura) -> Calculates area (base * height)."""
        return self.base * self.height

    def calculate_perimeter(self) -> float:
        """Calcula el perímetro 2 * (base + altura) -> Calculates perimeter 2 * (base + height)."""
        return 2 * (self.base + self.height)


try:
    # Solicitar medidas por teclado o usar 5 y 3 por defecto -> Prompt for dimensions or use 5 and 3 by default
    base_input: str = input("Ingresa la base del rectángulo (Enter para 5) -> Enter rectangle base (Enter for 5): ").strip()
    height_input: str = input("Ingresa la altura del rectángulo (Enter para 3) -> Enter rectangle height (Enter for 3): ").strip()

    base_val: float = float(base_input) if base_input else 5.0
    height_val: float = float(height_input) if height_input else 3.0

    if base_val <= 0 or height_val <= 0:
        print("Error: La base y la altura deben ser mayores a cero -> Error: Base and height must be greater than zero.")
    else:
        rect1 = Rectangle(base_val, height_val)
        print(f"El área es -> Area is: {rect1.calculate_area():.2f}")
        print(f"El perímetro es -> Perimeter is: {rect1.calculate_perimeter():.2f}")

except ValueError:
    print("Error: Ingresa valores numéricos válidos -> Error: Please enter valid numeric values.")
