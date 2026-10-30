"""
CONVERTIR UN NÚMERO DECIMAL A UN NÚMERO ENTERO -> CONVERT A DECIMAL NUMBER TO AN INTEGER
"""

try:
    # Captura de número decimal por consola o valor predeterminado -> Decimal number capture or default value
    user_input = input("Ingresa un número decimal (o Enter para usar el predeterminado) -> Enter a decimal number (or Enter for default): ").strip()
    
    decimal_number = float(user_input) if user_input else 26.171819

    # Conversión explícita a entero (trunca la parte decimal) -> Explicit conversion to integer (truncates decimal part)
    integer_number = int(decimal_number)

    print(f"Número decimal original -> Original decimal number: {decimal_number}")
    print(f"Número convertido a entero -> Converted integer number: {integer_number}")

except ValueError:
    print("Error: Ingresa un número decimal válido -> Error: Please enter a valid decimal number")
    