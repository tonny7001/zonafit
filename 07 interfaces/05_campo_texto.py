# Importa la librería Tkinter y le asigna el alias tk
import tkinter as tk
from tkinter import ttk

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

# Insertar un campo de texto o entry
campo_texto = ttk.Entry(ventana, font=("Arial", 12))
campo_texto.pack(pady=30)


def enviar():
    texto = campo_texto.get()
    print(f"Has ingresado:{texto} ")
    label1["text"] = texto


# boton
boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.pack(pady=30)
# etiqueta
label1 = ttk.Label(ventana, text="")
label1.pack(pady=50)

# Mantiene la ventana abierta y esperando eventos
ventana.mainloop()
