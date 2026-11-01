# 03-main-import.py

# Script principal que importa y utiliza funciones del módulo personalizado helper_utils.py -> Main script that imports and uses functions from the custom module helper_utils.py

# 1. Importación específica de funciones -> 1. Specific function imports

from helper_utils import greet_user, calculate_discount

# 2. Importación del módulo completo con alias -> 2. Full module import using an alias
import helper_utils as utils

# Ejecución de funciones importadas -> Execution of imported functions
user_name: str = "Jaider"
product_price: float = 85000.0
discount_rate: float = 12.0

# Usando las funciones importadas directamente -> Using directly imported functions
greeting_message: str = greet_user(user_name)
final_price: float = calculate_discount(product_price, discount_rate)

print("--- Ejecución desde 03-main-import.py -> Execution from 03-main-import.py ---")
print(greeting_message)
print(f"Precio original del producto -> Original product price: ${product_price:,.2f} COP")
print(f"Precio con {discount_rate}% de descuento -> Price with {discount_rate}% discount: ${final_price:,.2f} COP")

# Usando el módulo mediante alias -> Using module via alias
print(f"\nVerificación mediante alias (utils) -> Alias verification (utils):")
print(utils.greet_user("Dev Yopal"))
