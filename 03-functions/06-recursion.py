# 06-recursion.py

# La recursividad es cuando una función se invoca a sí misma. -> Recursion is when a function calls itself.

# 1. Ejemplo 1: Cuenta regresiva recursiva -> 1. Example 1: Recursive Countdown
def recursive_countdown(number: int) -> None:
    """Realiza una cuenta regresiva imprimiendo cada número usando recursividad."""
    # Caso Base (Condición de parada) -> Base Case (Stopping Condition)
    if number <= 0:
        print("¡Despegue! Entorno listo para programar.")
        return
    
    print(f"Tiempo restante: {number}s")
    
    # Caso Recursivo (nos acercamos al caso base restando 1) -> Recursive Case (we approach the base case by subtracting 1)
    recursive_countdown(number - 1)

print("--- Prueba de Recursividad: Cuenta Regresiva ---")
recursive_countdown(3)


# 2. Ejemplo 2: Cálculo de Factorial (5! = 5 * 4 * 3 * 2 * 1 = 120) -> 2. Example 2: Factorial Calculation (5! = 5 * 4 * 3 * 2 * 1 = 120)
def calculate_factorial(n: int) -> int:
    """Calcula el factorial de un número entero positivo."""
    # Caso Base -> Base Case
    if n == 0 or n == 1:
        return 1
    
    # Caso Recursivo -> Recursive Case
    return n * calculate_factorial(n - 1)

number_to_test = 5
result = calculate_factorial(number_to_test)
print(f"\nEl factorial de {number_to_test} es: {result}")
