"""
SOLICITAR UN NÚMERO Y COMPROBAR SI ES PAR O IMPAR USANDO IF Y MÓDULO (%) -> REQUEST A NUMBER AND CHECK IF IT IS EVEN OR ODD USING IF AND MODULO (%)
"""

try:
    # Captura de número entero por consola -> Integer number capture from console
    user_input = input("Introduce un número entero -> Please enter an integer: ").strip()
    number = int(user_input) if user_input else 4

    # Operador módulo (%) para evaluar el residuo de la división entre 2 -> Modulo operator (%) to evaluate the remainder of division by 2
    if number % 2 == 0:
        print(f"El número {number} es par -> The number {number} is even")
    else:
        print(f"El número {number} es impar -> The number {number} is odd")

except ValueError:
    print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer")
