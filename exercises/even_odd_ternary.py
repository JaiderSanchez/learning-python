"""
VERIFICAR SI UN NÚMERO ES PAR O IMPAR (ENFOQUE TERNARIO) -> CHECK IF A NUMBER IS EVEN OR ODD (TERNARY APPROACH)
"""

try:
    # Captura de datos de entrada del usuario -> User input capture
    user_input = input("Introduce un número entero (o Enter para el predeterminado) -> Enter an integer (or press Enter for default): ").strip()
    number = int(user_input) if user_input else 4

    # Expresión ternaria evaluada dentro de una f-string -> Ternary expression evaluated inside an f-string
    parity_status = "even" if number % 2 == 0 else "odd"

    print(f"El número {number} es {parity_status} -> The number {number} is {parity_status}")

except ValueError:
    print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer")
