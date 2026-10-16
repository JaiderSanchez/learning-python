import tkinter as tk
from tkinter import font
from config import constants as cons
import util.window_util as window_util


class FormCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.build_widget()

    def config_window(self):
        # Configuración inicial de la ventana -> Initial window configuration
        self.title("Python GUI Calculadora")
        # Configurar el color de fondo y hacer transparente la ventana -> Configure background color and set window transparency
        self.configure(bg=cons.COLOR_DE_FONDO_DARK)
        self.attributes('-alpha', 0.95) # Ayuda a generar una transparencia en la ventana -> Helps generate window transparency
        w, h = 370, 570 # Valor del ancho y alto de la ventana -> Window width and height values
        window_util.centrar_ventana(self, w, h)

    def build_widget(self): # Un Widget es un componente visual e interactivo que permite al usuario interactuar con un programa mediante una interfaz gráfica (GUI, Graphical User Interface). Por ejemplo, un botón, una caja de texto, una lista desplegable o una casilla de verificación son widgets. -> A Widget is a visual and interactive component that allows the user to interact with a program through a graphical user interface (GUI). For example, a button, a text box, a dropdown list, or a checkbox are widgets.

        # PRIMER WIDGET: Etiqueta para mostrar la operación solicitada -> FIRST WIDGET: Label to display the requested operation
        self.operation_label = tk.Label(self, text="", font=('Arial', 16), fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_DE_FONDO_DARK, justify='right')
        self.operation_label.grid(
            row=0, column=3, padx=10, pady=10 # Añadido columnspan -> Added columnspan
        )

        # SEGUNDO WIDGET: Pantalla de operación -> SECOND WIDGET: Operation display
        self.entry = tk.Entry(self, width=12, font=('Arial', 40), bd=0, fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_CAJA_TEXTO_DARK, justify='right')
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10) # Añadido padding -> Added padding

        # Lista de botones -> Button list
        buttons = [
            'C', '%', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=',
        ]

        row_val = 2 # Ajustando para dejar espacio para la etiqueta de operación -> Adjusting to leave space for the operation label
        col_val = 0

        # Configurar la tipografía "Roboto" para los botones -> Configure "Roboto" font for the buttons
        roboto_font = font.Font(family="Roboto", size=16)

        for button in buttons:
            if button in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                color_fondo = cons.COLOR_BOTONES_ESPECIALES_DARK
                # Adjuntar el tamaño de la fuente solo para estos botones -> Set font size only for these buttons
                button_font = roboto_font
            else:
                color_fondo = cons.COLOR_BOTONES_DARK
                button_font = roboto_font

            tk.Button(
                self, text=button, width=5, height=2,
                bg=color_fondo, fg=cons.COLOR_CAJA_TEXTO_DARK, relief=tk.FLAT,
                font=button_font, padx=5, pady=5, bd=0, borderwidth=0,
                highlightthickness=0, overrelief='flat'
            ).grid(row=row_val, column=col_val, pady=5) # Añadido padding -> Added padding

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
