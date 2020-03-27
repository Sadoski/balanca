from sqlalchemy import create_engine, exc


class Conexao:
    """
    Classe de conexão com o banco de dados
    """

    def __init__(self):
        """
        Inicializador da classe de conexão com a banco de dados
        """
        try:

            self.engine = create_engine('sqlite+pysqlcipher://:balanca@/balanca.db?cipher=aes-256-cbc&kdf_iter=64000')

        except (exc.DBAPIError, exc.InterfaceError, exc.DatabaseError, exc.DataError, exc.OperationalError,
                exc.IntegrityError, exc.InternalError, exc.ProgrammingError, exc.NotSupportedError) as err:
            error = err.orig.args[2]
            print(error)