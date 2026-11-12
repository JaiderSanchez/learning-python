"""
DESAFÍO FIZZBUZZ DEL 1 AL 100 USANDO BUCLE WHILE -> FIZZBUZZ CHALLENGE FROM 1 TO 100 USING WHILE LOOP
"""

current_number: int = 1

# Iterar del 1 al 100 evaluando divisibilidad -> Iterate from 1 to 100 evaluating divisibility
while current_number <= 100:
    # Evaluar primero el múltiplo común de 3 y 5 -> Evaluate common multiple of 3 and 5 first
    if current_number % 3 == 0 and current_number % 5 == 0:
        print("FizzBuzz")
    elif current_number % 3 == 0:
        print("Fizz")
    elif current_number % 5 == 0:
        print("Buzz")
    else:
        print(current_number)

    current_number += 1
