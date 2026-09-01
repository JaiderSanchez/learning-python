# Concatenación e impresión de cadenas

##### En Python podemos combinar texto y variables de diferentes maneras.

#####

##### **_cats = 3_**

#####

##### **_print("I have", cats, "cats.")_**

#####

#####

##### Al usar comas, print() recibe varios argumentos y coloca un espacio automáticamente entre ellos. Es una forma sencilla cuando solo necesitamos mostrar varios valores.

##### También podemos usar +, pero debemos asegurarnos de que todos los elementos sean cadenas:

#####

##### **_print("I have " + str(cats) + " cats.")_**

##### Otra alternativa, especialmente útil cuando necesitamos insertar variables o controlar su formato, son los f-strings:

#####

##### **_print(f"I have {cats} cats.")_**

#####

#####

##### Los f-strings suelen ser una opción más completa y profesional para construir cadenas con variables y aplicar formatos.

La razón por la que los f-strings suelen considerarse “más cómodos” es en situaciones donde necesitas controlar el formato, por ejemplo:

name = "Carlos"
age = 25
print(f"{name} tiene {age} años.")

O:
price = 19.9876
print(f"Precio: ${price:.2f}")
Ahí el f-string empieza a resultar mucho más conveniente que concatenar manualmente.

