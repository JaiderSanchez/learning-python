"""
ESCRIBIR UNA FUNCIÓN PARA IMPRIMIR UN MENSAJE DE SALUDO -> WRITE A FUNCTION TO PRINT A GREETING MESSAGE
"""

def greet_user(name: str = "autodidact!") -> None:
    """Imprime un saludo personalizado -> Prints a personalized greeting."""
    print(f"Hi, good day 👋🌤️🙏✅ {name}")


# Capturar nombre o usar el valor predeterminado -> Capture name or use default value
user_name: str = input("Ingresa tu nombre (Enter para 'autodidact!') -> Enter your name (Enter for 'autodidact!'): ").strip()

if user_name:
    greet_user(user_name)
else:
    greet_user()
