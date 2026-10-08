# 06-for-loops.py

# El bucle 'for' se usa para iterar (recorrer) sobre secuencias como listas, textos o rangos de números. -> The 'for' loop is used to iterate (traverse) over sequences like lists, strings, or ranges of numbers.


# 1. Recorrer una lista de elementos -> Iterate over a list of elements
snacks = ["Manzana", "Pan integral", "Buñuelo", "Durazno"]
print("--- Menú de mecatos ---")

for snack in snacks:
    print(f"Disponible en el minimarket: {snack}")


# 2. Recorrer los caracteres de un String -> Iterate over the characters of a String
# Cada ciclo toma una letra del texto -> Each cycle takes a letter from the text
tech_stack = "Python"
print("\n--- Deletreando la tecnología ---")

for letter in tech_stack:
    print(f"Letra: {letter}")


# 3. Bucle 'for' con range(inicio, fin, paso) -> 'for' loop with range(start, end, step)
# Recuerda: el límite superior no se incluye. -> Remember: the upper limit is not included.
print("\n--- Contador de rondas en partida ---")

for round_num in range(1, 4):
    print(f"Iniciando Ronda #{round_num} en Blood Strike")
