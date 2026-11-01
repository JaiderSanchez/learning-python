"""
REALIZAR OPERACIONES BÁSICAS CON CONJUNTOS: UNIÓN E INTERSECCIÓN -> PERFORM BASIC SET OPERATIONS: UNION AND INTERSECTION
"""

# Definición de conjuntos con tipos anotados -> Set definitions with annotated types
set_a: set[str] = {"Pera", "Manzana", "Fresa", "Kiwi", "Nucita"}
set_b: set[str] = {"Chocoramo", "Galleta Cocosette", "Chocolatina Jet", "Nucita"}

# Operación de Unión (|): Junta todos los elementos únicos de ambos conjuntos -> Union (|): Joins all unique elements from both sets
union_result: set[str] = set_a | set_b

# Operación de Intersección (&): Retorna solo los elementos presentes en ambos conjuntos -> Intersection (&): Returns only elements present in both sets
intersection_result: set[str] = set_a & set_b

print(f"Conjunto A -> Set A: {set_a}")
print(f"Conjunto B -> Set B: {set_b}")
print(f"Unión de conjuntos -> Set union: {union_result}")
print(f"Intersección de conjuntos -> Set intersection: {intersection_result}")
