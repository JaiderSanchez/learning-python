"""
VERIFICAR SI UNA PALABRA ES UN PALÍNDROMO -> CHECK IF A WORD IS A PALINDROME
"""

# Lista de palíndromos populares en español e inglés -> List of popular palindromes in Spanish and English
palindrome_words: list[str] = [
    "radar", "reconocer", "sometemos", "rotor", 
    "anilina", "arepera", "madam", "level"
]

# Captura de palabra por usuario o prueba -> Word input by user or test case
user_word = input("Ingresa una palabra para verificar -> Enter a word to check: ").strip().lower()

target_word = user_word if user_word else "radar"

# Inversión de cadena con slicing [::-1] -> String reversal using slicing [::-1]
is_palindrome = target_word == target_word[::-1]

print(f"\n¿La palabra '{target_word}' es un palíndromo? -> Is the word '{target_word}' a palindrome?: {is_palindrome}")

# Probar la lista de palíndromos del catálogo -> Test catalog palindrome list
print("\n--- Lista de Palíndromos Famosos -> Famous Palindromes List ---")
for word in palindrome_words:
    check = word == word[::-1]
    print(f"- {word}: {check}")
