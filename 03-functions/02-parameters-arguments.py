# 02-parameters-arguments.py

# Parámetros: Variables declaradas en la definición de la función. -> Parameters: Variables declared in the function definition.
# Argumentos: Valores reales pasados a la función al llamarla. -> Arguments: Real values passed to the function when calling it.

# 1. Parámetros posicionales y valores por defecto (Default parameters) -> 1. Positional parameters and default values (Default parameters)
def create_player_profile(username: str, level: int = 1, rank: str = "Unranked") -> str:
    """Crea una ficha de jugador en Call of duty Mobile con valores iniciales por defecto."""
    return f"Jugador: {username} | Nivel: {level} | Rango: {rank}"

# Usando solo el parámetro obligatorio (usa los valores por defecto para el resto) -> Using only the mandatory parameter (uses default values for the rest)
player1 = create_player_profile("Gamer_Yopal")
print(player1)

# Sobrescribiendo todos los valores por defecto -> Overriding all default values
player2 = create_player_profile("Sniper_Xx", 15, "Leyenda")
print(player2)


# 2. Argumentos por nombre (Keyword Arguments) 
# Permiten enviar los argumentos en cualquier orden especificando explícitamente el nombre del parámetro. -> 2. Keyword Arguments: Allow sending arguments in any order by explicitly specifying the parameter name.
def calculate_freelance_payout(hours_worked: float, hourly_rate: float, currency: str = "USD") -> str:
    """Calcula el pago estimado para un contrato de desarrollo web remoto."""
    total = hours_worked * hourly_rate
    return f"Pago estimado por el proyecto: {total} {currency}"

# Pasamos los argumentos cambiando el orden usando sus nombres -> We pass the arguments changing the order using their names
payout = calculate_freelance_payout(hourly_rate=25.0, hours_worked=40, currency="USD")
print(payout)
