"""
REALIZAR LA POTENCIA DE UN NÚMERO -> CALCULATE THE POWER OF A NUMBER
"""

# Manejo de excepciones para validar entradas numéricas -> Exception handling to validate numeric inputs
try:
    base = int(input("Ingresa la base por favor -> Please enter the base: "))
    exponent = int(input("Ingresa el exponente por favor -> Please enter the exponent: "))
    
    # Cálculo de la potencia usando el operador ** -> Power calculation using the ** operator
    power_result = base ** exponent
    
    print(f"El resultado de la potencia es -> The result of the power is: {power_result}")

except ValueError:
    print("Error: Ingresa únicamente números enteros -> Error: Please enter integers only")
    