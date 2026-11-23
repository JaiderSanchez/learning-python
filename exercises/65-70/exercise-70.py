"""
ESCRIBIR UNA FUNCIÓN PARA CLASIFICAR SI UNA SUSTANCIA ES ÁCIDA, BÁSICA O NEUTRA SEGÚN SU pH -> WRITE A FUNCTION TO CLASSIFY A SUBSTANCE AS ACIDIC, BASIC, OR NEUTRAL BY pH
"""

def classify_substance_ph(ph_level: float) -> str:
    """Clasifica el nivel de pH en escala estándar (0 a 14) -> Classifies pH level on standard scale (0 to 14)."""
    if ph_level < 7:
        return "Ácida -> Acidic"
    elif ph_level > 7:
        return "Básica (Alcalina) -> Basic (Alkaline)"
    else:
        return "Neutra -> Neutral"


try:
    # Solicitar valor de pH o usar 7 por defecto -> Request pH value or use 7 by default
    ph_input: str = input("Ingresa el valor de pH de 0 a 14 (Enter para 7) -> Enter pH value from 0 to 14 (Enter for 7): ").strip()
    
    ph_value: float = float(ph_input) if ph_input else 7.0

    if ph_value < 0 or ph_value > 14:
        print("Aviso: El valor está fuera de la escala estándar de pH (0 a 14) -> Warning: Value is outside the standard pH scale (0 to 14).")
    else:
        classification: str = classify_substance_ph(ph_value)
        print(f"Una sustancia con pH {ph_value} es -> A substance with pH {ph_value} is: {classification}")

except ValueError:
    print("Error: Ingresa un valor numérico válido para el pH -> Error: Please enter a valid numeric value for pH.")
