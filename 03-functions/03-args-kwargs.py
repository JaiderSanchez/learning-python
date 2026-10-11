# 03-args-kwargs.py

# *args (Arbitrary Arguments): Permite recibir múltiples argumentos posicionales en una tupla. -> *args (Arbitrary Arguments): Allows receiving multiple positional arguments in a tuple.
# **kwargs (Keyword Arguments): Permite recibir múltiples argumentos por nombre en un diccionario. -> **kwargs (Keyword Arguments): Allows receiving multiple named arguments in a dictionary.

# 1. Uso de *args (Tupla de elementos) -> 1. Using *args (Tuple of elements)
def calculate_total_expenditure(*prices: float) -> float:
    """Calcula el costo total de un número indefinido de productos comprados."""
    # 'prices' es una tupla con todos los valores pasados -> 'prices' is a tuple with all the passed values
    return sum(prices)

# Podemos pasar 2, 3 o la cantidad de snacks que queramos -> We can pass 2, 3, or as many snacks as we want
total_1 = calculate_total_expenditure(2500, 1800)
total_2 = calculate_total_expenditure(2500, 1800, 3000, 1200)

print(f"Gasto sesión 1: ${total_1}")
print(f"Gasto sesión 2: ${total_2}")


# 2. Uso de **kwargs (Diccionario clave-valor) -> 2. Using **kwargs (Key-value dictionary)
def build_remote_setup(**components: str) -> None: # Los dos asteriscos ** son como una caja con casilleros con nombre. Cada dato llega como pareja etiqueta = valor (processor="Intel Core i5"). components es un diccionario: como un cuaderno donde cada página tiene un título y su contenido. -> The two asterisks ** are like a box with labeled compartments. Each piece of data arrives as a label=value pair (processor="Intel Core i5"). components is a dictionary: like a notebook where each page has a title and its content.
    """Muestra la configuración del entorno de trabajo pasando parámetros dinámicos."""
    print("\n--- Entorno de Trabajo Configurado ---")
    for key, value in components.items():
        print(f"{key.capitalize()}: {value}") # capitalize() convierte la primera letra en mayúscula -> capitalize() converts the first letter to uppercase

# Pasamos argumentos clave=valor arbitrarios -> We pass arbitrary key=value arguments
build_remote_setup(processor="Intel Core i5", ram="12 GB", gpu="NVIDIA MX330", os="Windows 11")
