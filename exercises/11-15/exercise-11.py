"""
CALCULAR EL ÁREA DE UN RECTÁNGULO CON DATOS DEL USUARIO -> CALCULATE THE AREA OF A RECTANGLE WITH USER INPUT
"""

# Captura y validación de datos de entrada -> Input data capture and validation
try:
    base = float(input("Ingresa la base del rectángulo por favor -> Please enter the base of the rectangle: "))
    height = float(input("Ingresa la altura del rectángulo por favor -> Please enter the height of the rectangle: "))

    # Cálculo del área (soporta decimales) -> Area calculation (supports decimals)
    rectangle_area = base * height

    print(f"El área del rectángulo es igual a -> The area of the rectangle is equal to: {rectangle_area}")

except ValueError:
    print("Error: Ingresa únicamente valores numéricos válidos -> Error: Please enter valid numerical values only")
    