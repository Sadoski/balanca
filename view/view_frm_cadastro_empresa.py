# -*- coding: utf-8 -*-
"""
Modulo de controle e visualização do formulário de cadastro de empresa
"""
from PySide2 import QtCore, QtGui, QtWidgets
from formulario.frm_cadastro_empresa import FrmRegistroEmpresa
from funcoes.funcoes import Funcoes


class CadastroEmpresa(FrmRegistroEmpresa, Funcoes):

    def frm_cadastro_empresa(self, frame):
        self.set_frm_registro_empresa(frame)
        # super(CadastroEmpresa, self).set_frm_registro_empresa(frame)
        # self.fra_main_registro_empresa.show()




