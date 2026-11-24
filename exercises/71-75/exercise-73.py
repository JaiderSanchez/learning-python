"""
CREAR UNA CLASE LIBRO CON CONSTRUCTOR DE ATRIBUTOS -> CREATE A BOOK CLASS WITH ATTRIBUTE CONSTRUCTOR
"""

class Book:
    def __init__(self, title: str, author: str, publisher: str, publication_year: int) -> None:
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year


# Permitir entrada rápida o cargar el libro predeterminado -> Allow quick input or load default book
title_in: str = input("Título del libro (Enter para 'Cien años de soledad') -> Book title (Enter for default): ").strip()
author_in: str = input("Autor (Enter para 'Gabriel García Márquez') -> Author (Enter for default): ").strip()
publisher_in: str = input("Editorial (Enter para 'Editorial Sudamericana') -> Publisher (Enter for default): ").strip()
year_in: str = input("Año de publicación (Enter para 1967) -> Publication year (Enter for 1967): ").strip()

try:
    year_val: int = int(year_in) if year_in else 1967

    my_book = Book(
        title=title_in if title_in else "Cien años de soledad",
        author=author_in if author_in else "Gabriel García Márquez",
        publisher=publisher_in if publisher_in else "Editorial Sudamericana - Buenos Aires, Argentina",
        publication_year=year_val
    )

    print("\nDatos del objeto en diccionario -> Object data dictionary:")
    print(my_book.__dict__)

except ValueError:
    print("Error: El año de publicación debe ser un número entero -> Error: Publication year must be an integer.")
