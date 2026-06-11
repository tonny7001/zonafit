# USO DE VENTANA CON PROGRAMACION ORIENTADA A OBJETOS

# importar la libreria tk y ttk
import tkinter as tk
from tkinter import ttk


# definir la clase para la ventana y hereda de la libreria tk
class App(tk.Tk):

    # Metodo constructor
    def __init__(self):
        # iniciar el objeto de la clase padre
        super().__init__()

        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_tabla()

    # configuracion de la ventana
    def configurar_ventana(self):
        self.title("Mi primera ventana con POO")
        self.geometry("1200x500")
        self.resizable(False, False)
        self.configure(background="#303841")

    # configuracion del grid
    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

    def mostrar_tabla(self):

        # Definir columnas
        columnas = (
            "Id",
            "Nombre",
            "Apellido",
            "Telefono",
            "Correo",
            "Membresia",
            "Fecha Inscripcion",
            "Fecha Vencimiento",
            "Estado Cliente",
        )

        # Crear Treeview
        tabla_cliente = ttk.Treeview(self, columns=columnas, show="headings")

        # Configurar encabezados
        for columna in columnas:
            tabla_cliente.heading(columna, text=columna)

        # Configurar ancho de columnas
        tabla_cliente.column("Id", width=80, anchor="center")
        tabla_cliente.column("Nombre", width=120, anchor="center")
        tabla_cliente.column("Apellido", width=120, anchor="center")
        tabla_cliente.column("Telefono", width=120, anchor="center")
        tabla_cliente.column("Correo", width=220, anchor="center")
        tabla_cliente.column("Membresia", width=100, anchor="center")
        tabla_cliente.column("Fecha Inscripcion", width=120, anchor="center")
        tabla_cliente.column("Fecha Vencimiento", width=120, anchor="center")
        tabla_cliente.column("Estado Cliente", width=100, anchor="center")

        # Datos de ejemplo
        clientes = [
            (
                71795830,
                "Jorge",
                "Mosquera",
                "3003669824",
                "jorge_mosquera6@hotmail.com",
                "AC001",
                "2025-05-26",
                "2026-06-20",
                "Activo",
            ),
            (
                12345678,
                "Maria",
                "Lopez",
                "3101234567",
                "maria@gmail.com",
                "AC002",
                "2025-06-01",
                "2026-06-01",
                "Activo",
            ),
            (
                98765432,
                "Carlos",
                "Ramirez",
                "3209876543",
                "carlos@gmail.com",
                "AC003",
                "2025-04-15",
                "2026-04-15",
                "Inactivo",
            ),
        ]

        # Cargar datos en la tabla
        for cliente in clientes:
            tabla_cliente.insert("", tk.END, values=cliente)

        # Scroll vertical
        scroll_y = ttk.Scrollbar(self, orient="vertical", command=tabla_cliente.yview)

        tabla_cliente.configure(yscrollcommand=scroll_y.set)

        # Ubicar componentes
        tabla_cliente.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        scroll_y.pack(side="right", fill="y")


# PRUEBA
if __name__ == "__main__":
    app = App()
    app.mainloop()
