# 04-match-case.py

# match-case' es la forma moderna en Python (>= 3.10) para evaluar múltiples valores posibles de una variable sin usar 'elif' repetitivos. -> 'match-case' is the modern way in Python (versions >= 3.10) to evaluate multiple possible values ​​of a variable without using repetitive 'elif' statements.


# 1. Ejemplo básico: Selección de estado/rol -> 1. Basic example: State/role selection

user_role = "developer"

match user_role:
    case "admin":
        print("Acceso total al sistema y la base de datos.")
    case "developer":
        print("Acceso a repositorios de código y entornos de prueba.")
    case "guest":
        print("Acceso limitadoa solo lectura.")
    case _:
        # El guion (_) actúa como el caso por defecto (default / else)
        print("Rol no reconocido. Acceso denegado.")

# 2. Combinando múltiples opciones en un solo 'case' usando '|' (OR)
snack = "Pera + Jugo bajo en azúcar"

match snack:
    case "Pera + Jugo bajo en azúcar" | "Yogurt natural + galletas integrales":
        print("Snack delicioso y saludable.")
    case "Empanada":
        print("Snack no saludable.")
    case _:
        print("Snack no registrado en el menú.")

# 3. Match con condiciones (Guard Clauses)
# Podemos agregar una condición 'if' dentro del mismo case.
http_code = 404

match http_code:
    case 200:
        print("200 OK: Solicitud exitosa.")
    case 404:
        print("404 Not Found: El recurso solicitado no existe.")
    case code if code >= 500:
        print(f"{code} Server Error: Ocurrió un error en el servidor.")
    case _:
        print("Código HTTP no clasificado.")
    