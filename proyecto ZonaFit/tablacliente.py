from conexionDB import Conexion

conexion = None
cursor = None

try:
    conexion = Conexion.obtener_conexion()
    cursor = conexion.cursor()

    # =====================
    # TABLA CLIENTE
    # =====================

    cursor.execute("DROP TABLE IF EXISTS cliente")

    cursor.execute("""
    CREATE TABLE cliente (
        id_cliente INT PRIMARY KEY NOT NULL,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        telefono VARCHAR(20) NOT NULL,
        correo VARCHAR(100),
        membresia VARCHAR(20) NOT NULL,
        fecha_inscripcion DATE NOT NULL,
        fecha_vencimiento DATE NOT NULL,
        estado VARCHAR(20) NOT NULL
    )
    """)

    # =====================
    # TABLA USUARIO
    # =====================

    cursor.execute("DROP TABLE IF EXISTS usuario")

    cursor.execute("""
    CREATE TABLE usuario (
        id_usuario INT PRIMARY KEY NOT NULL,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        telefono VARCHAR(20) NOT NULL,
        correo VARCHAR(100),
        rol VARCHAR(20) NOT NULL,
        estado VARCHAR(20) NOT NULL
    )
    """)

    conexion.commit()

    print("Tablas creadas correctamente")

except Exception as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()

    if conexion:
        conexion.close()
