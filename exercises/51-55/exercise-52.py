"""
SUMAR LOS NÚMEROS DEL 1 AL 10 CON EL CICLO FOR -> SUM NUMBERS FROM 1 TO 10 USING A FOR LOOP
"""

total_sum: int = 0

# Iteración acumulativa usando el operador += -> Cumulative iteration using the += operator
for number in range(1, 11):
    total_sum += number

print(f"La suma de los números del 1 al 10 es -> The sum of numbers from 1 to 10 is: {total_sum}")

# Alternativa idiomática en una línea -> One-line Pythonic alternative:
# total_sum = sum(range(1, 11))
