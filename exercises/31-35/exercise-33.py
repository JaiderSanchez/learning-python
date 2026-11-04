"""
DETERMINAR SI UN AÑO ES BISIESTO -> DETERMINE IF A YEAR IS A LEAP YEAR
Regla de negocio -> Business rule:
    - Divisible entre 4 y no divisible entre 100 -> Divisible by 4 and not divisible by 100
    - O divisible entre 400 -> Or divisible by 400
"""

try:
    user_input = input("Introduce un año (ej. 2024, 2026) -> Enter a year (e.g. 2024, 2026): ").strip()
    year = int(user_input) if user_input else 2024

    # Evaluación de la condición lógica de año bisiesto -> Evaluation of leap year logical condition
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if is_leap_year:
        print(f"El año {year} es bisiesto -> The year {year} is a leap year")
    else:
        print(f"El año {year} no es bisiesto -> The year {year} is not a leap year")

except ValueError:
    print("Error: Ingresa un año válido en formato numérico -> Error: Please enter a valid year in numeric format")
