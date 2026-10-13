# 05-lambda-functions.py

# Las funciones lambda son funciones anónimas de una sola línea. -> Lambda functions are anonymous single-line functions.
# Sintaxis: lambda parametros: expresion -> Syntax: lambda parameters: expression

# 1. Lambda básica vs Función tradicional -> 1. Basic Lambda vs Traditional Function
# Tradicional: -> Traditional
# def calculate_tax(price: float) -> float:
#     return price * 0.19

# Lambda equivalente (ideal para cálculos rápidos): -> Equivalent Lambda (ideal for quick calculations):
calculate_tax = lambda price: price * 0.19 # Antes de los dos puntos : va lo que recibe (el ingrediente). Después de los dos puntos va lo que devuelve (el resultado) y No necesita return: porque devuelve el resultado solita.
print(f"IVA del snack ($2500): ${calculate_tax(2500)}")

# 2. Lambda con múltiples parámetros -> 2. Lambda with multiple parameters
calculate_total = lambda price, qty: price * qty
print(f"Total combo (3x $3500): ${calculate_total(3500, 3)}")

# 3. Uso práctico: Ordenar colecciones con sorted() -> 3. Practical use: Sorting collections with sorted()
snacks = [
    {"name": "Galleta avena", "price": 2500},
    {"name": "Jugo natural en agua", "price": 3000},
    {"name": "Pan de bono", "price": 2000},
    {"name": "Pony Malta", "price": 3500}
]

# Ordenar snacks de menor a mayor precio usando lambda como clave (key) -> Sort snacks from lowest to highest price using lambda as key
cheapest_first = sorted(snacks, key=lambda snack: snack["price"])

print("\n--- Snacks ordenados por precio (Menor a Mayor) ---")
for s in cheapest_first:
    print(f"- {s['name']}: ${s['price']}")

# Truco para recordar:
# def = “Te contrato con papeles” 📄
# lambda = “Hazme este favorcito rápido” 🤝