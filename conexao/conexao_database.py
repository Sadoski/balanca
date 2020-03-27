# -*- coding: utf-8 -*-
"""
Modulo especifico para a conexão da aplicação com o banco de dados
"""
from sqlalchemy import create_engine, exc
from funcoes.controle_arquivo import ConfiguracoesDatabase, Crypt


configuracoes_data_base = ConfiguracoesDatabase()
criptografia = Crypt()


class Conexao:
    """
    Classe de conexão com o banco de dados
    """

    def __init__(self):
        """
        Inicializador da classe de conexão com a banco de dados
        """
        try:
            senha = criptografia.decrypt_base_64(configuracoes_data_base.senha)

            self.engine = create_engine('sqlite+pysqlcipher://:{}}@/{}}?cipher=aes-256-cbc&kdf_iter=64000').format(
                          senha, configuracoes_data_base.database)

        except (exc.DBAPIError, exc.InterfaceError, exc.DatabaseError, exc.DataError, exc.OperationalError,
                exc.IntegrityError, exc.InternalError, exc.ProgrammingError, exc.NotSupportedError) as err:
                error = err.orig.args[2]
                print(error)