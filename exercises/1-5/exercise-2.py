"""
SUMAR DOS NÚMEROS Y MOSTRAR SU RESULTADO -> ADD TWO NUMBERS AND DISPLAY THE RESULT
"""

number_1 = 1
number_2 = 8
addition_result = number_1 + number_2

print("The sum result is:", addition_result)  # La coma pasa múltiples argumentos separándolos con espacio -> Comma passes multiple arguments separated by space

"""
EXPLICACIONES IMPORTANTES SOBRE CONCATENACIÓN O UNIR ARGUMENTOS -> IMPORTANT EXPLANATIONS ON CONCATENATION AND ARGUMENT JOINING
"""

# OPCIÓN 1: Separar argumentos con coma -> OPTION 1: Separate arguments with comma
# print("Result:", addition_result) -> print() recibe argumentos y los separa con espacio por defecto -> print() receives arguments and separates them with space by default

# OPCIÓN 2: Utilizar una f-string -> OPTION 2: Use an f-string
# print(f"Result: {addition_result}") -> La expresión se evalúa dentro de la plantilla de texto -> The expression is evaluated inside the string template

# OPCIÓN 3: Concatenar con + -> OPTION 3: Concatenate with +
# print("Result: " + str(addition_result)) -> Se unen cadenas explícitamente, requiriendo conversión con str() -> Strings are joined explicitly, requiring conversion with str()
