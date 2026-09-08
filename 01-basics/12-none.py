# 12-none.py

# Se usa mucho en desarrollo web cuando un usuario no llena un campo opcional en un formulario, o en un videojuego cuando aún no ha equipado un objeto. -> It is often used in web development when a user does not fill out an optional field in a form, or in a video game when they have not yet equipped an item.

# Al aterrizar en Blood Strike, no tengo arma secundaria. -> When landing in Blood Strike, I don't have a secondary weapon.
secondary_weapon = None
print(f"Arma al iniciar la partida: {secondary_weapon}")

# ¿Es None lo mismo que Falso? -> Is None the same as False?
# Cuando validamos None en una condición, Python lo interpreta como vacío/falso. -> When we validate None in a condition, Python interprets it as empty/false.
if not secondary_weapon:
    print("¡Estás desarmado! Busca loot rápido.")

# Después de lootear, la variable ya tiene un valor. -> After looting, the variable now has a value.
secondary_weapon = "Escopeta"
print(f"Arma equipada: {secondary_weapon}")
