"""
ELIMINAR DUPLICADOS DE UNA LISTA -> REMOVE DUPLICATES FROM A LIST
"""

numbers_list: list[int] = [1, 2, 2, 3, 4, 4, 5, 5, 7, 7]

# Método 1: Usando set() (no garantiza preservar el orden original) -> Method 1: Using set() (does not guarantee preserving original order)
unique_set_list: list[int] = list(set(numbers_list))

# Método 2: Usando dict.fromkeys() (elimina duplicados preservando el orden) -> Method 2: Using dict.fromkeys() (removes duplicates while preserving order)
unique_ordered_list: list[int] = list(dict.fromkeys(numbers_list))

print(f"Lista original con duplicados -> Original list with duplicates: {numbers_list}")
print(f"Sin duplicados (usando set) -> Without duplicates (using set): {unique_set_list}")
print(f"Sin duplicados (preservando orden) -> Without duplicates (preserving order): {unique_ordered_list}")
