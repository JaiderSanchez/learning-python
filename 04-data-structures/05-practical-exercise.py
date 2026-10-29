# 05-practical-exercise.py

# Ejercicio integrador de estructuras de datos nativas -> Integrated exercise of native data structures

# 1. TUPLA: Ubicación fija e inmutable del negocio (Latitud, Longitud) -> TUPLE: Fixed and immutable business location (Latitude, Longitude)
store_location: tuple[float, float] = (5.3378, -72.3959)

# 2. SET: Categorías únicas disponibles sin duplicados -> SET: Unique available categories without duplicates
categories: set[str] = {"Snacks", "Bebidas", "Apanados"}

# 3. DICCIONARIOS: Catálogo de productos con detalles completos -> DICTIONARIES: Product catalog with complete details
catalog: dict[str, dict[str, float | str]] = {
    "P01": {"name": "Empanada", "price": 2500, "category": "Apanados"},
    "P02": {"name": "Pony Malta", "price": 1800, "category": "Bebidas"},
    "P03": {"name": "Chocoramo", "price": 2000, "category": "Snacks"}
}

# 4. LISTA: Historial dinámico de pedidos realizados -> LIST: Dynamic order history
orders_history: list[dict[str, str | int]] = [
    {"order_id": 101, "product_code": "P01", "quantity": 2},
    {"order_id": 102, "product_code": "P02", "quantity": 1}
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
    product_name = product_info.get("name", "Desconocido")
    unit_price = float(product_info.get("price", 0.0))
    
    subtotal = unit_price * qty
    total_revenue += subtotal
    
    print(f"Pedido #{order['order_id']}: {qty}x {product_name} | Subtotal: ${subtotal} COP")

print(f"\nIngresos totales generados: ${total_revenue} COP")
