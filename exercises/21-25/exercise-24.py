"""
ELIMINAR UN ELEMENTO ESPECÍFICO DE UNA LISTA -> REMOVE A SPECIFIC ELEMENT FROM A LIST
"""

# Renombramos la variable a 'fruits_list' para evitar sobrescribir la palabra reservada 'list' de Python -> Renamed variable to 'fruits_list' to avoid shadowing Python's built-in 'list'
fruits_list: list[str] = ["Pera", "Manzana", "Banano", "Uva"]

item_to_remove = "Banano"
# item_to_remove = "Fresa" -> Imprime: "El elemento 'Fresa' no se encuentra en la lista -> Element 'Fresa' not found in list."

print(f"Lista original -> Original list: {fruits_list}")

# Verificación de existencia previa para evitar 'ValueError' -> Check existence prior to removal to prevent 'ValueError'
if item_to_remove in fruits_list:
    fruits_list.remove(item_to_remove)
    print(f"Elemento '{item_to_remove}' eliminado -> Element '{item_to_remove}' removed.")
    print(f"Lista actualizada -> Updated list: {fruits_list}")
else:
    print(f"El elemento '{item_to_remove}' no se encuentra en la lista -> Element '{item_to_remove}' not found in list.")
