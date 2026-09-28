"""INVIERTE EL SIGUIENTE NÚMERO: 2003"""

numero = 2003
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print(invertido)


"""VERSIÓN MATEMÁTICA DINÁMICA (CON INPUT)""" # Dynamic Mathematical Version (with input)

# Capturamos la entrada del usuario y la convertimos a número entero -> We capture the user input and convert it to an integer.
number = int(input("Enter the number you wish to invest: "))
original_number = number # Guardamos una copia para el mensaje final -> We are saving a copy for the final message.
invested = 0

# Mientras queden dígitos por procesar -> As long as there are digits left to process
while number > 0:
    digit = number % 10
    invested = invested * 10 + digit
    number = number // 10

print(f"The number {original_number} reversed is: {invested}")


"""LA FORMA "Pythonic" (Slicing [::-1])""" # THE "Pythonic" FORM (Slicing [::-1])
numero = 38123741

# Convertimos a string, invertimos con slicing y volvemos a convertir a entero -> We convert it to a string, reverse it using slicing, and convert it back to an integer.
invertido = int(str(numero)[::-1])

print(invertido)  # Imprime: 14732183 -> Print: 14732183
