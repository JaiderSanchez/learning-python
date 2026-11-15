"""
IMPRIMIR LOS NÚMEROS PARES DEL 2 AL 10 CON EL CICLO FOR -> PRINT EVEN NUMBERS FROM 2 TO 10 USING A FOR LOOP
"""

print("--- Números pares del 2 al 10 -> Even numbers from 2 to 10 ---")

# El tercer argumento de range(inicio, fin, paso) define el incremento de 2 en 2 -> The third argument in range(start, stop, step) sets the increment by 2
for even_number in range(2, 11, 2):
    print(even_number)
