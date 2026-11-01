# helper_utils.py

# Módulo utilitario personalizado con funciones de ayuda -> Custom utility module with helper functions

def greet_user(name: str) -> str:
    """Genera un saludo personalizado para el usuario -> Generates a personalized greeting for the user."""
    return f"¡Hola, {name}! Bienvenido al módulo de utilidades. -> Hello, {name}! Welcome to the utility module."

def calculate_discount(price: float, discount_percentage: float = 10.0) -> float:
    """Calcula el precio final tras aplicar un porcentaje de descuento -> Calculates the final price after applying a discount percentage."""
    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount

# Bloque de salvaguarda para pruebas locales -> Safeguard block for local testing

if __name__ == "__main__":
    print("=== Prueba local de helper_utils.py -> Local test of helper_utils.py ===")
    print(greet_user("Jaider"))
    print(f"Precio con descuento -> Discounted price: ${calculate_discount(100000, 15):,.2f}")
