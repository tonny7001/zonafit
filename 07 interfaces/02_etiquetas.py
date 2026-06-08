# Importa Tkinter
import tkinter as tk

# Importa los widgets modernos de Tkinter
from tkinter import ttk

# Crea la ventana principal
ventana = tk.Tk()

# Configuración de la ventana
ventana.title("Mi primera ventana")
ventana.geometry("600x600")
ventana.resizable(None, None)
ventana.configure(background="#303841")

# Crea una etiqueta de texto
label1 = ttk.Label(ventana, text="Hola mundo...")

# Muestra la etiqueta en la ventana
# pady agrega espacio vertical
label1.pack(pady=20)

# Inicia la aplicación
ventana.mainloop()
