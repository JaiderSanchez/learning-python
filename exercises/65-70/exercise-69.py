"""
ESCRIBIR UNA FUNCIÓN PARA CALCULAR LA TASA DE DESEMPLEO -> WRITE A FUNCTION TO CALCULATE THE UNEMPLOYMENT RATE
Fórmula / Formula: (Desempleados / Fuerza Laboral) * 100
"""

def calculate_unemployment_rate(unemployed: float, labor_force: float) -> float:
    """Calcula el porcentaje de desempleo -> Calculates the unemployment percentage."""
    return (unemployed / labor_force) * 100


try:
    # Solicitar datos o usar 100 y 900 por defecto -> Request data or use 100 and 900 by default
    unemployed_input: str = input("Ingresa el número de desempleados (Enter para 100) -> Enter unemployed count (Enter for 100): ").strip()
    
    force_input: str = input("Ingresa la fuerza laboral total (Enter para 900) -> Enter total labor force (Enter for 900): ").strip()

    unemployed_count: float = float(unemployed_input) if unemployed_input else 100.0
    total_force: float = float(force_input) if force_input else 900.0

    if total_force <= 0 or unemployed_count < 0:
        print("Error: La fuerza laboral debe ser mayor a 0 y los desempleados no pueden ser negativos -> Error: Labor force must be > 0 and unemployed cannot be negative.")
    elif unemployed_count > total_force:
        print("Error: El número de desempleados no puede superar la fuerza laboral total -> Error: Unemployed count cannot exceed total labor force.")
    else:
        rate: float = calculate_unemployment_rate(unemployed_count, total_force)
        print(f"La tasa de desempleo es -> The unemployment rate is: {rate:.2f}%")

except ValueError:
    print("Error: Ingresa únicamente valores numéricos válidos -> Error: Please enter valid numeric values only.")
