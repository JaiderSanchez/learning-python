# 05-practical-exercise.py

# Ejercicio integrador de estructuras de datos nativas -> Integrated exercise of native data structures

# 1. TUPLA: Ubicación fija e inmutable del negocio (Latitud, Longitud) -> TUPLE: Fixed and immutable business location (Latitude, Longitude)
store_location: tuple[float, float] = (5.3378, -72.3959)

# 2. SET: Categorías únicas disponibles sin duplicados -> SET: Unique available categories without duplicates
categories: set[str] = {"Snacks", "Bebidas", "Frutas"}

# 3. DICCIONARIOS: Catálogo de productos con detalles completos -> DICTIONARIES: Product catalog with complete details
catalog: dict[str, dict[str, float | str]] = {
    "P01": {"name": "Manzana", "price": 2500, "category": "Frutas"},
    "P02": {"name": "Pony Malta", "price": 3000, "category": "Bebidas"},
    "P03": {"name": "Chocoramo", "price": 2600, "category": "Snacks"},
    "P04": {"name": "Pera", "price": 2500, "category": "Frutas"},
    "P05": {"name": "Avena Alpina Bolsa", "price": 2000, "category": "Snacks"}
}

# 4. LISTA: Historial dinámico de pedidos realizados -> LIST: Dynamic order history
orders_history: list[dict[str, str | int]] = [
    {"order_id": 101, "product_code": "P01", "quantity": 2},
    {"order_id": 102, "product_code": "P02", "quantity": 1},
    {"order_id": 103, "product_code": "P05", "quantity": 3},
    {"order_id": 104, "product_code": "P04", "quantity": 2},
    {"order_id": 105, "product_code": "P01", "quantity": 2}
]

# --- PROCESAMIENTO E INTEGRACIÓN ---
print(f"=== Sede Principal | Coordenadas: {store_location} ===")
print(f"Categorías activas: {categories}\n")

# Calcular el total del historial de ventas -> Calculate total sales history
total_revenue = 0.0

print("--- Resumen de Pedidos Procesados ---")
for order in orders_history:
    code = str(order["product_code"])
    qty = int(order["quantity"])
    
    # Obtenemos la información del producto buscando por su clave en el diccionario -> Get product information by key lookup
    product_info = catalog.get(code, {})

    # Paso 3: Sacar el nombre y el precio de la ficha -> Step 3: Extract the name and price from the product page
    product_name = product_info.get("name", "Desconocido") # Si el producto existe → toma su nombre y precio real. -> If the product exists → take its name and actual price.
    unit_price = float(product_info.get("price", 0.0)) # Si no existe → nombre "Desconocido" y precio 0.0. -> If it does not exist → name "Unknown" and price 0.0.

    # Paso 4: Hacer la cuenta -> Step 4: Do the calculation
    subtotal = unit_price * qty # precio × cantidad. -> price × quantity.
    total_revenue += subtotal # echa ese dinero a la alcancía -> Put that money in the piggy bank.

    # Paso 5: Imprimir el recibo -> Step 5: Print the receipt
    print(f"Pedido #{order['order_id']}: {qty}x {product_name} | Subtotal: ${subtotal} COP")

print(f"\nIngresos totales generados: ${total_revenue} COP")
