from conexionServidor import Conexion

try:
    conexion = Conexion.obtener_conexion()
    conexion.autocommit = True

    cursor = conexion.cursor()

    cursor.execute("""
    CREATE DATABASE musica_jorge
    """)

    print("Base de datos creada correctamente")

except Exception as e:
    print(f"Error: {e}")

finally:
    cursor.close()
    conexion.close()
