# 03-sets.py

# Los conjuntos (sets) son colecciones no ordenadas de elementos únicos -> Sets are unordered collections of unique elements
# Se definen usando llaves {} o la función set() -> They are defined using curly braces {} or the set() function

# 1. Creación y eliminación de duplicados -> 1. Creation and removal of duplicates
# Python elimina automáticamente los valores repetidos -> Python automatically removes duplicate values
raw_player_ids: list[int] = [101, 102, 101, 103, 104, 102]
unique_players: set[int] = set(raw_player_ids)
print(f"Jugadores únicos en la sala: {unique_players}")

# 2. Agregar y eliminar elementos -> 2. Adding and removing elements
available_snacks: set[str] = {"Jugo mora agua", "Mogolla integral", "Galletas Oreo", "Buñuelo"}

# Agregar un elemento (.add) -> Add an element (.add)
available_snacks.add("Pony Malta")

# Eliminar sin lanzar error si no existe (.discard) -> Remove without raising an error if absent (.discard)
available_snacks.discard("Buñuelo")
print(f"Snacks disponibles hoy: {available_snacks}") # Como los sets no tienen orden, en consola los snacks pueden salir en otro orden, e incluso cambiar cada vez que ejecutes el programa. Since sets are unordered, the snacks may appear in a different order in the console and might even change each time you run the program.

# 3. Operaciones matemáticas de conjuntos -> 3. Mathematical set operations
yopal_devs: set[str] = {"Python", "Git", "SQL", "Tkinter"}
remote_job_reqs: set[str] = {"Python", "Git", "Docker", "REST API"}

# Intersección (&): Habilidades que coinciden -> Intersection (&): Matching skills
matching_skills = yopal_devs & remote_job_reqs
print(f"Habilidades que cumples para la vacante: {matching_skills}")

# Unión (|): Todas las habilidades combinadas sin repetir -> Union (|): All combined skills without duplicates
all_skills = yopal_devs | remote_job_reqs # Mezcla los dos círculos en uno solo. Python y Git estaban en ambos, pero solo aparecen una vez. -> Combine the two circles into one. Python and Git were in both, but they appear only once.
print(f"Habilidades totales combinadas: {all_skills}")

missing = remote_job_reqs - yopal_devs   # {'Docker', 'REST API'}
print(f"Habilidades qué faltan por aprender: {missing}")

# IMPORTANTE: {} Vacías no crean un set, crean un diccionario. Para un set vacío se usa set(). -> Empty braces do not create a set; they create a dictionary. To create an empty set, use `set()`.
