# ===================
# CREAR EL ACCESO A LOS ATRIBUTOS DE LA TABLA CLIENTE
# ===================


class Cliente:
    # Método constructor con atributos
    def __init__(
        self,
        id=None,
        nombre=None,
        apellido=None,
        telefono=None,
        correo=None,
        membresia=None,
    ):
        # Atributos de la clase
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.membresia = membresia

    # Representación en texto del objeto
    def __str__(self):
        return (
            f"Cliente("
            f"id={self.id}, "
            f"nombre='{self.nombre}', "
            f"apellido='{self.apellido}', "
            f"telefono='{self.telefono}', "
            f"correo='{self.correo}', "
            f"membresia='{self.membresia}'"
            f")"
        )
