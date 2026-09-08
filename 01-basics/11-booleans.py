# 11-booleans.py

# Los booleanos siempre se escriben con la primera letra en mayúscula. -> Booleans are always written with the first letter capitalized.
is_remote_job = True
requires_relocation = False

# 1. Evaluando condiciones -> Evaluating Conditions
# Cuando comparamos cosas, Python siempre  responde con un booleano. -> When we compare things, Python always responds with a boolean.
python_level = 10
required_level = 5
meets_requirements = python_level >= required_level

print(f"¿Cumple con el nivel de Python para la vacante? {meets_requirements}")

# 2. Booleanos y Snacks (Lógica AND / OR) -> Booleans and Snacks (AND / OR Logic)
# Para una sesión de código perfecta, necesitamos ambas cosas (and). -> For a perfect coding session, we need both things (and).
has_empanadas = True
has_pony_malta = False

perfect_session = has_empanadas and has_pony_malta
print(f"¿Tenemos el combo perfecto de empanada y Pony Malta? {perfect_session}")
