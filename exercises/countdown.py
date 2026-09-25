"""Countdown Timer"""

import time  # Importamos la librería nativa para manejar pausas y tiempo

# range(inicio, fin_sin_incluir, paso)
# Empieza en 10, se detiene antes del 0 (en 1) y descuenta 1 en cada ciclo (-1)
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  # Pausa la ejecución del programa durante exactamente 1 segundo

print("¡TIEMPO!")
