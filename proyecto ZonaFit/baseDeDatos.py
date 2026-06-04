# ===================
# CREAR BASE DE DATOS
# ===================

from conexionservidor import Conexion

conexion = None
cursor = None

try:
    conexion = Conexion.obtener_conexion()
    conexion.autocommit = True  # necesario para CREATE DATABASE
    cursor = conexion.cursor()

    # crea la base de datos solo si no existe
    cursor.execute("""
    IF NOT EXISTS (
        SELECT name FROM sys.databases WHERE name = 'zona_fit_db'
    )
    CREATE DATABASE zona_fit_db
    """)

    print("Base de datos creada correctamente")

except Exception as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()
