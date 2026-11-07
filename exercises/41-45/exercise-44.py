"""
JUEGO DE ADIVINAR UN NÚMERO ALEATORIO DEL 1 AL 10 -> GUESS THE RANDOM NUMBER GAME (1 TO 10)
"""

import random

# Generar número secreto entre 1 y 10 inclusive -> Generate secret number between 1 and 10 inclusive
secret_number: int = random.randint(1, 10)

# Contador independiente para los intentos reales -> Independent counter for actual attempts
attempts_count: int = 0

print("=== Juego de Adivinanzas -> Guessing Game ===")

while True:
    try:
        user_input = input("Adivina el número (entre 1 y 10) -> Guess the number (between 1 and 10): ").strip()
        user_guess = int(user_input)
        
        # Incrementar el contador real de intentos -> Increment actual attempt counter
        attempts_count += 1

        # Validar rango del número ingresado -> Validate entered number range
        if user_guess < 1 or user_guess > 10:
            print("Por favor ingresa un número dentro del rango de 1 a 10 -> Please enter a number within the 1 to 10 range")
            continue

        if user_guess == secret_number:
            print(f"¡Felicidades! Adivinaste el número {secret_number} en {attempts_count} intento(s) -> Congratulations! You guessed the number {secret_number} in {attempts_count} attempt(s).")
            break
        elif user_guess < secret_number:
            print("El número secreto es MAYOR -> The secret number is HIGHER")
        else:
            print("El número secreto es MENOR -> The secret number is LOWER")

    except ValueError:
        print("Error: Ingresa un número entero válido -> Error: Please enter a valid integer")
