"""
CALCULAR EL IMC (ÍNDICE DE MASA CORPORAL) E INTERPRETARLO -> CALCULATE BMI (BODY MASS INDEX) AND INTERPRET IT
"""

try:
    weight_input = input("Introduce tu peso en kg (ej. 70) -> Enter your weight in kg (e.g. 70): ").strip()
    height_input = input("Introduce tu altura en metros (ej. 1.75) -> Enter your height in meters (e.g. 1.75): ").strip()

    weight = float(weight_input) if weight_input else 70.0
    height = float(height_input) if height_input else 1.75

    if height <= 0 or weight <= 0:
        raise ValueError("El peso y la altura deben ser mayores a cero")

    # Cálculo del IMC: Peso / (Altura ** 2) -> BMI Calculation: Weight / (Height ** 2)
    bmi = weight / (height ** 2)

    print(f"\nTu IMC calculado es -> Your calculated BMI is: {bmi:.2f}")

    # Clasificación del IMC según rangos de la OMS -> BMI classification according to WHO ranges
    if bmi < 18.5:
        interpretation = "Bajo peso -> Underweight"
    elif bmi < 25.0:
        interpretation = "Peso normal -> Normal weight"
    elif bmi < 30.0:
        interpretation = "Sobrepeso -> Overweight"
    elif bmi < 35.0:
        interpretation = "Obesidad grado 1 -> Class 1 Obesity"
    elif bmi < 40.0:
        interpretation = "Obesidad grado 2 -> Class 2 Obesity"
    else:
        interpretation = "Obesidad grado 3 -> Class 3 Obesity"

    print(f"Categoría -> Category: {interpretation}")

except ValueError:
    print("Error: Ingresa valores válidos y positivos para peso y altura -> Error: Please enter valid positive values for weight and height")
    