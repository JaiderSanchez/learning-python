"""NUMBER GUESSING GAME"""

import random  # Importamos el módulo para generar números aleatorios

# Genera un número entero aleatorio incluyente entre 1 y 100
numero = random.randint(1, 100)
intentos = 0

print("Adivina el número entre 1 y 100.")
print("Estoy pensando en un número entre 1 y 100. ¡Adivina cuál es!")

# Bucle infinito: se ejecutará repetidamente hasta que se encuentre un 'break'
while True:
    # Capturamos la entrada del usuario y la convertimos de string a entero (int)
    intento = int(input("Adivina el número: "))
    intentos += 1  # Incrementamos el contador de intentos (intentos = intentos + 1)

    # Validaciones de lógica condicional
    if intento < numero:
        print("El número es mayor. Intenta de nuevo.")
    elif intento > numero:
        print("El número es menor. Intenta de nuevo.")
    else:
        print("¡CORRECTO!")
        print(f"Adivinaste el número en {intentos} intentos.") # Uso de f-string para formatear e incrustar la variable directamente
        break  # Rompe el bucle 'while' y finaliza el juego