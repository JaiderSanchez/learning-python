# 02-custom-modules.py

# Un módulo en Python es simplemente un archivo .py con funciones y variables reutilizables -> A module in Python is simply a .py file with reusable functions and variables
# El bloque if __name__ == "__main__": evita la ejecución accidental al importar -> The if __name__ == "__main__": block prevents accidental execution upon import

# 1. Funciones del módulo utilitario -> 1. Utility module functions
def calculate_vat(amount: float, rate: float = 0.19) -> float:
    """Calcula el IVA de una cifra -> Calculates VAT for an amount."""
    return amount * rate


def format_currency(value: float) -> str:
    """Formatea un número a formato de moneda local -> Formats a number to local currency format."""
    return f"${value:,.2f} COP"


# 2. Bloque de prueba de ejecución directa -> 2. Direct execution test block
if __name__ == "__main__":
    sample_amount: float = 50000.0
    vat_amount: float = calculate_vat(sample_amount)
    total: str = format_currency(sample_amount + vat_amount)

    print(f"Monto base -> Base amount: {format_currency(sample_amount)}")
    print(f"IVA (19%) -> VAT (19%): {format_currency(vat_amount)}")
    print(f"Total con IVA -> Total with VAT: {total}")
