# 02-nested-if.py

# Los condicionales anidados nos permiten evaluar reglas secundarias -> Nested conditionals allow us to evaluate secondary rules.
# SOLO SI la regla principal ya se cumplió. -> ONLY IF the main rule has already been met.

is_store_open = True
budget = 4500
has_empanadas = True

# Puerta principal: Validar si el lugar está abierto -> Main gate: Validate if the place is open
if is_store_open:
    print("La panadería está abierta. Entrando...")
    
    # Puertas secundarias (Anidadas): Tienen 4 espacios extra de indentación -> Secondary gates (Nested): They have 4 extra spaces of indentation.
    if budget >= 4000:
        if has_empanadas:
            print("¡Bingo! Comprando combo de empanada y Pony Malta.")
        else:
            print("Tengo el dinero, pero se acabaron las empanadas. Llevaré un Chocoramo.")
    else:
        print("El presupuesto no alcanza, mejor llevo solo un pan de queso.")
        
else:
    # Si la puerta principal es False, el programa salta directo hasta aquí -> If the main gate is False, the program jumps straight here.
    print("La panadería está cerrada. No hay snacks hoy.")
