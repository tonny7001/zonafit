# PRUEBAS DE LOS MODELOS QUE FUNCIONEN

from album import Album
from artista import Artista
from cancion import Cancion
from genero import Genero

# Género
genero = Genero(1, "Rock")
print(genero)

# Artista
artista = Artista(1, "Queen", "Reino Unido", 1970, 1)
print(artista)

# Album
album = Album(1, "A Night at the Opera", 1975, 1)
print(album)

# Canción
cancion = Cancion(1, "Bohemian Rhapsody", "5:55", 1)
print(cancion)
