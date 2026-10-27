"""
REEMPLAZAR UN CARÁCTER O TEXTO EN UNA CADENA -> REPLACE A CHARACTER OR TEXT IN A STRING
"""

# Entrada de texto base o valor por defecto -> Base text input or default value
user_text = input("Ingresa un texto (o presiona Enter para usar el valor predeterminado) -> Enter text (or press Enter for default): ").strip()

if not user_text:
    user_text = "NFS: The Run"

target = input("Texto o carácter a buscar -> Text or character to search for: ").strip()
replacement = input("Texto de reemplazo -> Replacement text: ").strip()

# Reemplazo dinámico de subcadena -> Dynamic substring replacement
if target:
    updated_text = user_text.replace(target, replacement)
else:
    # Ejemplo predeterminado si no se especifica búsqueda -> Default example if search target is empty
    updated_text = user_text.replace("The Run", "Most Wanted 2012")

print(f"Texto original -> Original text: {user_text}")
print(f"Texto actualizado -> Updated text: {updated_text}")
