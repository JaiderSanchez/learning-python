# 07-strings.py

# Los Strings (textos) son como un tren. -> Strings (texts) are like a train.
# Cada letra va en un vagón, pero empezamos a contar desde el cero. -> Each letter goes in a wagon, but we start counting from zero.

game = "PES 2016"

# 1. Indexing (Sacar una sola letra o número) -> Indexing (Get a single letter or number)
first_char = game[0]  # El vagón 0 tiene la 'P'
last_char = game[-1]  # El truco del -1: siempre saca el último vagón (el '6')
print(f"Primer carácter: {first_char} | Último carácter: {last_char}")

# 2. Slicing (Cortar un pedazo del texto) -> Slicing (Cut a piece of the text)
# La regla mágica es: [inicio : final(sin incluir el final)] -> The magic rule is: [start : end (without including the end)]
title = game[0:3] # Saca del vagón 0 al 2 ('P', 'E', 'S') -> Get from wagon 0 to 2 ('P', 'E', 'S')
year = game[4:8]  # Saca del vagón 4 al 7 ('2016') -> Get from wagon 4 to 7 ('2016')
print(f"Juego: {title} | Año de edición: {year}")

# 3. Función len() (Saber el tamaño) -> len() function (Know the size)
# Nos dice cuántos espacios y letras hay en total. -> It tells us how many spaces and letters there are in total.
topping = "Condimentos"
size = len(topping)
print(f"La palabra '{topping}' ocupa {size} espacios de memoria.")
