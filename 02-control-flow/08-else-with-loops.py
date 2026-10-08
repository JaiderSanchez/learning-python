# 08-else-with-loops.py

# La cláusula 'else' en un bucle se ejecuta SOLO SI el bucle no fue interrumpido por un 'break'. -> The 'else' clause in a loop is executed ONLY IF the loop was not interrupted by a 'break'.

# 1. Búsqueda fallida (Ejecuta el bloque else) -> 1. Unsuccessful search (Executes the else block)
inventory = ["Avena natural", "Banano", "Chocoramo"]
target_snack = "Pan de la abuela"

print("--- Buscando snack en el inventario ---")
for item in inventory:
    if item == target_snack:
        print(f"¡Encontrado! Hay {target_snack} disponible.")
        break
else:
    # Se ejecuta porque el 'for' revisó todo sin activar el 'break' -> It executes because the 'for' loop checked everything without triggering the 'break'
    print(f"Aviso: No se encontró '{target_snack}' en la cafetería.")


# 2. Búsqueda exitosa (NO ejecuta el bloque else) -> 2. Successful search (Does NOT execute the else block)
players_in_lobby = ["Sniper_Xx", "Gamer_Yopal", "Carlos_99"]
search_player = "Gamer_Yopal"

print("\n--- Buscando jugador en la sala ---")
for player in players_in_lobby:
    if player == search_player:
        print(f"Jugador '{search_player}' está listo para jugar.")
        break  # Al activarse el break, el bloque 'else' se ignora por completo -> When the break is triggered, the 'else' block is completely ignored
else:
    print(f"El jugador '{search_player}' no está en la sala.")
