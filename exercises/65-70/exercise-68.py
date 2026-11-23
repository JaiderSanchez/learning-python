"""
ESCRIBIR UNA FUNCIÓN QUE PIDA DISTANCIA Y VELOCIDAD PARA CALCULAR EL TIEMPO DE VIAJE -> WRITE A FUNCTION TO CALCULATE TRAVEL TIME FROM DISTANCE AND SPEED
9"""

def calculate_travel_time() -> float | None:
    """Solicita datos por teclado y retorna el tiempo estimado en horas -> Prompts for data and returns estimated time in hours."""

    try:
        dist_input: str = input("Escribe la distancia en km (Enter para 120) -> Enter distance in km (Enter for 120): ").strip()
        
        speed_input: str = input("Escribe la velocidad en km/h (Enter para 60) -> Enter speed in km/h (Enter for 60): ").strip()

        # Limpiar unidades comunes antes de convertir a float en caso de que el usuario escriba por ejemplo: '120 km' -> Clean up common units before converting to a float, in case the user enters, for example, '120 km'.
        dist_clean: str = dist_input.lower().replace("km", "").strip()
        speed_clean: str = speed_input.lower().replace("km/h", "").replace("km", "").strip()

        distance: float = float(dist_clean) if dist_clean else 120.0
        speed: float = float(speed_clean) if speed_clean else 60.0

        if distance < 0 or speed <= 0:
            print("Error: La distancia no puede ser negativa y la velocidad debe ser mayor a 0 -> Error: Distance cannot be negative and speed must be greater than 0.")
            return None

        return distance / speed
    
    except ValueError:
        print("Error: Ingresa valores numéricos válidos -> Error: Please enter valid numeric values.")
        return None

travel_hours: float | None = calculate_travel_time()

if travel_hours is not None:
    print(f"El tiempo estimado de viaje es -> Estimated travel time is: {travel_hours:.2f} horas / hours")
