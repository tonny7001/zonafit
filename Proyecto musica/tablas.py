# 04. Crando las tablas
# importar la clase de conexion
from conexionDB import Conexion

# obtener conexion
conexion = Conexion.obtener_conexion()

# crear cursor
cursor = conexion.cursor()

# ===================
# TABLA GENEROS
# ===================

cursor.execute("""
IF NOT EXISTS (
    SELECT * FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = 'generos'
)
CREATE TABLE generos(
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(100) NOT NULL UNIQUE,
    CONSTRAINT chk_nombre_genero CHECK (LEN(nombre) > 2)
);
""")

# ===================
# TABLA ARTISTAS
# ===================

cursor.execute("""
IF NOT EXISTS (
    SELECT * FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = 'artistas'
)
CREATE TABLE artistas(
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(100) NOT NULL,
    pais VARCHAR(50),
    anio_formacion INT,
    id_genero INT NULL,

    FOREIGN KEY (id_genero)
    REFERENCES generos(id)
    ON DELETE SET NULL
);
""")

# ===================
# TABLA ALBUMES
# ===================

cursor.execute("""
IF NOT EXISTS (
    SELECT * FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = 'albumes'
)
CREATE TABLE albumes(
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(100) NOT NULL,
    anio_lanzamiento INT NOT NULL,
    artista_id INT NOT NULL,

    FOREIGN KEY (artista_id)
    REFERENCES artistas(id)
    ON DELETE CASCADE
);
""")

# ===================
# TABLA CANCIONES
# ===================

cursor.execute("""
IF NOT EXISTS (
    SELECT * FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = 'canciones'
)
CREATE TABLE canciones(
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(100) NOT NULL,
    duracion INT,
    album_id INT NOT NULL,

    FOREIGN KEY (album_id) REFERENCES albumes(id)
    ON DELETE CASCADE,

    CHECK (duracion > 0)
);
""")

# guardar cambios
conexion.commit()

# cerrar cursor y conexion
cursor.close()
conexion.close()

print("Tablas creadas correctamente")
