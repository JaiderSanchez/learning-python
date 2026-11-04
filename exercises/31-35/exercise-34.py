"""
VERIFICAR SI UNA CADENA TIENE 10 O MÁS CARACTERES -> CHECK IF A STRING HAS 10 OR MORE CHARACTERS
"""

# Captura de texto del usuario -> User text capture
text_input = input("Introduce una cadena de texto -> Enter a text string: ")

# Evaluación de longitud con len() -> Length evaluation with len()
if len(text_input) >= 10:
    print(f"La cadena tiene {len(text_input)} caracteres (10 o más) -> The string has {len(text_input)} characters (10 or more)")
else:
    print(f"La cadena tiene solo {len(text_input)} caracteres (menos de 10) -> The string has only {len(text_input)} characters (less than 10)")
