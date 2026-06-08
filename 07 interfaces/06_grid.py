# Importa Tkinter
import tkinter as tk

# Importa widgets modernos
from tkinter import ttk

# Importa la función para mostrar mensajes emergentes
from tkinter.messagebox import showinfo

# Crea la ventana principal
ventana = tk.Tk()

# Configuración de la ventana
ventana.title("Mi primera ventana")
ventana.geometry("600x600")
ventana.resizable(None, None)
ventana.configure(background="#303841")

# manejo de grid botones en linea recta
boton1 = ttk.Button(ventana, text="Boton 1")
boton2 = ttk.Button(ventana, text="Boton 2")
boton3 = ttk.Button(ventana, text="Boton 3")


# publicar usando grid
boton1.grid(row=0, column=0, pady=10, padx=5)
boton2.grid(row=1, column=1, pady=10, padx=5)
boton3.grid(row=2, column=2, pady=10, padx=5)


# Mantiene la aplicación en ejecución
ventana.mainloop()
