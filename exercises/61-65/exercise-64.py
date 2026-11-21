"""
ESCRIBIR UNA FUNCIÓN PARA VERIFICAR SI UN NÚMERO ES PAR O IMPAR -> WRITE A FUNCTION TO CHECK IF A NUMBER IS EVEN OR ODD
"""

def is_even(number: int) -> bool:
    """Retorna True si el número es par, False si es impar -> Returns True if number is even, False if odd."""
    return number % 2 == 0


try:
    # Solicitar número entero o usar 10 por defecto -> Request integer or use 10 by default
    num_input: str = input("Ingresa un número entero (Enter para 10) -> Enter an integer (Enter for 10): ").strip()
    target_number: int = int(num_input) if num_input else 10

    result: bool = is_even(target_number)
    print(f"¿El número {target_number} es par? -> Is {target_number} even?: {result}")

except ValueError:
    print("Error: Debes ingresar un número entero válido -> Error: You must enter a valid integer.")
    