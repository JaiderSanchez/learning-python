"""
SIMULAR EL LANZAMIENTO DE UNA MONEDA (CARA O SELLO) -> SIMULATE A COIN TOSS (HEADS OR TAILS)
"""

import random

print("=== Simulador de Lanzamiento de Moneda -> Coin Toss Simulator ===")

while True:
    # Generar resultado aleatorio (1 = Cara, 2 = Sello) -> Generate random outcome (1 = Heads, 2 = Tails)
    coin_side: int = random.randint(1, 2)

    if coin_side == 1:
        print("Resultado -> Result: Cara (Heads)")
    else:
        print("Resultado -> Result: Sello (Tails)")

    play_again: str = input("¿Deseas lanzar la moneda nuevamente? (s/n) -> Toss again? (y/n): ").strip().lower()

    if play_again in ("n", "no"):
        break

# Mensaje ubicado fuera del bucle para ejecutarse solo al finalizar -> Message placed outside loop to run only upon exit
print("Lanzamiento finalizado. ¡Gracias por jugar! -> Toss finished. Thanks for playing!")
