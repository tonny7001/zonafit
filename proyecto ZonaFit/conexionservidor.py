# ===================
# CONEXIÓN SOLO AL SERVIDOR SQL SERVER
# (sin base de datos específica)
# ===================

import pyodbc


class Conexion:

    @staticmethod
    def obtener_conexion():
        # Conecta al motor de SQL Server
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "Trusted_Connection=yes;"
        )
        return conexion
