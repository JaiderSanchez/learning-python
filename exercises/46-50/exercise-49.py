"""
SIMULAR EL LANZAMIENTO DE UN DADO HASTA OBTENER UN 6 -> SIMULATE ROLLING A DIE UNTIL GETTING A 6
"""

import random

dice_value: int = 0
rolls_count: int = 0

print("=== Lanzando el dado -> Rolling the die ===")

# Repetir lanzamientos hasta obtener 6 -> Repeat rolls until 6 is rolled
while dice_value != 6:
    dice_value = random.randint(1, 6)
    rolls_count += 1
    print(f"Lanzamiento #{rolls_count}: Has sacado el número {dice_value} -> Roll #{rolls_count}: You rolled {dice_value}")

print(f"¡Felicidades! Obtuviste un 6 en {rolls_count} intento(s). Fin del juego -> Congratulations! You rolled a 6 in {rolls_count} attempt(s). Game over.")
