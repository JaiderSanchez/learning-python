"""
ENCUENTRAR Y MOSTRAR EL ÚLTIMO CARÁCTER DE UNA CADENA -> FIND AND DISPLAY THE LAST CHARACTER OF A STRING
"""

text_string = 'I am working on exercises in Python'

# Extracción del último carácter con índice negativo -1 -> Extraction of the last character using negative index -1
last_character = text_string[-1]

# Ejemplo opcional: Extraer la última palabra completa ("Python") usando slicing -> Optional example: Extract full last word ("Python") using slicing
last_word = text_string[-6:]

print(f"Último carácter -> Last character: '{last_character}'")
print(f"Última palabra completa -> Full last word: '{last_word}'")
