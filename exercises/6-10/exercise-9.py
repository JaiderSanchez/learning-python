"""
CALCULAR EL PROMEDIO DE UNA LISTA DE NÚMEROS -> CALCULATE THE AVERAGE OF A LIST OF NUMBERS
"""

numbers_list: list[float] = [2, 4, 6, 8]

# Validación para evitar división por cero -> Validation to prevent division by zero
if len(numbers_list) > 0:
    average_result = sum(numbers_list) / len(numbers_list)
    print(f"El promedio de la lista es -> The average of the list is: {average_result}")
else:
    print("La lista está vacía -> The list is empty")
    