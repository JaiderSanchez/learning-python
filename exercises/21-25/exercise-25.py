"""
GENERAR UNA LISTA DE NÚMEROS DEL 1 AL 200 -> GENERATE A LIST OF NUMBERS FROM 1 TO 200
"""

# range(1, 201) genera números desde 1 hasta 200 (el límite superior es exclusivo) -> range(1, 201) generates numbers from 1 up to 200 (upper bound is exclusive)
numbers_list: list[int] = list(range(1, 201))

print(f"Primeros 5 elementos -> First 5 elements: {numbers_list[:5]}")
print(f"Últimos 5 elementos -> Last 5 elements: {numbers_list[-5:]}")
print(f"Total de elementos en la lista -> Total elements in list: {len(numbers_list)}")

# NOTA IMPORTANTE: Este ejercicio es útil para generar datos de prueba (dummy data) -> IMPORTANT NOTE: This exercise is useful for generating dummy test data
