"""
DIVIDIR UNA CADENA EN UNA LISTA DE SUBCADENAS -> SPLIT A STRING INTO A LIST OF SUBSTRINGS
"""

# Captura de texto del usuario -> User text capture
user_text = input("Ingresa una frase por favor (o Enter para el predeterminado) -> Enter a sentence (or press Enter for default): ").strip()

text_string = user_text if user_text else "Hello, how are you today?"

# El método .split() divide por espacios por defecto -> The .split() method splits by spaces by default
substrings_list: list[str] = text_string.split()

print(f"Cadena original -> Original string: '{text_string}'")
print(f"Lista de subcadenas -> List of substrings: {substrings_list}")
