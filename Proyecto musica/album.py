# ======================
#    CLASE ALBUM
# ======================


# 1. Nombre de la clase
class Album:

    # 2. Método constructor
    def __init__(self, id=None, nombre=None, anio_lanzamiento=None, artista_id=None):

        # 3. Atributos
        self.id_album = id
        self.nombre_album = nombre
        self.anio_lanzamiento = anio_lanzamiento
        self.artista_id = artista_id

    # 4. Mostrar información
    def __str__(self):
        return f"""
        Id Album: {self.id_album}
        Nombre Album: {self.nombre_album}
        Año Lanzamiento: {self.anio_lanzamiento}
        Id Artista: {self.artista_id}
        """
