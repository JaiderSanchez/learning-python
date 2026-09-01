# 03-operators.py

# 1. Arithmetic Operators (Operadores Aritméticos)
cats = 3
print("I have", cats, "cats.") # NOTA IMPORTANTE: La coma separa argumentos de print(), '+' concatena strings, por eso, hay controlar manualmente los tipos de datos y los espacios.

# Formas de incrementar el valor de una variable
cats = 3 + 1 # Forma estándar de incrementar el valor de una variable
cats += 4 # Forma abreviada de incrementar el valor de una variable

# Formas de disminuir el valor de una variable
cats = cats - 1 # Forma estándar de disminuir el valor de una variable
cats -= 1 # Forma abreviada de disminuir el valor de una variable

cats = cats * 2 # Forma estándar de multiplicar el valor de una variable
cats *= 2 # Forma abreviada de multiplicar el valor de una variable

cats = cats / 2 # Forma estándar de dividir el valor de una variable
cats /= 2 # Forma abreviada de dividir el valor de una variable

# Explicación importante sobre la división: Si dividimos con '/' nos devuelve un float, si dividimos con '//' nos devuelve un int.

# Módulo
cats = 10
resto = cats % 3 # El operador módulo devuelve el resto de la división
# resto = cats % 2 -> El operador módulo devuelve el resto de la división

# Explicación divisiones
print(cats)
print(resto)



# Practical examples based on certain video games and fast food (Ejemplos prácticos basados en algunos videojuegos y comida rápida.)

# 1. Arithmetic Operators (Operadores Aritméticos)
kills = 45
deaths = 12
kd_ratio = kills / deaths
print(f"Call of Duty K/D Ratio: {kd_ratio}")

# Floor division (//) and Modulo (%)
minutes_played = 135
hours = minutes_played // 60
minutes_left = minutes_played % 60
print(f"Tiempo de juego: {hours}h {minutes_left}m")

# 2. Comparison Operators (Operadores de Comparación)
# Devuelven un valor booleano (True o False)
my_vram_gb = 2
required_vram_gb = 1
can_run_pes = my_vram_gb >= required_vram_gb
print(f"¿Cumple VRAM para PES 2013? {can_run_pes}")

# 3. Logical Operators (Operadores Lógicos: and, or, not)
has_doritos = True
has_salchichon = True
epic_ramen = has_doritos and has_salchichon
print(f"¿Ramen listo con todos los ingredientes extra? {epic_ramen}")

# Combinando operadores
is_ready_to_play = can_run_pes and not (minutes_played > 180)
print(f"¿Listo para otra partida? {is_ready_to_play}")
