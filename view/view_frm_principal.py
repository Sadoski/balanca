# -*- coding: utf-8 -*-
"""
Modulo de controle e visualização do formulário principal da aplicação
"""
from PySide2 import QtCore, QtGui, QtWidgets
from formulario.frm_principal import Ui_frm_principal
from view.view_frm_cadastro_empresa import CadastroEmpresa


class Principal(QtWidgets.QMainWindow):
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
        self.__ui = Ui_frm_principal()
        self.__ui.setupUi(self)

        # Inicio das ações dos botões do formulário
        self.__ui.btn_slider.clicked.connect(self.slider)
        self.__ui.btn_maximize.clicked.connect(self.maximinizar_ou_resetar)
        self.__ui.btn_maximize_rest.clicked.connect(self.maximinizar_ou_resetar)
        self.__ui.btn_close.clicked.connect(self.close)
        # Fim das ações dos botões do formulário

        # Inicio das ações dos botões dos menus Superior
        self.__ui.btn_minimizar.clicked.connect(self.showMinimized)
        self.__ui.btn_cadastro.clicked.connect(self.submenu_cadastro)
        self.__ui.btn_movimento.clicked.connect(self.submenu_movimento)
        self.__ui.btn_relatorio.clicked.connect(self.submenu_relatorio)
        self.__ui.btn_sobre.clicked.connect(self.submenu_sobre)
        self.__ui.btn_configuracao.clicked.connect(self.submenu_configuracao)
        # Fim das ações dos botões dos menus Superior

        self.__ui.btn_cadastro_empresa.clicked.connect(self.formulario_cadastro_empresa)

    def mousePressEvent(self, event):
        """
        Metodo de evento para capiturar posição onde o mouse clicou
        Parâmetro:
            - event: evento do formulário
        """
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        """
        Metoto de evento a ação de mover o formulário
        Parâmetro:
            - event: evento do formulário
        """
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def maximinizar_ou_resetar(self):
        """
        Metodo para maximizar a janela do formulário ou restaurar a forma anterior
        """
        if self.isMaximized():
            self.showNormal()
            self.__ui.btn_maximize.setVisible(True)
            self.__ui.btn_maximize_rest.setVisible(False)
        else:
            self.showMaximized()
            self.__ui.btn_maximize.setVisible(False)
            self.__ui.btn_maximize_rest.setVisible(True)

    def submenu_cadastro(self):
        """
        Metodo para visualizar ou não o sub-menu de cadastro
        """
        self.__ui.fra_submenu_cadastro.setVisible(not self.__ui.fra_submenu_cadastro.isVisible())
        self.__ui.fra_submenu_movimento.setVisible(False)
        self.__ui.fra_submenu_relatorio.setVisible(False)
        self.__ui.fra_submenu_sobre.setVisible(False)
        self.__ui.fra_submenu_configuracao.setVisible(False)

    def submenu_movimento(self):
        """
        Metodo para visualizar ou não o sub-menu de movimento
        """
        self.__ui.fra_submenu_movimento.setVisible(not self.__ui.fra_submenu_movimento.isVisible())
        self.__ui.fra_submenu_cadastro.setVisible(False)
        self.__ui.fra_submenu_relatorio.setVisible(False)
        self.__ui.fra_submenu_sobre.setVisible(False)
        self.__ui.fra_submenu_configuracao.setVisible(False)

    def submenu_relatorio(self):
        """
        Metodo para visualizar ou não o sub-menu de relatório
        """
        self.__ui.fra_submenu_relatorio.setVisible(not self.__ui.fra_submenu_relatorio.isVisible())
        self.__ui.fra_submenu_cadastro.setVisible(False)
        self.__ui.fra_submenu_movimento.setVisible(False)
        self.__ui.fra_submenu_sobre.setVisible(False)
        self.__ui.fra_submenu_configuracao.setVisible(False)

    def submenu_configuracao(self):
        """
        Metodo para visualizar ou não o sub-menu de configurações
        """
        self.__ui.fra_submenu_configuracao.setVisible(not self.__ui.fra_submenu_configuracao.isVisible())
        self.__ui.fra_submenu_cadastro.setVisible(False)
        self.__ui.fra_submenu_movimento.setVisible(False)
        self.__ui.fra_submenu_relatorio.setVisible(False)
        self.__ui.fra_submenu_sobre.setVisible(False)

    def submenu_sobre(self):
        """
        Metodo para visualizar ou não o sub-menu de Sobre
        """
        self.__ui.fra_submenu_sobre.setVisible(not self.__ui.fra_submenu_sobre.isVisible())
        self.__ui.fra_submenu_cadastro.setVisible(False)
        self.__ui.fra_submenu_movimento.setVisible(False)
        self.__ui.fra_submenu_relatorio.setVisible(False)
        self.__ui.fra_submenu_configuracao.setVisible(False)

    def slider(self):
        """
        Metodo para redimencionar a barra lateral do menu
        """
        if self.__ui.fra_menu_vertical.minimumSize().width() <= 78:
            self.__ui.fra_menu_vertical.setMinimumSize(QtCore.QSize(210, 0))
            self.__ui.fra_menu_vertical.setMaximumSize(QtCore.QSize(210, 16777215))
        else:
            self.__ui.fra_menu_vertical.setMinimumSize(QtCore.QSize(78, 0))
            self.__ui.fra_menu_vertical.setMaximumSize(QtCore.QSize(78, 16777215))

    def formulario_cadastro_empresa(self):
        cadastro_empresa = CadastroEmpresa()
        cadastro_empresa.frm_cadastro_empresa(self.__ui.fra_conteudo)