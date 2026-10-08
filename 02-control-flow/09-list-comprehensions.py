# 09-list-comprehensions.py

# Sintaxis básica: [expresion for elemento in iterable if condicion] -> Basic syntax: [expression for element in iterable if condition]

# 1. Forma tradicional (3 líneas) vs List Comprehension (1 línea) -> 1. Traditional way (3 lines) vs List Comprehension (1 line)
scores = [45, 12, 89, 100, 32, 67]

# Método tradicional:
high_scores_trad = []
for score in scores:
    if score >= 50:
        high_scores_trad.append(score)

# Método Pythonic (List Comprehension):
high_scores = [score for score in scores if score >= 50]

print(f"Puntuaciones destacadas (>=50): {high_scores}")


# 2. Transformar elementos en una sola línea -> 2. Transform elements in a single line
snacks = ["Avena natural", "Banano", "Chocoramo"]

# Convertimos cada palabra a mayúsculas directamente al crear la lista -> We convert each word to uppercase directly when creating the list
uppercase_snacks = [snack.upper() for snack in snacks]
print(f"Menú en mayúsculas: {uppercase_snacks}")


# 3. Múltiples operaciones -> 3. Multiple operations
# Filtrar números pares y multiplicarlos por 2 -> Filter even numbers and multiply them by 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled_evens = [n * 2 for n in numbers if n % 2 == 0]

print(f"Pares duplicados: {doubled_evens}")
