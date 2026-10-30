"""
MULTIPLICAR UNA CADENA POR UN NÚMERO ENTERO -> MULTIPLY A STRING BY AN INTEGER
"""

# Entrada de usuario o valor por defecto -> User input or default value
user_input = input("Ingresa un texto (o Enter para usar el predeterminado) -> Enter text (or press Enter for default): ").strip()
text_string = user_input if user_input else "Call of Duty Modern Warfare "

try:
    repetitions = int(input("Número de repeticiones (ej. 4) -> Number of repetitions (e.g. 4): ") or 4)
    
    # Multiplicación de cadenas (repite el texto N veces) -> String multiplication (repeats text N times)
    multiplication_result = text_string * repetitions

    print(f"Resultado de la multiplicación -> Multiplication result:\n{multiplication_result}")

except ValueError:
    print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer")
    