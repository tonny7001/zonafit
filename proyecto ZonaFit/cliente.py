# ===================
# CLASE CLIENTE
# ===================


class Cliente:

    def __init__(
        self,
        id_cliente=None,
        nombre=None,
        apellido=None,
        telefono=None,
        correo=None,
        membresia=None,
        fecha_inscripcion=None,
        fecha_vencimiento=None,
        estado=None,
    ):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.membresia = membresia
        self.fecha_inscripcion = fecha_inscripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado

    def __str__(self):
        return (
            f"Cliente("
            f"id_cliente={self.id_cliente}, "
            f"nombre='{self.nombre}', "
            f"apellido='{self.apellido}', "
            f"telefono='{self.telefono}', "
            f"correo='{self.correo}', "
            f"membresia='{self.membresia}', "
            f"fecha_inscripcion='{self.fecha_inscripcion}', "
            f"fecha_vencimiento='{self.fecha_vencimiento}', "
            f"estado='{self.estado}'"
            f")"
        )
