# 04-input.py

# 1. Basic text input (Entrada de texto básica)
# The program pauses and waits for you to press 'Enter' after typing. (El programa se detiene y espera a que presiones 'Enter' después de escribir.)
player = input("¿Cuál es tu usuario en Blood Strike o Call of Duty? ")
print(f"¡Prepárate para la partida, {player}!")

# 2. Entrada de números (Requiere conversión)
# Si pedimos un número, input() lo entrega como texto: "45" en lugar de 45.
kills = input("¿Cuántas bajas conseguiste en tu última partida? ")
kills_int = int(kills) # Convertimos el texto a número entero

# Forma más rápida: pedir y convertir en la misma línea
matches_played = int(input("¿Cuántas partidas jugaste hoy? "))

# Ahora sí podemos hacer matemáticas con las variables
total_score = (kills_int * 100) + (matches_played * 50)
print(f"Tu puntuación total de hoy es: {total_score} puntos.")

# 3. Ejemplo combinando múltiples entradas
city = input("¿Desde qué ciudad te estás conectando? ")
snack_ingredient = input("¿Qué snack vas a consumir (ej. Doritos, Chocorramo, Pan de la Abuela)? ")

print(f"Transmitiendo desde {city}... ¡{player} recargando energías con un mecato de {snack_ingredient}!")
