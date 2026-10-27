"""
CONVERTIR UN NÚMERO ENTERO EN CADENA DE TEXTO -> CONVERT AN INTEGER NUMBER TO A TEXT STRING
"""

try:
    # Captura de número entero por consola -> Integer input capture from console
    number_input = int(input("Ingresa un número entero por favor -> Please enter an integer number: "))

    print(f"Tipo de dato original -> Original data type: {type(number_input)}")

    # Conversión explícita a cadena de texto -> Explicit conversion to text string
    text_string = str(number_input)

    print(f"Tipo de dato convertido -> Converted data type: {type(text_string)}")
    print(f"Valor convertido a texto -> Text value: '{text_string}'")

except ValueError:
    print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer number")
    