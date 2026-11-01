"""
COMBINAR DOS LISTAS EN PARES USANDO LA FUNCIÓN zip() -> COMBINE TWO LISTS INTO PAIRS USING THE zip() FUNCTION
"""

numbers_list: list[int] = [1, 2, 3]
letters_list: list[str] = ['a', 'b', 'c']

# Combinación en pares de tuplas con zip() -> Pairing into tuple pairs using zip()
paired_list: list[tuple[int, str]] = list(zip(numbers_list, letters_list))

print(f"Lista 1 (Números) -> List 1 (Numbers): {numbers_list}")
print(f"Lista 2 (Letras) -> List 2 (Letters): {letters_list}")
print(f"Resultado combinado en pares -> Combined pairs result: {paired_list}")
