# 01-lists.py

# Las listas son mutables, ordenadas y permiten elementos duplicados -> Lists are mutable, ordered, and allow duplicate elements
# Se definen usando corchetes [] -> They are defined using square brackets []

# 1. Creación y manipulación básica -> 1. Creation and basic manipulation
favorite_snacks: list[str] = ["Pan de bono", "Galleta de avena", "Arequipe"]
print(f"Lista inicial de snacks: {favorite_snacks}")

# Agregar elementos al final (.append) -> Add elements to the end (.append)
favorite_snacks.append("Pera")

# Insertar en una posición específica (.insert) -> Insert at a specific position (.insert)
favorite_snacks.insert(1, "Pony Malta")
print(f"Lista actualizada: {favorite_snacks}")


# 2. Eliminar elementos -> 2. Remove elements
# .pop() remueve y retorna el último elemento (o el índice especificado) -> .pop() removes and returns the last element (or specified index)
last_item = favorite_snacks.pop()
print(f"Elemento removido con .pop(): {last_item}")

# .remove() busca y elimina el primer elemento que coincida con el valor -> .remove() searches for and removes the first element matching the value
favorite_snacks.remove("Arequipe")
print(f"Lista tras remover 'Arequipe': {favorite_snacks}")


# 3. Métodos útiles de ordenamiento y conteo -> 3. Useful sorting and counting methods
scores: list[int] = [85, 42, 99, 12, 70]

# Ordenar la lista in-place (modifica la lista original) -> Sort the list in-place (modifies the original list)
scores.sort()
print(f"Puntuaciones ordenadas (Ascendente): {scores}")

# Invertir el orden (.reverse) -> Reverse the order (.reverse)
scores.reverse()
print(f"Puntuaciones ordenadas (Descendente): {scores}")
