"""
CREAR UNA CLASE PERSONA Y VERIFICAR MAYORÍA DE EDAD -> CREATE A PERSON CLASS AND CHECK LEGAL AGE
"""

class Person:
    def __init__(self, name: str, age: int, dni: str) -> None:
        self.name = name
        self.age = age
        self.dni = dni

    def is_adult(self) -> bool:
        """Retorna True si tiene 18 años o más, False en caso contrario -> Returns True if 18 or older, False otherwise."""
        return self.age >= 18

    def __str__(self) -> str:
        """Define cómo se muestra el objeto al imprimirlo directamente -> Defines how the object displays when printed directly."""
        return f"Nombre: {self.name} | Edad: {self.age} | DNI: {self.dni}"


try:
    name_in: str = input("Ingresa el nombre (Enter para 'Jose') -> Enter name (Enter for 'Jose'): ").strip()
    age_in: str = input("Ingresa la edad (Enter para 20) -> Enter age (Enter for 20): ").strip()
    dni_in: str = input("Ingresa el DNI (Enter para 'QUERTY') -> Enter DNI (Enter for 'QUERTY'): ").strip()

    person1 = Person(
        name=name_in if name_in else "Jose",
        age=int(age_in) if age_in else 20,
        dni=dni_in if dni_in else "QUERTY"
    )

    print(f"\nEl nombre es -> Name is: {person1.name}")

    # Uso de __str__ dentro del print para mostrar todos sus datos -> Using __str__ inside print to display all data
    if person1.is_adult():
        print(f"La persona es mayor de edad -> Person is an adult: [{person1}]")
    else:
        print(f"La persona es menor de edad -> Person is a minor: [{person1}]")

except ValueError:
    print("Error: La edad debe ser un número entero válido -> Error: Age must be a valid integer.")
