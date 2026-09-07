# 09-f-strings.py

# Las f-strings son la forma más moderna y limpia de armar textos en Python. -> f-strings are the most modern and cleanest way to construct strings in Python.
# Solo necesitas poner una 'f' antes de las comillas. -> You just need to put an 'f' before the quotation marks.

# 1. Inyección básica de variables -> Basic variable injection
cpu = "Intel Core i5"
gpu = "NVIDIA Geforce MX330"
ram = 12

print(f"Mi laptop tiene un procesador {cpu}, una tarjeta gráfica {gpu} y {ram} GB de RAM.")

# 2. Matemáticas directamente dentro de las llaves -> Mathematics directly inside the braces
# No es necesario hacer el cálculo afuera y guardarlo en otra variable, Python lo resuelve adentro. -> You don't need to perform the calculation externally and store it in another variable; Python handles it internally.
print(f"Si logro ampliar la memoria al doble, tendré {ram * 2} GB de RAM.")

# 3. Formateo de números (Controlar los decimales) -> Number formatting (controlling decimal places)
# El truco ':.2f' le dice a Python que solo muestre 2 números después del punto. -> The ':.2f' trick tells Python to display only two digits after the decimal point.
win_rate = 55.678912
print(f"Porcentaje de victorias actual: {win_rate:.2f}%")
