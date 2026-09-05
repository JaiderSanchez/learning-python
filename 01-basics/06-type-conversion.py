# 06-type-conversion.py

# Conversión de tipos (Type Casting) es como un Transformer. -> Type Casting is like a Transformer.
# A veces tenemos un dato disfrazado de otra cosa y necesitamos transformarlo. -> 

# 1. De Texto (str) a Entero (int) -> Useful if you read a number as text and need to calculate with it.
# Imagina que lees la memoria RAM de tu sistema pero llega como texto
ram_text = "12" 
ram_number = int(ram_text)
print(f"Ahora la RAM es un número para calcular: {ram_number + 4} GB en total.")

# 2. De Entero (int) a Texto (str) -> Useful if you need to join numbers with text in the classic way.
kills = 50
message = "Logré " + str(kills) + " bajas seguidas en Call of Duty."
print(message)

# 3. De Texto (str) a Decimal (float) -> Useful if you need to perform calculations with decimal numbers.
# Calculando gastos en comida -> Calculating food expenses
price_text = "7000.50"
price_number = float(price_text)
print(f"El almuerzo base cuesta {price_number}. Con la sopa, carne y principios sube a {price_number + 3000.0}")

# 4. A Booleano (bool) -> Converting to Boolean
# La regla de oro: el 0 y los textos vacíos "" siempre se transforman en False. Lo demás es True.
players_online = 0
is_game_active = bool(players_online) 
print(f"¿Hay jugadores conectados? {is_game_active}")
