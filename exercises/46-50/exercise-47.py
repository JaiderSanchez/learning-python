"""
CREAR UN MENÚ DE OPCIONES INTERACTIVO CON OPCIÓN DE SALIDA -> CREATE AN INTERACTIVE OPTIONS MENU WITH AN EXIT OPTION
"""

while True:
    print("\n=== MENÚ PRINCIPAL -> MAIN MENU ===")
    print("1. Mostrar saludo -> Show greeting")
    print("2. Mostrar información del sistema -> Show system info")
    print("3. Salir del programa -> Exit program")

    try:
        option: int = int(input("Ingresa una opción (1-3) -> Enter an option (1-3): ").strip())

        if option == 1:
            print("-> ¡Hola! Bienvenido al menú interactivo en Python -> Hello! Welcome to the Python interactive menu.")
        elif option == 2:
            print("-> Estado: Ejecutando Python 3.12 correctamente -> Status: Running Python 3.12 smoothly.")
        elif option == 3:
            print("-> Saliendo del programa... -> Exiting program...")
            break
        else:
            print("Opción inválida. Ingresa un número entre 1 y 3 -> Invalid option. Enter a number between 1 and 3.")

    except ValueError:
        print("Error: Debes ingresar un número válido -> Error: You must enter a valid number.")

print("Programa finalizado -> Program finished.")
