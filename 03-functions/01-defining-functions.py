# 01-defining-functions.py

# Una función es un bloque de código reutilizable que realiza una tarea específica. -> A function is a reusable block of code that performs a specific task.
# Se define usando la palabra clave 'def'. -> It is defined using the 'def' keyword.

# 1. Función básica sin parámetros ni retorno -> A basic function without parameters or return value.
def show_welcome_message():
    """Imprime un mensaje de bienvenida al entorno de desarrollo."""
    print("=== Módulo de Funciones en Python 3.12 ===")
    print("Preparando el entorno para desarrollo web remoto...\n")

# Llamada a la función (ejecución)
show_welcome_message()


# 2. Función con valor de retorno (return) 'return' envía el resultado de vuelta a quien invocó la función. -> Function with a return value: 'return' sends the result back to the caller of the function.

def get_official_snack():
    """Devuelve el snack oficial de la sesión de código."""
    return "Pan de queso con Pony Malta"

# Guardamos el resultado devuelto en una variable -> We store the returned result in a variable
snack = get_official_snack()
print(f"Combustible de la sesión: {snack}")


# 3. Diferencia entre print() y return. print() solo muestra texto en pantalla; return entrega un valor utilizable. -> Difference between print() and return: print() only displays text on the screen; return provides a usable value.

def calculate_snack_total(price: int, quantity: int) -> int:
    """Calcula el costo total de la compra."""
    return price * quantity

total_cost = calculate_snack_total(2500, 3)
print(f"Total a pagar en la panadería: ${total_cost}")
