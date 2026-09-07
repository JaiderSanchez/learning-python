# 10-numbers.py

# Herramientas nativas para manejar números -> Native tools for handling numbers

# 1. Redondear (round)
ping_latency = 45.8
print(f"Ping redondeado para mostrar en pantalla: {round(ping_latency)} ms")

# 2. Valores absolutos (abs) -> Absolute values (abs)
# Siempre devuelve el número en positivo. Útil para medir distancias en un mapa. -> Always returns the number as positive. Useful for measuring distances on a map.
posicion_enemigo = -15
print(f"Distancia real al objetivo: {abs(posicion_enemigo)} metros")

# 3. Máximo y Mínimo (max, min)
# Encuentra rápidamente el valor más alto o más bajo en un grupo de números. -> Quickly finds the highest or lowest value in a group of numbers.
danio_m4 = 32
danio_ak47 = 40
danio_sniper = 95

mejor_arma = max(danio_m4, danio_ak47, danio_sniper)
peor_arma = min(danio_m4, danio_ak47, danio_sniper)
print(f"El daño letal máximo es de {mejor_arma} y el mínimo de {peor_arma}.")

# 4. Importar la librería Math (Poderes avanzados) -> Import the Math library (Advanced powers)
import math

# math.ceil() siempre redondea hacia ARRIBA (al entero siguiente) -> math.ceil() always rounds UP (to the next integer)
# math.floor() siempre redondea hacia ABAJO (al entero anterior) -> math.floor() always rounds DOWN (to the previous integer)
partidas_necesarias = 2.1
print(f"Como no puedes jugar 0.1 partidas, necesitas jugar {math.ceil(partidas_necesarias)} para subir de rango.")
