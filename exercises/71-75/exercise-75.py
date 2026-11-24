"""
CREAR UNA CLASE COCHE CON MÉTODO PARA AVANZAR KILOMETRAJE -> CREATE A CAR CLASS WITH METHOD TO INCREASE MILEAGE
"""

class Car:
    def __init__(self, brand: str, model: str, plate: str, km: float) -> None:
        self.brand = brand
        self.model = model
        self.plate = plate
        self.km = km

    def drive(self, extra_km: float) -> None:
        """Aumenta el kilometraje si el valor es positivo -> Increases mileage if value is positive."""
        if extra_km > 0:
            self.km += extra_km
        else:
            print("Aviso: Los kilómetros a avanzar deben ser mayores a 0 -> Warning: Kilometers to drive must be greater than 0.")


try:
    car1 = Car("Ford", "Fiesta", "ABC 123", 5000.0)
    print(f"Estado inicial -> Initial state: {car1.__dict__}")

    km_input: str = input("¿Cuántos km avanzará el coche? (Enter para 3000) -> How many km will the car drive? (Enter for 3000): ").strip()
    added_km: float = float(km_input) if km_input else 3000.0

    car1.drive(added_km)
    print(f"Estado actualizado -> Updated state: {car1.__dict__}")

except ValueError:
    print("Error: Ingresa una cantidad válida de kilómetros -> Error: Please enter a valid number of kilometers.")
