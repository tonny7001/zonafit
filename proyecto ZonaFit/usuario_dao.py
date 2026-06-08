from conexionDB import Conexion
from usuario import Usuario


class UsuarioDAO:

    SELECCIONAR = "SELECT * FROM usuario"

    INSERTAR = """
    INSERT INTO usuario
    (id_usuario, nombre, apellido, telefono, correo, rol, estado)
    VALUES (?,?,?,?,?,?,?)
    """

    ACTUALIZAR = """
    UPDATE usuario
    SET nombre=?,
        apellido=?,
        telefono=?,
        correo=?,
        rol=?,
        estado=?
    WHERE id_usuario=?
    """

    ELIMINAR = "DELETE FROM usuario WHERE id_usuario=?"

    @classmethod
    def seleccionar(cls):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            cursor.execute(cls.SELECCIONAR)

            registros = cursor.fetchall()
            usuarios = []

            for registro in registros:
                usuario = Usuario(
                    registro[0],  # id_usuario
                    registro[1],  # nombre
                    registro[2],  # apellido
                    registro[3],  # telefono
                    registro[4],  # correo
                    registro[5],  # rol
                    registro[6],  # estado
                )

                usuarios.append(usuario)

            return usuarios

        except Exception as e:
            print(f"Ocurrió un error al seleccionar usuarios: {e}")

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    @classmethod
    def insertar(cls, usuario):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (
                usuario.id_usuario,
                usuario.nombre,
                usuario.apellido,
                usuario.telefono,
                usuario.correo,
                usuario.rol,
                usuario.estado,
            )

            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Ocurrió un error al insertar usuarios: {e}")

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    @classmethod
    def actualizar(cls, usuario):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (
                usuario.nombre,
                usuario.apellido,
                usuario.telefono,
                usuario.correo,
                usuario.rol,
                usuario.estado,
                usuario.id_usuario,
            )

            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Ocurrió un error al actualizar usuarios: {e}")

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    @classmethod
    def eliminar(cls, usuario):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valor = (usuario.id_usuario,)

            cursor.execute(cls.ELIMINAR, valor)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Ocurrió un error al eliminar usuarios: {e}")

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()


# ==========================
#  PRUEBA INSERTAR
# ==========================
if __name__ == "__main__":

    usuario1 = Usuario(
        71795830,
        "Jorge",
        "Mosquera",
        "3001234567",
        "jorge@gmail.com",
        "Administrador",
        "Activo",
    )

    registros_insertados = UsuarioDAO.insertar(usuario1)

    print(f"Usuarios insertados: {registros_insertados}")
