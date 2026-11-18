"""
IMPRIMIR LOS NÚMEROS DEL N AL 1 EN ORDEN DESCENDENTE -> PRINT NUMBERS FROM N DOWN TO 1 IN DESCENDING ORDER
"""

try:
    # Solicitar número inicial o usar 5 por defecto -> Request starting number or use 5 by default
    user_input: str = input("Ingresa el número inicial para la cuenta regresiva (Enter para 5) -> Enter starting number for countdown (Enter for 5): ").strip()
    start_number: int = int(user_input) if user_input else 5

    if start_number < 1:
        print("El número inicial debe ser mayor o igual a 1 -> Starting number must be greater than or equal to 1.")

    else:
        print(f"\n--- Cuenta regresiva desde {start_number} -> Countdown from {start_number} ---")

        # El tercer parámetro -1 indica decremento paso a paso -> The third parameter -1 indicates step-by-step decrement
        for number in range(start_number, 0, -1):
            print(number)

except ValueError:
    print("Error: Debes ingresar un número entero válido -> Error: You must enter a valid integer.")
