# 04-dictionaries.py

# Los diccionarios almacenan datos en pares clave-valor -> Dictionaries store data in key-value pairs
# Son mutables y optimizados para búsquedas rápidas -> They are mutable and optimized for fast lookups

# 1. Creación y acceso a datos -> 1. Creation and accessing data
developer_profile: dict[str, str | int | float] = {
    "name": "Jaider",
    "role": "Junior Web Developer",
    "city": "Yopal",
    "experience_years": 1.5
}

# Uso seguro de .get() para evitar KeyErrors -> Safe use of .get() to prevent KeyErrors
dev_role = developer_profile.get("role", "Not specified") # .get("role", ...) = “Búscame el rol”. 🔍. El segundo valor ("Not specified") es el plan B: si la clave no existe, devuelve eso en vez de dar error. -> .get("role", ...) = “Find the role for me.” 🔍. The second value ("Not specified") is the backup plan: if the key doesn’t exist, it returns that instead of throwing an error.
print(f"Rol del desarrollador: {dev_role}")

# 2. Agregar y actualizar pares clave-valor -> 2. Adding and updating key-value pairs
snack_prices: dict[str, int] = {
    "Galleta de Avena": 2000,
    "Pony Malta": 3000,
    "Almojábana": 2000
}

# Actualizar o agregar nueva clave -> Update or add new key
snack_prices["Galleta de Avena"] = 2500  # Actualización -> Update
snack_prices["Pan de queso"] = 3000  # Nuevo elemento -> New item
print(f"Precios actualizados: {snack_prices}") # Si la clave no existe → Python la crea. Si la clave ya existe → Python cambia su valor -> If the key does not exist, Python creates it. If the key already exists, Python changes its value.

# 3. Recorrer un diccionario (.items, .keys, .values) -> 3. Iterating through a dictionary (.items, .keys, .values)
print("\n--- Catálogo de Snacks ---")
for snack, price in snack_prices.items():
    print(f"- {snack}: ${price} COP")


# Truco para recordar: -> Memory trick
# -- Set = “Solo uno de cada uno” 🧺 -> Set = “Solo uno de cada uno”
# -- Diccionario = “Busco por nombre, encuentro el dato” 📇 -> Dictionary = “Search by name, find the information” 📇
