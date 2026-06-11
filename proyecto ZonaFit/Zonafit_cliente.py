import tkinter as tk
from tkinter import ttk


class Interfaz(tk.Tk):
    COLOR_VENTANA = "#303841"

    def __init__(self):
        super().__init__()
        # definicion de metodos
        self.configurar_ventana()
        # self.
        # self.
        # self.
        # self.
        # self.
        # self.

    def configurar_ventana(self):
        self.geometry("1200x500")
        self.title("Zona Fit (Usuario)")
        self.configure(background=Interfaz.COLOR_VENTANA)

        # Aplicacion de los estilos

        self.estilos = ttk.Style()
        self.estilos.theme_use("clam")
        self.estilos.configure(
            ".",
            background=Interfaz.COLOR_VENTANA,
            foreground="#F5F5F5",
            fieldbackground="#06202B",
        )


# ==========================
# PRUEBA
# ==========================

if __name__ == "__main__":
    ventana = Interfaz()
    ventana.mainloop()
