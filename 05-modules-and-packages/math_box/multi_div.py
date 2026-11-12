# math_box/multi_div.py
# Herramientas de multiplicación y división -> Multiplication and division tools

def multiplicar(a: int, b: int) -> int:
    """Multiplica dos números -> Multiplies two numbers."""
    return a * b

def dividir(a: float, b: float) -> float | str:
    """Divide dos números -> Divides two numbers."""
    if b == 0:
        return "Error: No se puede dividir por cero -> Cannot divide by zero"
    return a / b
