# 01-if-else.py

# El flujo de control nos permite tomar caminos diferentes según las condiciones. -> Control flow allows us to take different paths depending on the conditions..

# 1. El condicional básico (if - else) -> The basic conditional.
# Solo una de las dos opciones se ejecutará. -> Only one of the two options will execute.
health = 45

if health <= 50:
    # La indentación (los 4 espacios antes del print) es obligatoria en Python -> Indentation (the 4 spaces before print) is mandatory in Python.
    print("¡Alerta! Tu salud es baja en el combate, busca un botiquín rápido.")
else:
    print("Salud óptima. Estás listo para el enfrentamiento.")

# 2. Múltiples caminos (elif) -> Multiple paths (elif).
# 'elif' significa 'else if' (si no se cumplió lo anterior, intenta esto). -> 'elif' means 'else if' (if the previous condition wasn't met, try this one).
budget = 3500

if budget >= 4000:
    print("Alcanza perfecto para la Empanada y la Pony Malta.")
elif budget >= 2500:
    print("Alcanza para un Chocoramo.")
else:
    print("El presupuesto está ajustado, toma un vaso de agua.")

# 3. Operador Ternario (If-else en una sola línea) -> Ternary Operator (If-else in a single line).
# Súper útil en desarrollo web cuando necesitas asignar un valor rápido. -> Super useful in web development when you need to assign a quick value.
is_server_active = True
status = "Online" if is_server_active else "Offline"

print(f"El estado actual del servidor PostgreSQL es: {status}")
