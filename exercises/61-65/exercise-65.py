"""
ESCRIBIR UNA FUNCIÓN PARA CONVERTIR GRADOS CELSIUS A FAHRENHEIT -> WRITE A FUNCTION TO CONVERT CELSIUS TO FAHRENHEIT
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convierte temperatura de °C a °F -> Converts temperature from °C to °F."""
    return (celsius * 9 / 5) + 32


try:
    # Solicitar temperatura en Celsius o usar 30 por defecto -> Request Celsius temperature or use 30 by default
    temp_input: str = input("Ingresa grados Celsius (Enter para 30) -> Enter Celsius degrees (Enter for 30): ").strip()
    celsius_temp: float = float(temp_input) if temp_input else 30.0

    fahrenheit_temp: float = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C equivalen a {fahrenheit_temp:.2f}°F -> {celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")

except ValueError:
    print("Error: Ingresa una temperatura numérica válida -> Error: Please enter a valid numeric temperature.")
