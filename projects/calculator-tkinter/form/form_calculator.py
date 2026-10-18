import tkinter as tk
from tkinter import font
from config import constants as cons
import util.window_util as window_util


class FormCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.build_widget()
        self.build_widget_toggle()

    def build_widget_toggle(self):
        # Iniciar con el tema oscuro -> Start with dark theme
        self.dark_theme = True  # Variable bandera -> Flag variable
        
        # Configurar la fuente para el botón de tema -> Configure font for theme button
        theme_font = font.Font(family='Roboto', size=11, weight='bold')
        
        # Botón para cambiar de tema (usando emojis nativos) -> Theme toggle button (using native emojis)
        self.theme_button = tk.Button(
            self, text="Modo Oscuro 🌙", width=13, font=theme_font, bd=0, 
            borderwidth=0, highlightthickness=0, relief=tk.FLAT, 
            command=self.toggle_theme, bg=cons.COLOR_BOTONES_ESPECIALES_DARK, 
            fg=cons.COLOR_DE_TEXTO_DARK
        )
        self.theme_button.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="nw")  # Añadido padding -> Added padding


    def toggle_theme(self):
        # Cambiar entre temas oscuro y claro -> Switch between dark and light themes
        if self.dark_theme:
            # Aplicar tema claro -> Apply light theme
            self.configure(bg=cons.COLOR_DE_FONDO_LIGHT)
            self.entry.config(
                fg=cons.COLOR_DE_TEXTO_LIGHT, 
                bg=cons.COLOR_CAJA_TEXTO_LIGHT
            )
            self.operation_label.config(
                fg=cons.COLOR_DE_TEXTO_LIGHT, 
                bg=cons.COLOR_DE_FONDO_LIGHT
            )
            self.theme_button.configure(
                text="Modo Claro ☀️", 
                relief=tk.SUNKEN, 
                bg=cons.COLOR_BOTONES_ESPECIALES_LIGHT,
                fg=cons.COLOR_DE_TEXTO_LIGHT
            )
        else:
            # Aplicar tema oscuro -> Apply dark theme
            self.configure(bg=cons.COLOR_DE_FONDO_DARK)
            self.entry.config(
                fg=cons.COLOR_DE_TEXTO_DARK, 
                bg=cons.COLOR_CAJA_TEXTO_DARK
            )
            self.operation_label.config(
                fg=cons.COLOR_DE_TEXTO_DARK, 
                bg=cons.COLOR_DE_FONDO_DARK
            )
            self.theme_button.configure(
                text="Modo Oscuro 🌙", 
                relief=tk.RAISED, 
                bg=cons.COLOR_BOTONES_ESPECIALES_DARK,
                fg=cons.COLOR_DE_TEXTO_DARK
            )

        # Invertir el tema -> Toggle theme flag
        self.dark_theme = not self.dark_theme            


    def config_window(self):
        # Configuración inicial de la ventana -> Initial window configuration
        self.title("Python GUI Calculadora")
        # Configurar el color de fondo y hacer transparente la ventana -> Configure background color and set window transparency
        self.configure(bg=cons.COLOR_DE_FONDO_DARK)
        self.attributes('-alpha', 0.95)  # Ayuda a generar transparencia en la ventana -> Helps generate window transparency
        w, h = 370, 570  # Ancho y alto de la ventana -> Window width and height values
        window_util.centrar_ventana(self, w, h)

    def build_widget(self):
        # PRIMER WIDGET: Etiqueta para mostrar la operación solicitada -> FIRST WIDGET: Label to display requested operation
        self.operation_label = tk.Label(
            self, text="", font=('Arial', 16), 
            fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_DE_FONDO_DARK, justify='right'
        )
        self.operation_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="e")

        # SEGUNDO WIDGET: Pantalla de operación -> SECOND WIDGET: Operation display
        self.entry = tk.Entry(
            self, width=12, font=('Arial', 40), bd=0, 
            fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_CAJA_TEXTO_DARK, justify='right'
        )
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Lista de botones -> Button list
        buttons = [
            'C', '%', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=',
        ]

        row_val = 2  # Posición inicial de fila -> Initial row value
        col_val = 0

        # Configurar tipografía para los botones -> Configure button typography
        roboto_font = font.Font(family="Roboto", size=16)

        for button in buttons:
            if button in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                color_fondo = cons.COLOR_BOTONES_ESPECIALES_DARK
            else:
                color_fondo = cons.COLOR_BOTONES_DARK

            # Crear botones según el tipo -> Create buttons according to type
            if button == '=':
                tk.Button(
                    self, text=button, width=11, height=2, 
                    command=lambda b=button: self.on_button_click(b),
                    bg=color_fondo, fg=cons.COLOR_DE_TEXTO_DARK, relief=tk.FLAT,
                    font=roboto_font, padx=5, pady=5, bd=0, borderwidth=0,
                    highlightthickness=0, overrelief='flat'
                ).grid(row=row_val, column=col_val, columnspan=2, pady=5)
                col_val += 1
            else:
                tk.Button(
                    self, text=button, width=5, height=2, 
                    command=lambda b=button: self.on_button_click(b),
                    bg=color_fondo, fg=cons.COLOR_DE_TEXTO_DARK, relief=tk.FLAT,
                    font=roboto_font, padx=5, pady=5, bd=0, borderwidth=0,
                    highlightthickness=0, overrelief='flat'
                ).grid(row=row_val, column=col_val, pady=5)
                col_val += 1
            
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, value):
        # Manejo de clic en los botones -> Handle button click events
        if value == '=':
            try:
                expression = self.entry.get().replace('%', '/100')
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                operation = expression + " = "
                self.operation_label.config(text=operation)

            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.operation_label.config(text="")

        elif value == 'C':
            self.entry.delete(0, tk.END)
            self.operation_label.config(text="")

        elif value == '<':
            current_text = self.entry.get()
            if current_text:
                new_text = current_text[:-1]  # Eliminar el último carácter -> Remove last character
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_text)
                self.operation_label.config(text=new_text + " ")

        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)
            