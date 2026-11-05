"""
PEDIR UN CARÁCTER Y DETERMINAR SI ES UNA VOCAL -> ASK FOR A CHARACTER AND DETERMINE IF IT IS A VOWEL
"""

# Captura de entrada del usuario -> User input capture
user_input = input("Introduce un carácter por favor -> Please enter a character: ").strip()

# Selección del primer carácter o valor por defecto -> Selection of first character or default value
char = user_input[0] if user_input else 'a'

# Definición de cadena con vocales en minúscula -> String definition with lowercase vowels
vowels = "aeiouáéíóú"

# Verificación utilizando .lower() y el operador 'in' -> Verification using .lower() and 'in' operator
if char.lower() in vowels:
    print(f"El carácter '{char}' es una vocal -> The character '{char}' is a vowel")
else:
    print(f"El carácter '{char}' NO es una vocal -> The character '{char}' is NOT a vowel")
    