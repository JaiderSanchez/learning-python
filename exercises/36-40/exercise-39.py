"""
VERIFICAR SI LA PALABRA INGRESADA ES 'PYTHON' -> CHECK IF THE ENTERED WORD IS 'PYTHON'
"""

word_input = input("Introduce una palabra para verificar -> Enter a word to check: ").strip()

# Asignar palabra predeterminada si la entrada está vacía -> Assign default word if input is empty
target_word = word_input if word_input else "Python"

# Comparación insensible a mayúsculas/minúsculas con .lower() -> Case-insensitive comparison using .lower()
if target_word.lower() == "python":
    print(f"¡Éxito! La palabra '{target_word}' es 'Python' -> Success! The word '{target_word}' is 'Python'")
else:
    print(f"¡Error! La palabra '{target_word}' NO es 'Python' -> Error! The word '{target_word}' is NOT 'Python'")
