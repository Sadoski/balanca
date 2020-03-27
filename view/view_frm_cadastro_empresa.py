# -*- coding: utf-8 -*-
"""
Modulo de controle e visualização do formulário de cadastro de empresa
"""
from PySide2 import QtCore, QtGui, QtWidgets
from formulario.frm_cadastro_empresa import Ui_frm_registro_empresa


class CadastroEmpresa:

    def frm_cadastro_empresa(self, frame):
        self.__ui = Ui_frm_registro_empresa()
        self.__ui.setupUi(frame)