# importar las librerias
import tkinter as tk
from tkinter import ttk

from genero_dao import GeneroDAO


# crear la clase proyecto musica
class MusicaJorge(tk.Tk):

    # Constantes de colores
    COLOR_VENTANA = "#0F172A"  # Azul oscuro

    # método constructor
    def __init__(self):
        super().__init__()

        # llamar los métodos de configuración
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()

    # método ventana
    def configurar_ventana(self):
        self.geometry("900x600")
        self.title("Musica Jorge (Generos)")
        self.config(background=self.COLOR_VENTANA)
        self.resizable(False, False)

        # estilos
        self.estilos = ttk.Style()
        self.estilos.theme_use("clam")

        self.estilos.configure(
            ".",
            background=self.COLOR_VENTANA,
            foreground="white",
            fieldbackground="black",
        )

    # configuración del grid
    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    # título de ventana
    def mostrar_titulo(self):

        # crear una etiqueta para el titulo
        label = ttk.Label(
            self,
            text="Musica Jorge (Generos)",
            font=("Segoe UI", 30),
            background=self.COLOR_VENTANA,
            foreground="#FFFFFF",
        )

        # mostrar la etiqueta y darle coordenadas
        label.grid(row=0, column=0, columnspan=2, pady=30)

    # mostrar el formulario
    def mostrar_formulario(self):

        # crear el formulario para el ingreso de los datos
        self.frame_formulario = ttk.Frame(self)

        # =======================
        # CAMPO ID
        # =======================
        label_id = ttk.Label(self.frame_formulario, text="Id:")

        label_id.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)

        self.id_texto = ttk.Entry(self.frame_formulario)
        self.id_texto.grid(row=0, column=1)

        # =======================
        # CAMPO NOMBRE
        # =======================
        label_nombre = ttk.Label(self.frame_formulario, text="Nombre:")

        label_nombre.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)

        self.nombre_texto = ttk.Entry(self.frame_formulario)
        self.nombre_texto.grid(row=1, column=1)

        # mostrar frame formulario
        self.frame_formulario.grid(row=1, column=0, padx=20, pady=20)

    # mostrar la tabla
    def mostrar_tabla(self):

        # crear el frame
        self.frame_tabla = ttk.Frame(self)

        # estilos de la tabla
        self.estilos.configure(
            "Treeview",
            background="#B9F1E7",
            foreground="black",
            fieldbackground="#B9F1E7",
            rowheight=30,
        )

        # columnas de la tabla
        columnas = ("Id", "Nombre")

        # crear el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")

        # mostrar la tabla
        self.tabla.grid(row=0, column=0)

        # mostrar el frame
        self.frame_tabla.grid(row=1, column=1, padx=30)

        # agregar los encabezados
        self.tabla.heading("Id", text="Id", anchor=tk.CENTER)

        self.tabla.heading("Nombre", text="Nombre", anchor=tk.W)

        # configurar las columnas
        self.tabla.column("Id", anchor=tk.CENTER, width=100)

        self.tabla.column("Nombre", anchor=tk.W, width=200)

        # reutilizar todo el código DAO y conexión
        generos = GeneroDAO.seleccionar()

        for genero in generos:
            self.tabla.insert(
                parent="",
                index=tk.END,
                values=(
                    genero.id,
                    genero.nombre,
                ),
            )

        # agregar el scrollbar
        scrollbar = ttk.Scrollbar(
            self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview
        )

        self.tabla.configure(yscrollcommand=scrollbar.set)

        scrollbar.grid(row=0, column=1, sticky=tk.NS)


if __name__ == "__main__":
    app = MusicaJorge()
    app.mainloop()
