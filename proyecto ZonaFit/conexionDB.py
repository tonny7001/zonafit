import pyodbc


class Conexion:

    @staticmethod
    def obtener_conexion():
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=zona_fit_db;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
        return conexion
