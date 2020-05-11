# -*- coding: utf-8 -*-
"""
Modulo de controle e visualização do formulário de cadastro de cliente
"""
from PySide2 import QtCore, QtGui, QtWidgets
from formulario.frm_cadastro_cliente import FrmRegistroCliente


class CadastroCliente(FrmRegistroCliente):

    def frm_cadastro_empresa(self, frame):
        self.set_frm_registro_cliente(frame)
        #self.fra_main_registro_cliente.show()