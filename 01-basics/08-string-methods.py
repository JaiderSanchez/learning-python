# 08-string-methods.py

# Los métodos son acciones que un tipo de dato puede hacerse a sí mismo. str.upper(), str.lower(), str.strip(), etc. -> Methods are actions that a data type can perform on itself.
# Se activan poniendo un punto (.) justo después de la variable. -> They are activated by placing a dot (.) right after the variable.

username = "  xX_Sniper_Xx  "
loadout = "M4,AK-47,Francoritador,Granada"
snack_status = "El snack incluye galletas Oreo"

# 1. Limpiar espacios extra (.strip) -> 1. Remove extra spaces (.strip)
# Quita los espacios invisibles al principio y al final. -> Remove invisible spaces at the beginning and end.
# Muy útil cuando tecleas rápido y dejas espacios sin querer al hacer login. -> Very useful when you type quickly and leave spaces unintentionally when logging in.
clean_user = username.strip()
print(f"Original: '{username}'")
print(f"Limpio: '{clean_user}'")

# 2. Mayúsculas y Minúsculas (.upper y .lower) -> 2. Uppercase and Lowercase (.upper and .lower)
# Es como gritar o susurrar en el chat de la partida. -> It's like shouting or whispering in the game chat.
print(f"Gritando: {clean_user.upper()}")
print(f"Susurrando: {clean_user.lower()}")

# 3. Reemplazar palabras (.replace) -> 3. Replace words (.replace)
# Buscamos una parte específica del texto y la cambiamos por otra. -> We look for a specific part of the text and change it to another.
epic_snack = snack_status.replace("Avena Alpina", "Ponqué Bimbo")
print(epic_snack)

# 4. Cortar un texto y convertirlo en una lista (.split) -> 4. Cut a text and convert it into a list (.split)
# Rompe el texto como si fuera un bloque de Lego cada vez que encuentra una coma (,).
weapons_list = loadout.split(",")
print(f"Inventario separado en cajas: {weapons_list}")

# 5. Comprobar si empieza o termina con algo (.startswith / .endswith) -> 5. Check if it starts or ends with something (.startswith / .endswith)
# Devuelve un Booleano (True o False). Útil para revisar nombres de archivos. -> Returns a Boolean (True or False). Useful for checking file names.
file_name = "gameplay_codmobile.mp4"
is_video = file_name.endswith(".mp4")
print(f"¿El archivo es un video? {is_video}")
