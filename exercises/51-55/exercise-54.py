"""
IMPRIMIR LOS CARACTERES DE UNA CADENA UTILIZANDO EL CICLO FOR -> PRINT THE CHARACTERS OF A STRING USING A FOR LOOP
"""

message: str = "Hello, how are You? I hope you are doing very well."

print("--- Caracteres individuales -> Individual characters ---")

# Las cadenas son iterables carácter por carácter -> Strings are iterable character by character
for character in message:
    print(character)
