# 03. conexion a base de datos
# importar libreria
import pyodbc


# crear clase conexion
class Conexion:

    @staticmethod
    def obtener_conexion():

        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=musica_jorge;"
            "Trusted_Connection=yes;"
        )

        return conexion
