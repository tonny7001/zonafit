# 01. esta conexion es solo para conectarme al servidor no para conectarme a la base de datos


# importar la libreria
import pyodbc


# crear una clase llamada Conexion
class Conexion:

    @staticmethod
    # funcion para obtener la conexion
    def obtener_conexion():

        # crear conexion con SQL Server
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "Trusted_Connection=yes;"
        )

        # retornar conexion
        return conexion
