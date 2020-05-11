# -*- coding: utf-8 -*-
"""
Modulo de controle e visualização do formulário de login
"""
from PySide2 import QtCore, QtGui, QtWidgets

from formulario.frm_login import UiFrmLogin


class Login(QtWidgets.QMainWindow):
    """
    Classe da janela principal da aplicação
    Herança:
        - QtWidgets.QMainWindow: classe pradrão do biblioteca PySide2 responsavel pela janela gráfica principal.
    """

    def __init__(self):
        """
        Inicializador da classe instanciando o formulario principal e seus componentes
        """
        QtWidgets.QMainWindow.__init__(self)
        self.__ui = UiFrmLogin()
        self.__ui.setupUi(self)

        self.__ui.btn_close.clicked.connect(self.close)
        self.__ui.btn_minimizar.clicked.connect(self.showMinimized)