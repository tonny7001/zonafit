# Importa la librería Tkinter y le asigna el alias tk
import tkinter as tk

# Crea la ventana principal
ventana = tk.Tk()

# Título que aparecerá en la barra superior
ventana.title("Mi primera ventana")

# Tamaño de la ventana (ancho x alto)
ventana.geometry("600x600")

# Impide que el usuario cambie el tamaño
ventana.resizable(None, None)

# Cambia el color de fondo de la ventana
ventana.configure(background="#303841")

# Mantiene la ventana abierta y esperando eventos
ventana.mainloop()
