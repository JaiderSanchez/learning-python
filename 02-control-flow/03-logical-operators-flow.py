# 03-logical-operators-flow.py

# Simplificación de flujo de control usando operadores lógicos (and, or, not). -> Simplification of control flow using logical operators (and, or, not).
# Evita el anidamiento excesivo de bloques 'if'. -> Avoid excessive nesting of 'if' blocks.

has_empanada = True
has_pony_malta = True
is_rainy = True

# 1. Uso de 'and' (Todas las condiciones deben ser True) -> Use of 'and' (All conditions must be True)
# En lugar de usar 2 'if' anidados, lo resolvemos en un solo nivel: -> Instead of using 2 nested 'if', we solve it in a single level:
if has_empanada and has_pony_malta:
    print("¡Combo completo! Tarde ideal para programar en Python.")

# 2. Uso de 'or' (Al menos UNA condición debe ser True) -> Use of 'or' (At least ONE condition must be True)
has_buñuelo = False
has_pan_de_bono = True

if has_buñuelo or has_pan_de_bono:
    print("Tienes un snack para acompañar el tinto.")

# 3. Uso de 'not' (Invierte el valor booleano) -> Use of 'not' (Inverts the boolean value)
# Evalúa si la condición NO es verdadera. -> Evaluates if the condition is NOT true.
if not is_rainy:
    print("El día está despejado, ideal para salir a jugar fútbol.")
else:
    print("Está lloviendo en Yopal, perfecto para quedarse haciendo código.")

# 4. Combinación compleja -> Complex combination
# Evaluación de requisitos para un entorno de trabajo o juego -> Evaluation of requirements for a work or gaming environment
ram_gb = 12
has_gpu = True
is_dev_mode = True

if (ram_gb >= 8 and has_gpu) or is_dev_mode:
    print("El sistema cumple con los requisitos para ejecutar el entorno de desarrollo.")
    