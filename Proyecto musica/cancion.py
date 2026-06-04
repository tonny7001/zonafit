# ======================
#    CLASE CANCION
# ======================


# 1. Nombre de la clase
class Cancion:

    # 2. Método constructor
    def __init__(self, id=None, nombre=None, duracion=None, album_id=None):

        # 3. Atributos
        self.id_cancion = id
        self.nombre_cancion = nombre
        self.duracion_cancion = duracion
        self.album_id = album_id

    # 4. Mostrar información
    def __str__(self):
        return f"""
        Id Canción: {self.id_cancion}
        Nombre Canción: {self.nombre_cancion}
        Duración: {self.duracion_cancion}
        Id Album: {self.album_id}
        """
