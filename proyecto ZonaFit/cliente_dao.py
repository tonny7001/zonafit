from cliente import Cliente
from conexionDB import Conexion


class ClienteDAO:

    SELECCIONAR = "SELECT * FROM cliente"
    INSERTAR = "INSERT INTO cliente (id, nombre, apellido, telefono, correo, membresia) VALUES (?,?,?,?,?,?)"
    ACTUALIZAR = "UPDATE cliente SET nombre=?, apellido=?, telefono=?, correo=?, membresia=? WHERE id=?"
    ELIMINAR = "DELETE FROM cliente WHERE id=?"

    @classmethod
    def seleccionar(cls):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)

            seleccion = cursor.fetchall()
            clientes = []

            for seleccionado in seleccion:
                cliente = Cliente(
                    seleccionado[0],
                    seleccionado[1],
                    seleccionado[2],
                    seleccionado[3],
                    seleccionado[4],
                    seleccionado[5],
                )
                clientes.append(cliente)

            return clientes

        except Exception as e:
            print(f"Ocurrió un error al seleccionar clientes: {e}")

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (
                cliente.id,
                cliente.nombre,
                cliente.apellido,
                cliente.telefono,
                cliente.correo,
                cliente.membresia,
            )
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f"Ocurrió un error al seleccionar clientes: {e}")

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()


if __name__ == "__main__":

    cliente1 = Cliente(
        71795830, "Jorge", "Mosquera", "3001234567", "jorge@gmail.com", "AF001"
    )
    registros_insertados = ClienteDAO.insertar(cliente1)

    print(f"Registros insertados: {registros_insertados}")

# if __name__ == "__main__":
# clientes = ClienteDAO.seleccionar()
# for cliente in clientes:
#   print(cliente)
