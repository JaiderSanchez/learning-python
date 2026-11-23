"""
ESCRIBIR UNA FUNCIÓN PARA CALCULAR EL VOLUMEN DE UN CILINDRO (V = π * r² * h) -> WRITE A FUNCTION TO CALCULATE THE VOLUME OF A CYLINDER
"""

import math

def calculate_cylinder_volume(radius: float, height: float) -> float:
    """Calcula el volumen del cilindro -> Calculates the volume of the cylinder."""
    return math.pi * (radius ** 2) * height

try:
    # Solicitar radio y altura o usar 3 y 5 por defecto -> Request radius and height or use 3 and 5 by default
    radius_input: str = input("Ingresa el radio del cilindro (Enter para 3) -> Enter cylinder radius (Enter for 3): ").strip()
    
    height_input: str = input("Ingresa la altura del cilindro (Enter para 5) -> Enter cylinder height (Enter for 5): ").strip()

    radius_val: float = float(radius_input) if radius_input else 3.0
    height_val: float = float(height_input) if height_input else 5.0

    if radius_val <= 0 or height_val <= 0:
        print("Error: El radio y la altura deben ser mayores a cero -> Error: Radius and height must be greater than zero.")
    else:
        volume: float = calculate_cylinder_volume(radius_val, height_val)
        print(f"El volumen del cilindro es -> The volume of the cylinder is: {volume:.2f}")

except ValueError:
    print("Error: Ingresa valores numéricos válidos -> Error: Please enter valid numeric values.")
