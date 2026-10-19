# 02-tuples.py

# Las tuplas son inmutables y ordenadas -> Tuples are immutable and ordered
# Se definen usando paréntesis () -> They are defined using parentheses ()

# 1. Creación e inmutabilidad -> 1. Creation and immutability
# Coordenadas aproximadas de Yopal, Casanare (Latitud, Longitud) -> Approximate coordinates of Yopal, Casanare (Latitude, Longitude)
yopal_coordinates: tuple[float, float] = (5.3378, -72.3959)
print(f"Coordenadas de Yopal: {yopal_coordinates}")

# Intentar modificar un elemento arrojaría un TypeError: -> Attempting to modify an element would raise a TypeError:
# yopal_coordinates[0] = 6.0  <-- Esto no está permitido en tuplas -> yopal_coordinates[0] = 6.0  <-- This is not allowed in tuples


# 2. Desempaquetado de Tuplas (Tuple Unpacking) -> 2. Tuple Unpacking
# Asignamos cada elemento de la tupla a variables individuales en una sola línea -> Assign each tuple element to individual variables in a single line
latitude, longitude = yopal_coordinates
print(f"Latitud: {latitude} | Longitud: {longitude}")


# 3. Métodos nativos de Tuplas (.count y .index) -> 3. Native tuple methods (.count and .index)
server_status_codes: tuple[int, ...] = (200, 200, 404, 200, 500, 200)

# Contar cuántas veces aparece un elemento (.count) -> Count how many times an element appears (.count)
successful_requests = server_status_codes.count(200)
print(f"Respuestas exitosas (200 OK): {successful_requests}")

# Buscar el índice de la primera ocurrencia (.index) -> Find the index of the first occurrence (.index)
first_error_index = server_status_codes.index(404)
print(f"Primer error 404 encontrado en la posición: {first_error_index}")
