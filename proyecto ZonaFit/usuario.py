class Usuario:

    def __init__(
        self,
        id_usuario=None,
        nombre=None,
        apellido=None,
        telefono=None,
        correo=None,
        rol=None,
        estado=None,
    ):

        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.rol = rol
        self.estado = estado

    def __str__(self):
        return (
            f"Usuario("
            f"id_usuario={self.id_usuario}, "
            f"nombre='{self.nombre}', "
            f"apellido='{self.apellido}', "
            f"telefono='{self.telefono}', "
            f"correo='{self.correo}', "
            f"rol='{self.rol}', "
            f"estado='{self.estado}'"
            f")"
        )


usuario1 = Usuario(
    1, "Jorge", "Mosquera", "3001234567", "jorge@gmail.com", "Administrador", "Activo"
)

print(usuario1)
