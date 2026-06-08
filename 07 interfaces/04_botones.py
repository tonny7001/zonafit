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


# Función que se ejecutará al presionar el botón
def enviar():
    # Muestra una ventana emergente
    showinfo(title="Mensaje", message="Hola mundo")


# Crea un botón
boton1 = ttk.Button(
    ventana, text="Enter", command=enviar  # Función que se ejecuta al hacer clic
)

# Muestra el botón en la ventana
boton1.pack(pady=20)

# Mantiene la aplicación en ejecución
ventana.mainloop()
