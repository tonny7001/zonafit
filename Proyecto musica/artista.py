# ======================
#    CLASE ARTISTA
# ======================


# 1. Nombre de la clase
class Artista:

    # 2. Método constructor
    def __init__(
        self, id=None, nombre=None, pais=None, anio_formacion=None, id_genero=None
    ):

        # 3. Atributos
        self.id_artista = id
        self.nombre_artista = nombre
        self.pais_artista = pais
        self.anio_formacion = anio_formacion
        self.id_genero = id_genero

    # 4. Mostrar información
    def __str__(self):
        return f"""
        Id Artista: {self.id_artista}
        Nombre Artista: {self.nombre_artista}
        País: {self.pais_artista}
        Año Formación: {self.anio_formacion}
        Id Género: {self.id_genero}
        """
