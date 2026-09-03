# 05-data-types.py

# 1. Primitivos (Tipos de datos básicos) -> Primitives (Basic data types)
player_name = "Jaider"         # String (str) - Texto -> Text
level = 45                     # Integer (int) - Número entero -> Integer number
kd_ratio = 1.95                # Float (float) - Número decimal -> Decimal number
is_online = True               # Boolean (bool) - Verdadero o Falso -> True or False

# 2. Colecciones (Contenedores que guardan múltiples datos) -> Collections (Containers that store multiple data items)

# Listas (list): Cajas ordenadas que son posibles modificar. -> Lists (list): Ordered containers that can be modified.
# Ideales para inventarios o cosas que cambian. -> Ideal for inventories or things that change.
loadout_weapons = ["M4", "AK-47", "Sniper"]
loadout_weapons.append("Granada") # Es posible agregar cosas nuevas a la lista -> It's possible to add new items to the list.

# Tuplas (tuple): Cajas ordenadas que no es posible modificar (inmutables). -> Tuples: Ordered containers that cannot be modified (immutable).
# Ideales para configuraciones fijas que no deben romperse. -> Ideal for fixed configurations that must not break.
screen_resolution = (1920, 1080)

# Diccionarios (dict): Cajas con "etiquetas" (clave-valor). -> Dictionaries (dict): Containers with "labels" (key-value pairs).
# Ideales para agrupar características de un solo objeto. -> Ideal for grouping characteristics of a single object.
ramen_recipe = {
    "base": "Fideos instantáneos",
    "topping_1": "Doritos",
    "topping_2": "Queso rallado",
    "topping_3": "Huevo cocido",
    "topping_4": "Ají",
    "spicy": True
}

# Conjuntos (set): Cajas desordenadas que no aceptan duplicados. -> Sets: Unordered collections that do not accept duplicates.
# Ideales para saber quiénes están conectados sin contar a nadie dos veces. -> Ideal for knowing who is connected without counting anyone twice.
connected_players = {"Jaider", "Jaider", "Paisa Sensei", "Jessica"} # "Jaider" solo se guardará una vez -> "Jaider" will only be stored once.

# 3. ¿Cómo saber qué tipo de dato tengo? Usamos la función type() -> How to know what data type I have? We use the type() function
print(f"La variable 'player_name' es de tipo: {type(player_name)}")
print(f"La variable 'loadout_weapons' es de tipo: {type(loadout_weapons)}")
print(f"El diccionario del ramen es de tipo: {type(ramen_recipe)}")
print(f"Los jugadores conectados (sin duplicados) son: {connected_players}")
