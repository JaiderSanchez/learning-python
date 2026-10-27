"""
PASAR UNA CADENA DE MAYÚSCULAS A MINÚSCULAS -> CONVERT A STRING FROM UPPERCASE TO LOWERCASE
"""

# Captura de texto del usuario -> User text capture
uppercase_text = input("Ingresa un texto en mayúsculas por favor -> Please enter text in uppercase: ")

# Asignar valor predeterminado si el usuario no ingresa texto -> Assign default value if input is empty
if not uppercase_text.strip():
    uppercase_text = 'CALL OF DUTY MODERN WARFARE 4'

# Conversión a minúsculas usando .lower() -> Conversion to lowercase using .lower()
lowercase_text = uppercase_text.lower()

print(f"Texto original -> Original text: {uppercase_text}")
print(f"Texto en minúsculas -> Lowercase text: {lowercase_text}")
