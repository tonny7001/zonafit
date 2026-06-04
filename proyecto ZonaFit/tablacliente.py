# ===================
# CREAR TABLAS
# ===================

from conexionDB import Conexion

conexion = None
cursor = None

try:
    conexion = Conexion.obtener_conexion()
    cursor = conexion.cursor()

    # crea tabla cliente si no existe
    cursor.execute("""
    IF NOT EXISTS (
        SELECT * FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_NAME = 'cliente'
    )
    BEGIN
        CREATE TABLE cliente (
            id INT IDENTITY(1,1) PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            apellido VARCHAR(100) NOT NULL,
            telefono VARCHAR(20) NOT NULL,
            correo VARCHAR(100),
            membresia VARCHAR(20) NOT NULL UNIQUE
        )
    END
    """)

    conexion.commit()
    print("Tabla cliente creada correctamente")

except Exception as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()
