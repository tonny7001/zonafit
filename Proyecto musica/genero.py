# ======================
#    CLASE GENERO
# ======================


class Genero:

    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"""
Id Genero: {self.id}
Nombre Genero: {self.nombre}
"""
