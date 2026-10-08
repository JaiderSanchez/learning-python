# 07-nested-loops.py

# Bucles anidados (bucle dentro de bucle) y el uso de 'pass'. -> Nested loops (loop inside a loop) and the use of 'pass'.

# 1. Bucles anidados: Tabla de posiciones / Rondas -> Nested loops: Standings table / Rounds
players = ["Sniper_Xx", "Gamer_Yopal"]
match_days = ["Sábado", "Domingo"]

print("--- Torneo de Fin de Semana ---")

for day in match_days:
    print(f"=== Día de juego: {day} ===")
    for player in players:
        # Por cada día, recorremos la lista completa de jugadores -> For each day, we traverse the complete list of players
        print(f"  -> Jugador {player} listo en la sala.")


# 2. La palabra clave 'pass' (Null statement) -> The 'pass' keyword (Null statement)
# Se usa cuando la sintaxis de Python requiere un bloque de código,
# pero aún no queremos programar la lógica (placeholder futuro).
is_feature_in_development = True

if is_feature_in_development:
    # 'pass' evita que Python lance un error por dejar el 'if' vacío -> 'pass' prevents Python from throwing an error for leaving the 'if' empty
    pass 

for i in range(5):
    if i == 3:
        pass  # Pendiente implementar lógica de guardado aquí -> Pending implementation of save logic here
    else:
        print(i)

# Este programa organiza un pequeño torneo recorriendo cada día → cada jugador, y luego muestra cómo usar pass cuando todavía no quieres poner ninguna acción dentro de un bloque de código.
