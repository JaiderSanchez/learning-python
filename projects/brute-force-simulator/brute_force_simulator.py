"""
SIMULADOR BÁSICO DE FUERZA BRUTA -> BASIC BRUTE FORCE SIMULATOR
"""

import itertools
from time import time

# 1. Pedir una contraseña corta para probar -> Ask for a short password to test
password: str = input("Ingresa una contraseña corta (máx. 4 caracteres) -> Enter a short password (max 4 chars): ")

# 2. Definir los caracteres posibles (corrigiendo el guion largo '—' por '-') -> Define possible characters (fixing em-dash '—' to '-')
letters: str = "abcdefghijklmnopqrstuvwxyz"
numbers: str = "1234567890"
special: str = "!$%&/()=?-_"
chars: str = letters + numbers + special

start: float = time()
attempts: int = 0
found: bool = False

# 3. Validar que no sea muy larga para no congelar la PC -> Validate length so it doesn't freeze the PC
if len(password) > 4:
    print("Aviso: Usa máximo 4 caracteres para que la prueba sea rápida -> Warning: Use max 4 characters for a fast test.")
else:
    # Probar combinaciones de 1 hasta 4 caracteres -> Test combinations from 1 up to 4 characters
    for length in range(1, 5):
        # itertools.product arma combinaciones una por una sin llenar la memoria -> Builds combinations one by one without filling RAM
        for combo in itertools.product(chars, repeat=length):
            attempts += 1
            guess: str = "".join(combo)

            if guess == password:
                found = True
                break

        # Si ya la encontró, salimos también del primer bucle -> If already found, exit the outer loop too
        if found:
            break

    # 4. Mostrar resultados -> Show results
    runtime: float = time() - start

    if found:
        print(f"\n¡Contraseña encontrada! -> Password found!: '{password}'")
        print(f"Intentos -> Guesses: {attempts}")
        print(f"Tiempo -> Runtime: {runtime:.2f} segundos / seconds")
    else:
        print("\nNo se encontró en el rango de 4 caracteres -> Not found within 4 characters.")
