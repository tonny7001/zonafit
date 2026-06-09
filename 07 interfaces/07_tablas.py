# Importa Tkinter
import tkinter as tk

# Importa widgets modernos
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()

# Configuración de la ventana
ventana.title("Manejo de Clientes")
ventana.geometry("1200x500")
ventana.resizable(False, False)
ventana.configure(background="#303841")

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
tabla_cliente = ttk.Treeview(ventana, columns=columnas, show="headings")

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
scroll_y = ttk.Scrollbar(ventana, orient="vertical", command=tabla_cliente.yview)

tabla_cliente.configure(yscrollcommand=scroll_y.set)

# Ubicar componentes
tabla_cliente.pack(side="left", fill="both", expand=True, padx=10, pady=10)
scroll_y.pack(side="right", fill="y")

# Ejecutar aplicación
ventana.mainloop()
