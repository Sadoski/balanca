# -*- coding: utf-8 -*-
"""
Modulo especifico de manipulação de arquicos de configurações
"""
import sys, os, configparser
from funcoes.crypt import Crypt


path = os.path.abspath(os.path.dirname(sys.argv[0]))
config = configparser.ConfigParser()
criptografia = Crypt()


class ConfiguracoesDatabase:
    """
    Classe de capitura de informações de arquivo de confiigurações
    """
    arquivo_configuacao_database = "D:/Usuários/Jefferson/Documents/Projetos/balança/configuracoes/database.ini"
    database = ""
    senha = ""

    def __init__(self):
        """
        Inicializador da classe de capitura de informações de arquivo de configurações
        """
        if os.path.exists(self.arquivo_configuacao_database):
            if config.read(self.arquivo_configuacao_database):
                self.database = config['DEFAULT']['DATABASE']
                self.senha = config['DEFAULT']['PASSWORD']
        else:
            print('Arquivo de configuração da base de dados se encontra inexistente!')