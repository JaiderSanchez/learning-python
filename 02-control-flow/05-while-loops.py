# 05-while-loops.py

# El bucle 'while' (mientras) ejecuta un bloque de código -> The 'while' loop executes a block of code.
# MIENTRAS una condición sea True. Es como un 'if' que se repite. -> WHILE a condition is True. It's like an 'if' statement that repeats.

# 1. Bucle básico con condición de parada -> 1. Basic loop with a stopping condition
# Regla de oro: Siempre debemos modificar la variable de control dentro del bucle para evitar un bucle infinito. -> Golden rule: We must always modify the control variable inside the loop to avoid an infinite loop.

hp = 20
print("--- Recargando salud ---")

while hp < 100:
    hp += 20  # Aumentamos la salud en cada ciclo -> We increase health in each cycle
    print(f"Salud actual: {hp} HP")

print("¡Salud al máximo! Listo para la partida.\n")


# 2. Uso de 'break' (Salir del bucle inmediatamente) -> 2. Use of 'break' (Exit the loop immediately)
# Interrumpe la ejecución del bucle sin importar si la condición sigue siendo True. -> Interrupts the execution of the loop regardless of whether the condition is still True.
budget = 100000
mazorcada_price = 30000
mazorcadas_bought = 0

print("--- Comprando en la cafetería ---")
while budget >= mazorcada_price:
    mazorcadas_bought += 1
    budget -= mazorcada_price
    print(f"Mazorcada #{mazorcadas_bought} comprada. Dinero restante: ${budget}")
    
    if mazorcadas_bought == 3:
        print("¡Ya es suficiente por hoy! Deteniendo compras.")
        break  # Forzamos la salida del bucle


# 3. Uso de 'continue' (Saltar a la siguiente iteración) -> 3. Use of 'continue' (Skip to the next iteration)
# Omite el resto del código en el ciclo actual y vuelve arriba a evaluar la condición. -> Skips the rest of the code in the current cycle and goes back up to evaluate the condition.
counter = 0

print("\n--- Contando solo números impares ---")
while counter < 5:
    counter += 1
    if counter % 2 == 0:
        continue  # Si el número es par, ignora el print y vuelve al 'while'
    
    print(f"Número impar: {counter}")
