import tkinter as tk
from tkinter import messagebox, ttk

# ==========================
# FUNCIONES
# ==========================


def ingresar():
    usuario = user_texto.get().strip()
    password = password_texto.get().strip()

    if not usuario or not password:
        messagebox.showwarning("Campos vacíos", "Debe ingresar usuario y contraseña")
        return

    messagebox.showinfo("Acceso correcto", f"Bienvenido {usuario}")


# ==========================
# VENTANA PRINCIPAL
# ==========================

ventana = tk.Tk()
ventana.title("Zona Fit Login")
ventana.geometry("600x600")
ventana.resizable(False, False)
ventana.configure(background="#2E3D47")

# ==========================
# ESTILOS
# ==========================

estilos = ttk.Style()
estilos.theme_use("clam")

estilos.configure("TFrame", background="#2E3D47")

estilos.configure(
    "Titulo.TLabel",
    background="#2E3D47",
    foreground="white",
    font=("Arial", 24, "bold"),
)

estilos.configure(
    "Subtitulo.TLabel", background="#2E3D47", foreground="#DADADA", font=("Arial", 11)
)

estilos.configure(
    "TLabel", background="#2E3D47", foreground="white", font=("Arial", 10)
)

# ==========================
# CONFIGURACION GRID
# ==========================

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# ==========================
# FRAME PRINCIPAL
# ==========================

frame = ttk.Frame(ventana, padding=30)
frame.grid(row=0, column=0)

# ==========================
# TITULOS
# ==========================

titulo = ttk.Label(frame, text="🏋️ Zona Fit", style="Titulo.TLabel")
titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))

subtitulo = ttk.Label(frame, text="Iniciar Sesión", style="Subtitulo.TLabel")
subtitulo.grid(row=1, column=0, columnspan=2, pady=(0, 25))

# ==========================
# USUARIO
# ==========================

user = ttk.Label(frame, text="Usuario:")
user.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)

user_texto = ttk.Entry(frame, width=30)
user_texto.grid(row=2, column=1, padx=10, pady=10)

# ==========================
# CONTRASEÑA
# ==========================

password = ttk.Label(frame, text="Contraseña:")
password.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)

password_texto = ttk.Entry(frame, width=30, show="*")
password_texto.grid(row=3, column=1, padx=10, pady=10)

# ==========================
# BOTON
# ==========================

boton = ttk.Button(frame, text="Entrar", command=ingresar)
boton.grid(row=4, column=0, columnspan=2, pady=20, ipadx=15, ipady=5)

# Permite iniciar sesión con Enter
ventana.bind("<Return>", lambda event: ingresar())

# Cursor inicialmente en usuario
user_texto.focus()

ventana.mainloop()


"""
no perdeer este dato calcular la fecha de vencimiento en base a la fecha de inscripcion 
from datetime import datetime, timedelta

fecha_inscripcion = datetime.now()
fecha_vencimiento = fecha_inscripcion + timedelta(days=30)

print(fecha_vencimiento.strftime("%Y-%m-%d"))





"""
