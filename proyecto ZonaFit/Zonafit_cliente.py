import tkinter as tk
from tkinter import ttk

from cliente_dao import ClienteDAO


class Interfaz(tk.Tk):
    COLOR_VENTANA = "#303841"

    def __init__(self):
        super().__init__()

        # Definición de métodos
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tablas()

    # ===================
    # MOSTRAR VENTANA
    # ===================
    def configurar_ventana(self):
        self.geometry("1200x900")
        self.title("Zona Fit (Usuario)")
        self.configure(background=Interfaz.COLOR_VENTANA)

        # Aplicación de estilos
        self.estilos = ttk.Style()
        self.estilos.theme_use("clam")

        self.estilos.configure(
            ".",
            background=Interfaz.COLOR_VENTANA,
            foreground="#F5F5F5",
            fieldbackground="#06202B",
        )

    # ===================
    # CONFIGURAR GRID
    # ===================
    def configurar_grid(self):
        self.columnconfigure(0, weight=1)  # el formulario
        self.columnconfigure(1, weight=4)  # la tabla
        self.columnconfigure(2, weight=4)  # los botones
        self.rowconfigure(1, weight=1)

    # ===================
    # MOSTRAR TÍTULO
    # ===================
    def mostrar_titulo(self):
        label_titulo = ttk.Label(
            self,
            text="Zona Fit (Clientes)",
            font=("Arial", 30, "bold"),
        )

        label_titulo.grid(row=0, column=0, columnspan=2, pady=30)

    # ===================
    # MOSTRAR FORMULARIO
    # ===================
    def mostrar_formulario(self):
        # crear el formulario
        self.frame_formulario = ttk.Frame(self)

        # 1. ID
        label_id = ttk.Label(self.frame_formulario, text="ID:")
        label_id.grid(row=0, column=0, sticky="e", pady=5, padx=5)

        self.id_text = ttk.Entry(self.frame_formulario)
        self.id_text.grid(row=0, column=1, sticky="ew", padx=5)

        # 2. NOMBRE
        label_nombre = ttk.Label(self.frame_formulario, text="Nombre:")
        label_nombre.grid(row=1, column=0, sticky="e", pady=5, padx=5)

        self.nombre_text = ttk.Entry(self.frame_formulario)
        self.nombre_text.grid(row=1, column=1, sticky="ew", padx=5)

        # 3. APELLIDO
        label_apellido = ttk.Label(self.frame_formulario, text="Apellido:")
        label_apellido.grid(row=2, column=0, sticky="e", pady=5, padx=5)

        self.apellido_text = ttk.Entry(self.frame_formulario)
        self.apellido_text.grid(row=2, column=1, sticky="ew", padx=5)

        # 4. TELEFONO
        label_telefono = ttk.Label(self.frame_formulario, text="Telefono:")
        label_telefono.grid(row=3, column=0, sticky="e", pady=5, padx=5)

        self.telefono_text = ttk.Entry(self.frame_formulario)
        self.telefono_text.grid(row=3, column=1, sticky="ew", padx=5)

        # 5. CORREO
        label_correo = ttk.Label(self.frame_formulario, text="Correo:")
        label_correo.grid(row=4, column=0, sticky="e", pady=5, padx=5)

        self.correo_text = ttk.Entry(self.frame_formulario)
        self.correo_text.grid(row=4, column=1, sticky="ew", padx=5)

        # 6. MEMBRESIA
        label_membresia = ttk.Label(self.frame_formulario, text="Membresia:")
        label_membresia.grid(row=5, column=0, sticky="e", pady=5, padx=5)

        self.membresia_text = ttk.Entry(self.frame_formulario)
        self.membresia_text.grid(row=5, column=1, sticky="ew", padx=5)

        # 7. FECHA INSCRIPCION
        label_fecha_ins = ttk.Label(self.frame_formulario, text="Fecha inscripción:")
        label_fecha_ins.grid(row=6, column=0, sticky="e", pady=5, padx=5)

        self.fecha_ins_text = ttk.Entry(self.frame_formulario)
        self.fecha_ins_text.grid(row=6, column=1, sticky="ew", padx=5)

        # 8. FECHA VENCIMIENTO
        label_fecha_venc = ttk.Label(self.frame_formulario, text="Fecha vencimiento:")
        label_fecha_venc.grid(row=7, column=0, sticky="e", pady=5, padx=5)

        self.fecha_venc_text = ttk.Entry(self.frame_formulario)
        self.fecha_venc_text.grid(row=7, column=1, sticky="ew", padx=5)

        # 9. ESTADO CLIENTE
        label_estado = ttk.Label(self.frame_formulario, text="Estado del cliente:")
        label_estado.grid(row=8, column=0, sticky="e", pady=5, padx=5)

        self.estado_text = ttk.Entry(self.frame_formulario)
        self.estado_text.grid(row=8, column=1, sticky="ew", padx=5)

        # configuración interna del frame
        self.frame_formulario.columnconfigure(0, weight=0)
        self.frame_formulario.columnconfigure(1, weight=1)

        # mostrar frame
        self.frame_formulario.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # ===================
    # MOSTRAR TABLA
    # ===================
    def mostrar_tablas(self):

        # Frame para la tabla
        self.frame_tabla = ttk.Frame(self)

        self.frame_tabla.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Expandir tabla dentro del frame
        self.frame_tabla.rowconfigure(0, weight=1)
        self.frame_tabla.columnconfigure(0, weight=1)

        # Estilo Treeview
        self.estilos.configure(
            "Treeview",
            background="black",
            foreground="white",
            fieldbackground="black",
            rowheight=30,
        )

        self.estilos.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        # Columnas
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

        # Crear tabla
        self.tabla_clientes = ttk.Treeview(
            self.frame_tabla, columns=columnas, show="headings"
        )

        # Encabezados
        for columna in columnas:
            self.tabla_clientes.heading(columna, text=columna)

        # Ancho de columnas
        self.tabla_clientes.column("Id", width=60, anchor="center")
        self.tabla_clientes.column("Nombre", width=120, anchor="center")
        self.tabla_clientes.column("Apellido", width=120, anchor="center")
        self.tabla_clientes.column("Telefono", width=120, anchor="center")
        self.tabla_clientes.column("Correo", width=220, anchor="center")
        self.tabla_clientes.column("Membresia", width=120, anchor="center")
        self.tabla_clientes.column("Fecha Inscripcion", width=140, anchor="center")
        self.tabla_clientes.column("Fecha Vencimiento", width=140, anchor="center")
        self.tabla_clientes.column("Estado Cliente", width=120, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            self.frame_tabla, orient="vertical", command=self.tabla_clientes.yview
        )

        self.tabla_clientes.configure(yscrollcommand=scrollbar.set)

        # Posicionar widgets
        self.tabla_clientes.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Cargar datos
        clientes = ClienteDAO.seleccionar() or []

        for cliente in clientes:
            self.tabla_clientes.insert(
                "",
                tk.END,
                values=(
                    cliente.id_cliente,
                    cliente.nombre,
                    cliente.apellido,
                    cliente.telefono,
                    cliente.correo,
                    cliente.membresia,
                    cliente.fecha_inscripcion,
                    cliente.fecha_vencimiento,
                    cliente.estado,
                ),
            )


if __name__ == "__main__":
    ventana = Interfaz()
    ventana.mainloop()
