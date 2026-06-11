import tkinter as tk
from tkinter import messagebox, ttk

from cliente_dao import ClienteDAO


class LoginApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # ==========================
        # CONFIGURACIÓN VENTANA
        # ==========================
        self.title("Zona Fit Login")
        self.geometry("600x600")
        self.resizable(False, False)
        self.configure(background="#2E3D47")

        # Grid principal
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Configurar estilos
        self.configurar_estilos()

        # Crear interfaz
        self.crear_componentes()

        # Evento Enter
        self.bind("<Return>", self.ingresar)

    def configurar_estilos(self):

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
            "Subtitulo.TLabel",
            background="#2E3D47",
            foreground="#DADADA",
            font=("Arial", 11),
        )

        estilos.configure(
            "TLabel", background="#2E3D47", foreground="white", font=("Arial", 10)
        )

        estilos.configure("Boton.TButton", font=("Arial", 10, "bold"))

    def crear_componentes(self):

        # ==========================
        # FRAME PRINCIPAL
        # ==========================
        self.frame = ttk.Frame(self, padding=30)

        self.frame.grid(row=0, column=0)

        # ==========================
        # TITULO
        # ==========================
        self.lbl_titulo = ttk.Label(
            self.frame, text="🏋️ Zona Fit", style="Titulo.TLabel"
        )

        self.lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # ==========================
        # SUBTITULO
        # ==========================
        self.lbl_subtitulo = ttk.Label(
            self.frame, text="Iniciar Sesión", style="Subtitulo.TLabel"
        )

        self.lbl_subtitulo.grid(row=1, column=0, columnspan=2, pady=(0, 25))

        # ==========================
        # USUARIO
        # ==========================
        self.lbl_usuario = ttk.Label(self.frame, text="Usuario:")

        self.lbl_usuario.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        self.txt_usuario = ttk.Entry(self.frame, width=30)

        self.txt_usuario.grid(row=2, column=1, padx=10, pady=10)

        # ==========================
        # PASSWORD
        # ==========================
        self.lbl_password = ttk.Label(self.frame, text="Contraseña:")

        self.lbl_password.grid(row=3, column=0, sticky="w", padx=10, pady=10)

        self.txt_password = ttk.Entry(self.frame, width=30, show="*")

        self.txt_password.grid(row=3, column=1, padx=10, pady=10)

        # ==========================
        # BOTÓN
        # ==========================
        self.btn_ingresar = ttk.Button(
            self.frame, text="Entrar", style="Boton.TButton", command=self.ingresar
        )

        self.btn_ingresar.grid(
            row=4, column=0, columnspan=2, pady=20, ipadx=15, ipady=5
        )

    def limpiar_campos(self):

        self.txt_usuario.delete(0, tk.END)
        self.txt_password.delete(0, tk.END)

    def validar_usuario(self, usuario, password):

        return usuario == "root" and password == "admin"

    def cargar_clientes(self):

        clientes = ClienteDAO.seleccionar()

        for cliente in clientes:
            print(cliente)

    def ingresar(self, event=None):

        usuario = self.txt_usuario.get().strip()
        password = self.txt_password.get().strip()

        if self.validar_usuario(usuario, password):

            messagebox.showinfo("Acceso correcto", f"Bienvenido {usuario}")

            self.cargar_clientes()

        else:

            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

        self.limpiar_campos()


# ==========================
# PROGRAMA PRINCIPAL
# ==========================

# if __name__ == "__main__":

# app = LoginApp()
# app.mainloop()
