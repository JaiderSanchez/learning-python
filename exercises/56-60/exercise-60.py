"""
IMPRIMIR LA SUMA DE LOS NÚMEROS PARES DEL 1 AL N UTILIZANDO EL CICLO FOR -> PRINT THE SUM OF EVEN NUMBERS FROM 1 TO N USING A FOR LOOP
"""

try:
    # Solicitar límite superior o usar 10 por defecto -> Request upper limit or use 10 by default
    user_input: str = input("Ingresa el límite superior para sumar pares (Enter para 10) -> Enter upper limit to sum evens (Enter for 10): ").strip()
    limit: int = int(user_input) if user_input else 10

    if limit < 1:
        print("El límite debe ser mayor o igual a 1 -> The limit must be greater than or equal to 1.")

    else:
        even_sum: int = 0

        for number in range(1, limit + 1):
            if number % 2 == 0:
                even_sum += number

        print(f"La suma de los números pares del 1 al {limit} es -> The sum of even numbers from 1 to {limit} is: {even_sum}")

except ValueError:
    print("Error: Debes ingresar un número entero válido -> Error: You must enter a valid integer.")
