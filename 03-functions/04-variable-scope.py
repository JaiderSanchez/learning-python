# 04-variable-scope.py

# Alcance Local vs Global y el uso de la palabra clave 'global'. -> Local vs Global Scope and the use of the 'global' keyword.

# 1. Variable Global: Accesible desde cualquier lugar del script -> 1. Global Variable: Accessible from anywhere in the script
app_name = "Yopal Dev Studio"

def display_app_info() -> None:
    # Leemos la variable global dentro de la función -> We read the global variable inside the function
    print(f"Bienvenido a {app_name}")

display_app_info()


# 2. Variable Local: Existe ÚNICAMENTE dentro de la función -> 2. Local Variable: Exists ONLY within the function
def set_session_status() -> None:
    status = "Active"  # Variable local -> Local variable
    print(f"Estado de la sesión interna: {status}")

set_session_status()
# Intentar ejecutar print(status) aquí afuera lanzaría un NameError -> Trying to execute print(status) out here would raise a NameError


# 3. La palabra clave 'global' se usa si necesitamos MODIFICAR una variable global desde el interior de una función. -> 3. The 'global' keyword is used if we need to MODIFY a global variable from within a function.

completed_tasks = 0

def complete_task() -> None:
    global completed_tasks  # Indicamos que modificaremos la variable global -> We indicate that we will modify the global variable
    completed_tasks += 1
    print(f"Tarea completada. Total actual: {completed_tasks}")

complete_task()
complete_task()
