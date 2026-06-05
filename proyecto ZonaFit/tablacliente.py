from conexionDB import Conexion

conexion = None
cursor = None

try:
    conexion = Conexion.obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("DROP TABLE IF EXISTS cliente")

    cursor.execute("""
    CREATE TABLE cliente (
        id INT PRIMARY KEY NOT NULL,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        telefono VARCHAR(20) NOT NULL,
        correo VARCHAR(100),
        membresia VARCHAR(20) NOT NULL
    )
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
