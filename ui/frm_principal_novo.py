# -*- coding: utf-8 -*-
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_frm_principal(object):
    def setupUi(self, frm_principal):
        if frm_principal.objectName():
            frm_principal.setObjectName(u"frm_principal")
        frm_principal.resize(839, 812)
        frm_principal.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"../imagens/balanca_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        frm_principal.setWindowIcon(icon)
        frm_principal.setStyleSheet(u"QMainWindow{\n"
                                    "	background: white;\n"
                                    "}")

        self.cwd_corpo_principal = QWidget(frm_principal)
        self.cwd_corpo_principal.setObjectName(u"cwd_corpo_principal"
                                               )
        self.grl_principal = QGridLayout(self.cwd_corpo_principal)
        self.grl_principal.setSpacing(0)
        self.grl_principal.setObjectName(u"grl_principal")
        self.grl_principal.setSizeConstraint(QLayout.SetMaximumSize)
        self.grl_principal.setContentsMargins(0, 0, 0, 0)

        self.fra_conteudo = QFrame(self.cwd_corpo_principal)
        self.fra_conteudo.setObjectName(u"fra_conteudo")
        self.fra_conteudo.setFrameShape(QFrame.StyledPanel)
        self.fra_conteudo.setFrameShadow(QFrame.Raised)

        self.grl_principal.addWidget(self.fra_conteudo, 1, 1, 1, 1)

        self.fra_menu_horizontal = QFrame(self.cwd_corpo_principal)
        self.fra_menu_horizontal.setObjectName(u"fra_menu_horizontal")
        self.fra_menu_horizontal.setMinimumSize(QSize(0, 41))
        self.fra_menu_horizontal.setMaximumSize(QSize(16777215, 41))
        self.fra_menu_horizontal.setStyleSheet(u"QFrame{\n"
                                               "	background: white;\n"
                                               "}")

        self.grl_menu_horizontal = QGridLayout(self.fra_menu_horizontal)
        self.grl_menu_horizontal.setSpacing(0)
        self.grl_menu_horizontal.setObjectName(u"grl_menu_horizontal")
        self.grl_menu_horizontal.setContentsMargins(5, 0, 0, 0)
        self.separador_vertical_menu_horizontal = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grl_menu_horizontal.addItem(self.separador_vertical_menu_horizontal, 0, 1, 2, 1)

        self.btn_minimizar = QPushButton(self.fra_menu_horizontal)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setStyleSheet(u"QPushButton#btn_minimizar:hover{\n"
                                         "	border: 0px solid rgba(31,31,31,.1);\n"
                                         "	background: rgba(31,31,31,.1);\n"
                                         "}\n"
                                         "QPushButton#btn_minimizar:pressed {\n"
                                         "	border: 0px solid rgba(31,31,31,.1);\n"
                                         "	background: rgba(31,31,31,.2);\n"
                                         "}\n"
                                         "QPushButton#btn_minimizar:disabled {\n"
                                         "	border: 1px solid rgba(166,166,166,1);\n"
                                         "	color: #6a6767;"
                                         "}")
        icon1 = QIcon()
        icon1.addFile(u"./imagens/minimizar-.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(16, 16))
        self.btn_minimizar.setAutoDefault(True)
        self.btn_minimizar.setFlat(True)

        self.grl_menu_horizontal.addWidget(self.btn_minimizar, 0, 3, 1, 1)

        self.btn_close = QPushButton(self.fra_menu_horizontal)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setStyleSheet(u"QPushButton#btn_close:hover{\n"
                                     "	border: 0px solid rgba(31,31,31,.1);\n"
                                     "	background: rgba(31,31,31,.1);\n"
                                     "}\n"
                                     "QPushButton#btn_close:pressed {\n"
                                     "	border: 0px solid rgba(31,31,31,.1);\n"
                                     "	background: rgba(31,31,31,.2);\n"
                                     "}\n"
                                     "QPushButton#btn_close:disabled {\n"
                                     "	border: 1px solid rgba(166,166,166,1);\n"
                                     "	color: #6a6767;"
                                     "}")
        icon2 = QIcon()
        icon2.addFile(u"./imagens/fechar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(16, 16))
        self.btn_close.setAutoDefault(True)
        self.btn_close.setFlat(True)

        self.grl_menu_horizontal.addWidget(self.btn_close, 0, 6, 1, 1)

        self.btn_maximize_rest = QPushButton(self.fra_menu_horizontal)
        self.btn_maximize_rest.setObjectName(u"btn_maximize_rest")
        self.btn_maximize_rest.setStyleSheet(u"QPushButton#btn_maximize_rest:hover{\n"
                                             "	border: 0px solid rgba(31,31,31,.1);\n"
                                             "	background: rgba(31,31,31,.1);\n"
                                             "}\n"
                                             "QPushButton#btn_maximize_rest:pressed {\n"
                                             "	border: 0px solid rgba(31,31,31,.1);\n"
                                             "	background: rgba(31,31,31,.2);\n"
                                             "}\n"
                                             "QPushButton#btn_maximize_rest:disabled {\n"
                                             "	border: 1px solid rgba(166,166,166,1);\n"
                                             "	color: #6a6767;"
                                             "}")
        icon3 = QIcon()
        icon3.addFile(u"./imagens/rest-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_rest.setIcon(icon3)
        self.btn_maximize_rest.setIconSize(QSize(16, 16))
        self.btn_maximize_rest.setAutoDefault(True)
        self.btn_maximize_rest.setFlat(True)

        self.grl_menu_horizontal.addWidget(self.btn_maximize_rest, 0, 4, 1, 1)

        self.btn_slider = QPushButton(self.fra_menu_horizontal)
        self.btn_slider.setObjectName(u"btn_slider")
        self.btn_slider.setStyleSheet(u"QPushButton#btn_slider{\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton#btn_slider:hover{\n"
                                      "	border: 1px solid rgba(31,31,31,.1);\n"
                                      "	background: rgba(31,31,31,.1);\n"
                                      "}\n"
                                      "QPushButton#btn_slider:pressed {\n"
                                      "	border: 1px solid rgba(31,31,31,.1);\n"
                                      "	background: rgba(31,31,31,.2);\n"
                                      "}\n"
                                      "QPushButton#btn_slider:disabled {\n"
                                      "	border: 1px solid rgba(166,166,166,1);\n"
                                      "	color: #6a6767;"
                                      "}")
        icon4 = QIcon()
        icon4.addFile(u"./imagens/slider.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_slider.setIcon(icon4)
        self.btn_slider.setIconSize(QSize(30, 30))
        self.btn_slider.setAutoDefault(True)
        self.btn_slider.setFlat(True)

        self.grl_menu_horizontal.addWidget(self.btn_slider, 0, 0, 2, 1)

        self.separador_horizontal_menu_horizontal = QSpacerItem(625, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_menu_horizontal.addItem(self.separador_horizontal_menu_horizontal, 0, 2, 2, 1)

        self.btn_maximize = QPushButton(self.fra_menu_horizontal)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setStyleSheet(u"QPushButton#btn_maximize:hover{\n"
                                        "	border: 0px solid rgba(31,31,31,.1);\n"
                                        "	background: rgba(31,31,31,.1);\n"
                                        "}\n"
                                        "QPushButton#btn_maximize:pressed {\n"
                                        "	border: 0px solid rgba(31,31,31,.1);\n"
                                        "	background: rgba(31,31,31,.2);\n"
                                        "}\n"
                                        "QPushButton#btn_maximize:disabled {\n"
                                        "	border: 1px solid rgba(166,166,166,1);\n"
                                        "	color: #6a6767;"
                                        "}")
        icon5 = QIcon()
        icon5.addFile(u"./imagens/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon5)
        self.btn_maximize.setIconSize(QSize(16, 16))
        self.btn_maximize.setAutoDefault(True)
        self.btn_maximize.setFlat(True)

        self.grl_menu_horizontal.addWidget(self.btn_maximize, 0, 5, 1, 1)

        self.grl_principal.addWidget(self.fra_menu_horizontal, 0, 1, 1, 1)

        self.fra_menu_vertical = QFrame(self.cwd_corpo_principal)
        self.fra_menu_vertical.setObjectName(u"fra_menu_vertical")
        self.fra_menu_vertical.setMinimumSize(QSize(80, 0))
        self.fra_menu_vertical.setMaximumSize(QSize(80, 16777215))
        self.fra_menu_vertical.setStyleSheet(u"QFrame{\n"
                                             "	background: #00beff;\n"
                                             "}")
        self.fra_menu_vertical.setFrameShape(QFrame.StyledPanel)
        self.fra_menu_vertical.setFrameShadow(QFrame.Raised)

        self.grl_menu_vertical = QGridLayout(self.fra_menu_vertical)
        self.grl_menu_vertical.setSpacing(0)
        self.grl_menu_vertical.setObjectName(u"grl_menu_vertical")
        self.grl_menu_vertical.setContentsMargins(0, 0, 0, 0)
        self.separacao_topo_logo = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_menu_vertical.addItem(self.separacao_topo_logo, 0, 2, 1, 1)

        self.separacao_borda_logo = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.grl_menu_vertical.addItem(self.separacao_borda_logo, 1, 0, 2, 2)

        self.lbl_logo = QLabel(self.fra_menu_vertical)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setMinimumSize(QSize(195, 61))
        self.lbl_logo.setMaximumSize(QSize(195, 61))
        self.lbl_logo.setTextFormat(Qt.RichText)
        self.lbl_logo.setPixmap(QPixmap(u"./imagens/BALANCA-LOGO.png"))
        self.lbl_logo.setScaledContents(True)

        self.grl_menu_vertical.addWidget(self.lbl_logo, 2, 1, 1, 2)

        self.separacao_logo_menu = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_menu_vertical.addItem(self.separacao_logo_menu, 3, 2, 1, 1)

        self.separacao_fundo_menu = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grl_menu_vertical.addItem(self.separacao_fundo_menu, 5, 2, 1, 1)

        self.grl_menu = QGridLayout()
        self.grl_menu.setSpacing(0)
        self.grl_menu.setObjectName(u"grl_menu")
        self.grl_menu.setSizeConstraint(QLayout.SetMinAndMaxSize)

        self.btn_movimento = QPushButton(self.fra_menu_vertical)
        self.btn_movimento.setObjectName(u"btn_movimento")
        self.btn_movimento.setMaximumSize(QSize(212, 32))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_movimento.setFont(font)
        self.btn_movimento.setFocusPolicy(Qt.ClickFocus)
        self.btn_movimento.setStyleSheet(u"QPushButton{\n"
                                         "	color: white;\n"
                                         "	text-align: left;\n"
                                         "	padding: 0 22px;\n"
                                         "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                         "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                         "}\n"
                                         "QPushButton#btn_movimento:hover{\n"
                                         "	border: 1px solid rgba(31,31,31,.0);\n"
                                         "	background: rgba(31,31,31,.1);\n"
                                         "}\n"
                                         "QPushButton#btn_movimento:pressed {\n"
                                         "	border: 1px solid rgba(31,31,31,.0);\n"
                                         "	background: rgba(31,31,31,.2);\n"
                                         "}\n"
                                         "QPushButton#btn_movimento:disabled {\n"
                                         "	border: 1px solid rgba(166,166,166,1);\n"
                                         "	color: #6a6767;"
                                         "}")
        icon6 = QIcon()
        icon6.addFile(u"./imagens/movimento-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_movimento.setIcon(icon6)
        self.btn_movimento.setIconSize(QSize(30, 30))
        self.btn_movimento.setFlat(True)

        self.grl_menu.addWidget(self.btn_movimento, 4, 0, 1, 1)

        self.btn_configuracao = QPushButton(self.fra_menu_vertical)
        self.btn_configuracao.setObjectName(u"btn_configuracao")
        self.btn_configuracao.setMaximumSize(QSize(212, 32))
        self.btn_configuracao.setFont(font)
        self.btn_configuracao.setFocusPolicy(Qt.ClickFocus)
        self.btn_configuracao.setStyleSheet(u"QPushButton{\n"
                                            "	color: white;\n"
                                            "	text-align: left;\n"
                                            "	padding: 0 22px;\n"
                                            "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                            "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                            "}\n"
                                            "QPushButton#btn_configuracao:hover{\n"
                                            "	border: 1px solid rgba(31,31,31,.0);\n"
                                            "	background: rgba(31,31,31,.1);\n"
                                            "}\n"
                                            "QPushButton#btn_configuracao:pressed {\n"
                                            "	border: 1px solid rgba(31,31,31,.0);\n"
                                            "	background: rgba(31,31,31,.2);\n"
                                            "}\n"
                                            "QPushButton#btn_configuracao:disabled {\n"
                                            "	border: 1px solid rgba(166,166,166,1);\n"
                                            "	color: #6a6767;"
                                            "}")
        icon7 = QIcon()
        icon7.addFile(u"../imagens/configuracao-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_configuracao.setIcon(icon7)
        self.btn_configuracao.setIconSize(QSize(30, 30))
        self.btn_configuracao.setFlat(True)

        self.grl_menu.addWidget(self.btn_configuracao, 8, 0, 1, 1)

        self.btn_sobre = QPushButton(self.fra_menu_vertical)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMaximumSize(QSize(212, 32))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setFocusPolicy(Qt.ClickFocus)
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
                                     "	color: white;\n"
                                     "	text-align: left;\n"
                                     "	padding: 0 22px;\n"
                                     "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                     "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                     "}\n"
                                     "QPushButton#btn_sobre:hover{\n"
                                     "	border: 1px solid rgba(31,31,31,.0);\n"
                                     "	background: rgba(31,31,31,.1);\n"
                                     "}\n"
                                     "QPushButton#btn_sobre:pressed {\n"
                                     "	border: 1px solid rgba(31,31,31,.0);\n"
                                     "	background: rgba(31,31,31,.2);\n"
                                     "}\n"
                                     "QPushButton#btn_sobre:disabled {\n"
                                     "	border: 1px solid rgba(166,166,166,1);\n"
                                     "	color: #6a6767;"
                                     "}")
        icon8 = QIcon()
        icon8.addFile(u"./imagens/informacoes-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sobre.setIcon(icon8)
        self.btn_sobre.setIconSize(QSize(30, 30))
        self.btn_sobre.setFlat(True)

        self.grl_menu.addWidget(self.btn_sobre, 10, 0, 1, 1)

        self.fra_submenu_sobre = QFrame(self.fra_menu_vertical)
        self.fra_submenu_sobre.setObjectName(u"fra_submenu_sobre")
        self.fra_submenu_sobre.setMinimumSize(QSize(0, 31))
        self.fra_submenu_sobre.setStyleSheet(u"QFrame {\n"
                                             "	border: 1px solid rgba(31,31,31,.1);\n"
                                             "	background: rgba(31,31,31,.1);\n"
                                             "}")
        self.fra_submenu_sobre.setFrameShape(QFrame.StyledPanel)
        self.fra_submenu_sobre.setFrameShadow(QFrame.Raised)

        self.vrl_subemenu_sobre = QVBoxLayout(self.fra_submenu_sobre)
        self.vrl_subemenu_sobre.setSpacing(0)
        self.vrl_subemenu_sobre.setObjectName(u"vrl_subemenu_sobre")
        self.vrl_subemenu_sobre.setContentsMargins(0, 0, 0, 0)

        self.btn_sobre_informacoes = QPushButton(self.fra_submenu_sobre)
        self.btn_sobre_informacoes.setObjectName(u"btn_sobre_informacoes")
        self.btn_sobre_informacoes.setMaximumSize(QSize(212, 32))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_sobre_informacoes.setFont(font1)
        self.btn_sobre_informacoes.setFocusPolicy(Qt.ClickFocus)
        self.btn_sobre_informacoes.setStyleSheet(u"QPushButton{\n"
                                                 "	color: white;\n"
                                                 "	text-align: left;\n"
                                                 "	padding: 0 26px;\n"
                                                 "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                 "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                 "}\n"
                                                 "QPushButton#btn_sobre_informacoes:hover{\n"
                                                 "	border: 1px solid rgba(31,31,31,.0);\n"
                                                 "	background: rgba(31,31,31,.1);\n"
                                                 "}\n"
                                                 "QPushButton#btn_sobre_informacoes:pressed {\n"
                                                 "	border: 1px solid rgba(31,31,31,.0);\n"
                                                 "	background: rgba(31,31,31,.2);\n"
                                                 "}\n"
                                                 "QPushButton#btn_minimizar:disabled {\n"
                                                 "	border: 1px solid rgba(166,166,166,1);\n"
                                                 "	color: #6a6767;"
                                                 "}")
        icon9 = QIcon()
        icon9.addFile(u"./imagens/informacao-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sobre_informacoes.setIcon(icon9)
        self.btn_sobre_informacoes.setIconSize(QSize(25, 25))
        self.btn_sobre_informacoes.setFlat(True)

        self.vrl_subemenu_sobre.addWidget(self.btn_sobre_informacoes)

        self.grl_menu.addWidget(self.fra_submenu_sobre, 11, 0, 1, 1)

        self.btn_cadastro = QPushButton(self.fra_menu_vertical)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setMaximumSize(QSize(212, 32))
        self.btn_cadastro.setFont(font)
        self.btn_cadastro.setFocusPolicy(Qt.ClickFocus)
        self.btn_cadastro.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	text-align: left;\n"
                                        "	padding: 0 22px;\n"
                                        "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                        "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                        "}\n"
                                        "QPushButton#btn_cadastro:hover{\n"
                                        "	border: 1px solid rgba(31,31,31,.0);\n"
                                        "	background: rgba(31,31,31,.1);\n"
                                        "}\n"
                                        "QPushButton#btn_cadastro:pressed {\n"
                                        "	border: 1px solid rgba(31,31,31,.0);\n"
                                        "	background: rgba(31,31,31,.2);\n"
                                        "}\n"
                                        "QPushButton#btn_cadastro:disabled {\n"
                                        "	border: 1px solid rgba(166,166,166,1);\n"
                                        "	color: #6a6767;"
                                        "}")
        icon10 = QIcon()
        icon10.addFile(u"./imagens/caixa_pasta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro.setIcon(icon10)
        self.btn_cadastro.setIconSize(QSize(30, 30))
        self.btn_cadastro.setFlat(True)

        self.grl_menu.addWidget(self.btn_cadastro, 2, 0, 1, 1)

        self.btn_relatorio = QPushButton(self.fra_menu_vertical)
        self.btn_relatorio.setObjectName(u"btn_relatorio")
        self.btn_relatorio.setMaximumSize(QSize(212, 32))
        self.btn_relatorio.setFont(font)
        self.btn_relatorio.setFocusPolicy(Qt.ClickFocus)
        self.btn_relatorio.setStyleSheet(u"QPushButton{\n"
                                         "	color: white;\n"
                                         "	text-align: left;\n"
                                         "	padding: 0 22px;\n"
                                         "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                         "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                         "}\n"
                                         "QPushButton#btn_relatorio:hover{\n"
                                         "	border: 1px solid rgba(31,31,31,.0);\n"
                                         "	background: rgba(31,31,31,.1);\n"
                                         "}\n"
                                         "QPushButton#btn_relatorio:pressed {\n"
                                         "	border: 1px solid rgba(31,31,31,.0);\n"
                                         "	background: rgba(31,31,31,.2);\n"
                                         "}\n"
                                         "QPushButton#btn_relatorio:disabled {\n"
                                         "	border: 1px solid rgba(166,166,166,1);\n"
                                         "	color: #6a6767;"
                                         "}")
        icon11 = QIcon()
        icon11.addFile(u"./imagens/relatorio-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorio.setIcon(icon11)
        self.btn_relatorio.setIconSize(QSize(30, 30))
        self.btn_relatorio.setFlat(True)

        self.grl_menu.addWidget(self.btn_relatorio, 6, 0, 1, 1)

        self.vsb_menu = QScrollBar(self.fra_menu_vertical)
        self.vsb_menu.setObjectName(u"vsb_menu")
        self.vsb_menu.setMinimumSize(QSize(12, 0))
        self.vsb_menu.setMaximumSize(QSize(10, 16777215))

        self.grl_menu.addWidget(self.vsb_menu, 2, 1, 10, 1)

        self.fra_submenu_relatorio = QFrame(self.fra_menu_vertical)
        self.fra_submenu_relatorio.setObjectName(u"fra_submenu_relatorio")
        self.fra_submenu_relatorio.setMinimumSize(QSize(0, 91))
        self.fra_submenu_relatorio.setStyleSheet(u"QFrame {\n"
                                                 "	border: 1px solid rgba(31,31,31,.1);\n"
                                                 "	background: rgba(31,31,31,.1);\n"
                                                 "}")
        self.fra_submenu_relatorio.setFrameShape(QFrame.StyledPanel)
        self.fra_submenu_relatorio.setFrameShadow(QFrame.Raised)

        self.vrl_submenu_relatorio = QVBoxLayout(self.fra_submenu_relatorio)
        self.vrl_submenu_relatorio.setSpacing(0)
        self.vrl_submenu_relatorio.setObjectName(u"vrl_submenu_relatorio")
        self.vrl_submenu_relatorio.setContentsMargins(0, 0, 0, 0)

        self.btn_relatorio_cadastros = QPushButton(self.fra_submenu_relatorio)
        self.btn_relatorio_cadastros.setObjectName(u"btn_relatorio_cadastros")
        self.btn_relatorio_cadastros.setMaximumSize(QSize(212, 32))
        self.btn_relatorio_cadastros.setFont(font1)
        self.btn_relatorio_cadastros.setFocusPolicy(Qt.ClickFocus)
        self.btn_relatorio_cadastros.setStyleSheet(u"QPushButton{\n"
                                                   "	color: white;\n"
                                                   "	text-align: left;\n"
                                                   "	padding: 0 26px;\n"
                                                   "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                   "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                   "}\n"
                                                   "QPushButton#btn_relatorio_cadastros:hover{\n"
                                                   "	border: 1px solid rgba(31,31,31,.0);\n"
                                                   "	background: rgba(31,31,31,.1);\n"
                                                   "}\n"
                                                   "QPushButton#btn_relatorio_cadastros:pressed {\n"
                                                   "	border: 1px solid rgba(31,31,31,.0);\n"
                                                   "	background: rgba(31,31,31,.2);\n"
                                                   "}\n"
                                                   "QPushButton#btn_relatorio_cadastros:disabled {\n"
                                                   "	border: 1px solid rgba(166,166,166,1);\n"
                                                   "	color: #6a6767;"
                                                   "}")
        icon12 = QIcon()
        icon12.addFile(u"./imagens/relatorio-cadastros-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorio_cadastros.setIcon(icon12)
        self.btn_relatorio_cadastros.setIconSize(QSize(25, 25))
        self.btn_relatorio_cadastros.setFlat(True)

        self.vrl_submenu_relatorio.addWidget(self.btn_relatorio_cadastros)

        self.btn_relatorio_caixa = QPushButton(self.fra_submenu_relatorio)
        self.btn_relatorio_caixa.setObjectName(u"btn_relatorio_caixa")
        self.btn_relatorio_caixa.setMaximumSize(QSize(212, 32))
        self.btn_relatorio_caixa.setFont(font1)
        self.btn_relatorio_caixa.setFocusPolicy(Qt.ClickFocus)
        self.btn_relatorio_caixa.setStyleSheet(u"QPushButton{\n"
                                               "	color: white;\n"
                                               "	text-align: left;\n"
                                               "	padding: 0 26px;\n"
                                               "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                               "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                               "}\n"
                                               "QPushButton#btn_relatorio_caixa:hover{\n"
                                               "	border: 1px solid rgba(31,31,31,.0);\n"
                                               "	background: rgba(31,31,31,.1);\n"
                                               "}\n"
                                               "QPushButton#btn_relatorio_caixa:pressed {\n"
                                               "	border: 1px solid rgba(31,31,31,.0);\n"
                                               "	background: rgba(31,31,31,.2);\n"
                                               "}\n"
                                               "QPushButton#btn_relatorio_caixa:disabled {\n"
                                               "	border: 1px solid rgba(166,166,166,1);\n"
                                               "	color: #6a6767;"
                                               "}")
        icon13 = QIcon()
        icon13.addFile(u"./imagens/relatorio-caixa-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorio_caixa.setIcon(icon13)
        self.btn_relatorio_caixa.setIconSize(QSize(25, 25))
        self.btn_relatorio_caixa.setFlat(True)

        self.vrl_submenu_relatorio.addWidget(self.btn_relatorio_caixa)

        self.btn_relatorio_pesos = QPushButton(self.fra_submenu_relatorio)
        self.btn_relatorio_pesos.setObjectName(u"btn_relatorio_pesos")
        self.btn_relatorio_pesos.setMaximumSize(QSize(212, 32))
        self.btn_relatorio_pesos.setFont(font1)
        self.btn_relatorio_pesos.setFocusPolicy(Qt.ClickFocus)
        self.btn_relatorio_pesos.setStyleSheet(u"QPushButton{\n"
                                               "	color: white;\n"
                                               "	text-align: left;\n"
                                               "	padding: 0 26px;\n"
                                               "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                               "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                               "}\n"
                                               "QPushButton#btn_relatorio_pesos:hover{\n"
                                               "	border: 1px solid rgba(31,31,31,.0);\n"
                                               "	background: rgba(31,31,31,.1);\n"
                                               "}\n"
                                               "QPushButton#btn_relatorio_pesos:pressed {\n"
                                               "	border: 1px solid rgba(31,31,31,.0);\n"
                                               "	background: rgba(31,31,31,.2);\n"
                                               "}\n"
                                               "QPushButton#btn_relatorio_pesos:disabled {\n"
                                               "	border: 1px solid rgba(166,166,166,1);\n"
                                               "	color: #6a6767;"
                                               "}")
        icon14 = QIcon()
        icon14.addFile(u"./imagens/relatorio-pesos-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorio_pesos.setIcon(icon14)
        self.btn_relatorio_pesos.setIconSize(QSize(25, 25))
        self.btn_relatorio_pesos.setFlat(True)

        self.vrl_submenu_relatorio.addWidget(self.btn_relatorio_pesos)

        self.grl_menu.addWidget(self.fra_submenu_relatorio, 7, 0, 1, 1)

        self.fra_submenu_cadastro = QFrame(self.fra_menu_vertical)
        self.fra_submenu_cadastro.setObjectName(u"fra_submenu_cadastro")
        self.fra_submenu_cadastro.setMinimumSize(QSize(78, 235))
        self.fra_submenu_cadastro.setStyleSheet(u"QFrame {\n"
                                                "	border: 1px solid rgba(31,31,31,.1);\n"
                                                "	background: rgba(31,31,31,.1);\n"
                                                "}")
        self.fra_submenu_cadastro.setFrameShape(QFrame.StyledPanel)
        self.fra_submenu_cadastro.setFrameShadow(QFrame.Raised)

        self.vrl_submenu_cadastro = QVBoxLayout(self.fra_submenu_cadastro)
        self.vrl_submenu_cadastro.setSpacing(0)
        self.vrl_submenu_cadastro.setObjectName(u"vrl_submenu_cadastro")
        self.vrl_submenu_cadastro.setContentsMargins(0, 0, 0, 0)

        self.btn_cadastro_empresa = QPushButton(self.fra_submenu_cadastro)
        self.btn_cadastro_empresa.setObjectName(u"btn_cadastro_empresa")
        self.btn_cadastro_empresa.setMaximumSize(QSize(212, 32))
        self.btn_cadastro_empresa.setFont(font1)
        self.btn_cadastro_empresa.setFocusPolicy(Qt.ClickFocus)
        self.btn_cadastro_empresa.setStyleSheet(u"QPushButton{\n"
                                                "	color: white;\n"
                                                "	text-align: left;\n"
                                                "	padding: 0 26px;\n"
                                                "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_empresa:hover{\n"
                                                "	border: 1px solid rgba(31,31,31,.0);\n"
                                                "	background: rgba(31,31,31,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_empresa:pressed {\n"
                                                "	border: 1px solid rgba(31,31,31,.0);\n"
                                                "	background: rgba(31,31,31,.2);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_empresa:disabled {\n"
                                                "	border: 1px solid rgba(166,166,166,1);\n"
                                                "	color: #6a6767;"
                                                "}")
        icon15 = QIcon()
        icon15.addFile(u"./imagens/empresa-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro_empresa.setIcon(icon15)
        self.btn_cadastro_empresa.setIconSize(QSize(25, 25))
        self.btn_cadastro_empresa.setFlat(True)

        self.vrl_submenu_cadastro.addWidget(self.btn_cadastro_empresa)

        self.btn_cadastro_cliente = QPushButton(self.fra_submenu_cadastro)
        self.btn_cadastro_cliente.setObjectName(u"btn_cadastro_cliente")
        self.btn_cadastro_cliente.setMaximumSize(QSize(212, 32))
        self.btn_cadastro_cliente.setFont(font1)
        self.btn_cadastro_cliente.setFocusPolicy(Qt.ClickFocus)
        self.btn_cadastro_cliente.setStyleSheet(u"QPushButton{\n"
                                                "	color: white;\n"
                                                "	text-align: left;\n"
                                                "	padding: 0 26px;\n"
                                                "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_cliente:hover{\n"
                                                "	border: 1px solid rgba(31,31,31,.0);\n"
                                                "	background: rgba(31,31,31,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_cliente:pressed {\n"
                                                "	border: 1px solid rgba(31,31,31,.0);\n"
                                                "	background: rgba(31,31,31,.2);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_cliente:disabled {\n"
                                                "	border: 1px solid rgba(166,166,166,1);\n"
                                                "	color: #6a6767;"
                                                "}")
        icon16 = QIcon()
        icon16.addFile(u"./imagens/cliente-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro_cliente.setIcon(icon16)
        self.btn_cadastro_cliente.setIconSize(QSize(25, 25))
        self.btn_cadastro_cliente.setFlat(True)

        self.vrl_submenu_cadastro.addWidget(self.btn_cadastro_cliente)

        self.btn_cadastro_fornecedor = QPushButton(self.fra_submenu_cadastro)
        self.btn_cadastro_fornecedor.setObjectName(u"btn_cadastro_fornecedor")
        self.btn_cadastro_fornecedor.setMaximumSize(QSize(212, 32))
        self.btn_cadastro_fornecedor.setFont(font1)
        self.btn_cadastro_fornecedor.setFocusPolicy(Qt.ClickFocus)
        self.btn_cadastro_fornecedor.setStyleSheet(u"QPushButton{\n"
                                                   "	color: white;\n"
                                                   "	text-align: left;\n"
                                                   "	padding: 0 26px;\n"
                                                   "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                   "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                   "}\n"
                                                   "QPushButton#btn_cadastro_fornecedor:hover{\n"
                                                   "	border: 1px solid rgba(31,31,31,.0);\n"
                                                   "	background: rgba(31,31,31,.1);\n"
                                                   "}\n"
                                                   "QPushButton#btn_cadastro_fornecedor:pressed {\n"
                                                   "	border: 1px solid rgba(31,31,31,.0);\n"
                                                   "	background: rgba(31,31,31,.2);\n"
                                                   "}\n"
                                                   "QPushButton#btn_cadastro_fornecedor:disabled {\n"
                                                   "	border: 1px solid rgba(166,166,166,1);\n"
                                                   "	color: #6a6767;"
                                                   "}")
        icon17 = QIcon()
        icon17.addFile(u"./imagens/fornecedor-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro_fornecedor.setIcon(icon17)
        self.btn_cadastro_fornecedor.setIconSize(QSize(25, 25))
        self.btn_cadastro_fornecedor.setFlat(True)

        self.vrl_submenu_cadastro.addWidget(self.btn_cadastro_fornecedor)

        self.btn_cadastro_transportadora = QPushButton(self.fra_submenu_cadastro)
        self.btn_cadastro_transportadora.setObjectName(u"btn_cadastro_transportadora")
        self.btn_cadastro_transportadora.setMaximumSize(QSize(212, 32))
        self.btn_cadastro_transportadora.setFont(font1)
        self.btn_cadastro_transportadora.setFocusPolicy(Qt.ClickFocus)
        self.btn_cadastro_transportadora.setStyleSheet(u"QPushButton{\n"
                                                       "	color: white;\n"
                                                       "	text-align: left;\n"
                                                       "	padding: 0 26px;\n"
                                                       "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                       "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                       "}\n"
                                                       "QPushButton#btn_cadastro_transportadora:hover{\n"
                                                       "	border: 1px solid rgba(31,31,31,.0);\n"
                                                       "	background: rgba(31,31,31,.1);\n"
                                                       "}\n"
                                                       "QPushButton#btn_cadastro_transportadora:pressed {\n"
                                                       "	border: 1px solid rgba(31,31,31,.0);\n"
                                                       "	background: rgba(31,31,31,.2);\n"
                                                       "}\n"
                                                       "QPushButton#btn_cadastro_transportadora:disabled {\n"
                                                       "	border: 1px solid rgba(166,166,166,1);\n"
                                                       "	color: #6a6767;"
                                                       "}")
        icon18 = QIcon()
        icon18.addFile(u"./imagens/transportadora-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro_transportadora.setIcon(icon18)
        self.btn_cadastro_transportadora.setIconSize(QSize(25, 25))
        self.btn_cadastro_transportadora.setFlat(True)

        self.vrl_submenu_cadastro.addWidget(self.btn_cadastro_transportadora)

        self.btn_cadastro_motorista = QPushButton(self.fra_submenu_cadastro)
        self.btn_cadastro_motorista.setObjectName(u"btn_cadastro_motorista")
        self.btn_cadastro_motorista.setMaximumSize(QSize(212, 32))
        self.btn_cadastro_motorista.setFont(font1)
        self.btn_cadastro_motorista.setFocusPolicy(Qt.ClickFocus)
        self.btn_cadastro_motorista.setStyleSheet(u"QPushButton{\n"
                                                  "	color: white;\n"
                                                  "	text-align: left;\n"
                                                  "	padding: 0 26px;\n"
                                                  "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                  "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                  "}\n"
                                                  "QPushButton#btn_cadastro_motorista:hover{\n"
                                                  "	border: 1px solid rgba(31,31,31,.0);\n"
                                                  "	background: rgba(31,31,31,.1);\n"
                                                  "}\n"
                                                  "QPushButton#btn_cadastro_motorista:pressed {\n"
                                                  "	border: 1px solid rgba(31,31,31,.0);\n"
                                                  "	background: rgba(31,31,31,.2);\n"
                                                  "}\n"
                                                  "QPushButton#btn_cadastro_motorista:disabled {\n"
                                                  "	border: 1px solid rgba(166,166,166,1);\n"
                                                  "	color: #6a6767;"
                                                  "}")
        icon19 = QIcon()
        icon19.addFile(u"./imagens/motorista-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro_motorista.setIcon(icon19)
        self.btn_cadastro_motorista.setIconSize(QSize(25, 25))
        self.btn_cadastro_motorista.setFlat(True)

        self.vrl_submenu_cadastro.addWidget(self.btn_cadastro_motorista)

        self.btn_cadastro_veiculo = QPushButton(self.fra_submenu_cadastro)
        self.btn_cadastro_veiculo.setObjectName(u"btn_cadastro_veiculo")
        self.btn_cadastro_veiculo.setMaximumSize(QSize(212, 32))
        self.btn_cadastro_veiculo.setFont(font1)
        self.btn_cadastro_veiculo.setFocusPolicy(Qt.ClickFocus)
        self.btn_cadastro_veiculo.setStyleSheet(u"QPushButton{\n"
                                                "	color: white;\n"
                                                "	text-align: left;\n"
                                                "	padding: 0 26px;\n"
                                                "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_veiculo:hover{\n"
                                                "	border: 1px solid rgba(31,31,31,.0);\n"
                                                "	background: rgba(31,31,31,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_veiculo:pressed {\n"
                                                "	border: 1px solid rgba(31,31,31,.0);\n"
                                                "	background: rgba(31,31,31,.2);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_veiculo:disabled {\n"
                                                "	border: 1px solid rgba(166,166,166,1);\n"
                                                "	color: #6a6767;"
                                                "}")
        icon20 = QIcon()
        icon20.addFile(u"./imagens/veiculo-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro_veiculo.setIcon(icon20)
        self.btn_cadastro_veiculo.setIconSize(QSize(25, 25))
        self.btn_cadastro_veiculo.setFlat(True)

        self.vrl_submenu_cadastro.addWidget(self.btn_cadastro_veiculo)

        self.btn_cadastro_usuario = QPushButton(self.fra_submenu_cadastro)
        self.btn_cadastro_usuario.setObjectName(u"btn_cadastro_usuario")
        self.btn_cadastro_usuario.setMaximumSize(QSize(212, 32))
        self.btn_cadastro_usuario.setFont(font1)
        self.btn_cadastro_usuario.setFocusPolicy(Qt.ClickFocus)
        self.btn_cadastro_usuario.setStyleSheet(u"QPushButton{\n"
                                                "	color: white;\n"
                                                "	text-align: left;\n"
                                                "	padding: 0 26px;\n"
                                                "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_usuario:hover{\n"
                                                "	border: 1px solid rgba(31,31,31,.0);\n"
                                                "	background: rgba(31,31,31,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_usuario:pressed {\n"
                                                "	border: 1px solid rgba(31,31,31,.0);\n"
                                                "	background: rgba(31,31,31,.2);\n"
                                                "}\n"
                                                "QPushButton#btn_cadastro_usuario:disabled {\n"
                                                "	border: 1px solid rgba(166,166,166,1);\n"
                                                "	color: #6a6767;"
                                                "}")
        icon21 = QIcon()
        icon21.addFile(u"./imagens/usuario-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro_usuario.setIcon(icon21)
        self.btn_cadastro_usuario.setIconSize(QSize(25, 25))
        self.btn_cadastro_usuario.setFlat(True)

        self.vrl_submenu_cadastro.addWidget(self.btn_cadastro_usuario)

        self.btn_cadastro_permissao = QPushButton(self.fra_submenu_cadastro)
        self.btn_cadastro_permissao.setObjectName(u"btn_cadastro_permissao")
        self.btn_cadastro_permissao.setMaximumSize(QSize(212, 32))
        self.btn_cadastro_permissao.setFont(font1)
        self.btn_cadastro_permissao.setFocusPolicy(Qt.ClickFocus)
        self.btn_cadastro_permissao.setStyleSheet(u"QPushButton{\n"
                                                  "	color: white;\n"
                                                  "	text-align: left;\n"
                                                  "	padding: 0 26px;\n"
                                                  "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                  "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                  "}\n"
                                                  "QPushButton#btn_cadastro_permissao:hover{\n"
                                                  "	border: 1px solid rgba(31,31,31,.0);\n"
                                                  "	background: rgba(31,31,31,.1);\n"
                                                  "}\n"
                                                  "QPushButton#btn_cadastro_permissao:pressed {\n"
                                                  "	border: 1px solid rgba(31,31,31,.0);\n"
                                                  "	background: rgba(31,31,31,.2);\n"
                                                  "}\n"
                                                  "QPushButton#btn_cadastro_permissao:disabled {\n"
                                                  "	border: 1px solid rgba(166,166,166,1);\n"
                                                  "	color: #6a6767;"
                                                  "}")
        icon22 = QIcon()
        icon22.addFile(u"./imagens/usuario_cadeado-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro_permissao.setIcon(icon22)
        self.btn_cadastro_permissao.setIconSize(QSize(25, 25))
        self.btn_cadastro_permissao.setFlat(True)

        self.vrl_submenu_cadastro.addWidget(self.btn_cadastro_permissao)

        self.grl_menu.addWidget(self.fra_submenu_cadastro, 3, 0, 1, 1)

        self.fra_submenu_configuracao = QFrame(self.fra_menu_vertical)
        self.fra_submenu_configuracao.setObjectName(u"fra_submenu_configuracao")
        self.fra_submenu_configuracao.setMinimumSize(QSize(0, 61))
        self.fra_submenu_configuracao.setStyleSheet(u"QFrame {\n"
                                                    "	border: 1px solid rgba(31,31,31,.1);\n"
                                                    "	background: rgba(31,31,31,.1);\n"
                                                    "}")
        self.fra_submenu_configuracao.setFrameShape(QFrame.StyledPanel)
        self.fra_submenu_configuracao.setFrameShadow(QFrame.Raised)

        self.vrl_submenu_configuracao = QVBoxLayout(self.fra_submenu_configuracao)
        self.vrl_submenu_configuracao.setSpacing(0)
        self.vrl_submenu_configuracao.setObjectName(u"vrl_submenu_configuracao")
        self.vrl_submenu_configuracao.setContentsMargins(0, 0, 0, 0)

        self.btn_configuracao_balanca = QPushButton(self.fra_submenu_configuracao)
        self.btn_configuracao_balanca.setObjectName(u"btn_configuracao_balanca")
        self.btn_configuracao_balanca.setMaximumSize(QSize(212, 32))
        self.btn_configuracao_balanca.setFont(font1)
        self.btn_configuracao_balanca.setFocusPolicy(Qt.ClickFocus)
        self.btn_configuracao_balanca.setStyleSheet(u"QPushButton{\n"
                                                    "	color: white;\n"
                                                    "	text-align: left;\n"
                                                    "	padding: 0 26px;\n"
                                                    "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                    "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                    "}\n"
                                                    "QPushButton#btn_configuracao_balanca:hover{\n"
                                                    "	border: 1px solid rgba(31,31,31,.0);\n"
                                                    "	background: rgba(31,31,31,.1);\n"
                                                    "}\n"
                                                    "QPushButton#btn_configuracao_balanca:pressed {\n"
                                                    "	border: 1px solid rgba(31,31,31,.0);\n"
                                                    "	background: rgba(31,31,31,.2);\n"
                                                    "}\n"
                                                    "QPushButton#btn_configuracao_balanca:disabled {\n"
                                                    "	border: 1px solid rgba(166,166,166,1);\n"
                                                    "	color: #6a6767;"
                                                    "}")
        icon23 = QIcon()
        icon23.addFile(u"./imagens/balanca-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_configuracao_balanca.setIcon(icon23)
        self.btn_configuracao_balanca.setIconSize(QSize(25, 25))
        self.btn_configuracao_balanca.setFlat(True)

        self.vrl_submenu_configuracao.addWidget(self.btn_configuracao_balanca)

        self.btn_configuracao_sistema = QPushButton(self.fra_submenu_configuracao)
        self.btn_configuracao_sistema.setObjectName(u"btn_configuracao_sistema")
        self.btn_configuracao_sistema.setMaximumSize(QSize(212, 32))
        self.btn_configuracao_sistema.setFont(font1)
        self.btn_configuracao_sistema.setFocusPolicy(Qt.ClickFocus)
        self.btn_configuracao_sistema.setStyleSheet(u"QPushButton{\n"
                                                    "	color: white;\n"
                                                    "	text-align: left;\n"
                                                    "	padding: 0 26px;\n"
                                                    "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                                    "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                                    "}\n"
                                                    "QPushButton#btn_configuracao_sistema:hover{\n"
                                                    "	border: 1px solid rgba(31,31,31,.0);\n"
                                                    "	background: rgba(31,31,31,.1);\n"
                                                    "}\n"
                                                    "QPushButton#btn_configuracao_sistema:pressed {\n"
                                                    "	border: 1px solid rgba(31,31,31,.0);\n"
                                                    "	background: rgba(31,31,31,.2);\n"
                                                    "}\n"
                                                    "QPushButton#btn_configuracao_sistema:disabled {\n"
                                                    "	border: 1px solid rgba(166,166,166,1);\n"
                                                    "	color: #6a6767;"
                                                    "}")
        icon24 = QIcon()
        icon24.addFile(u"./imagens/configuracao-sistema-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_configuracao_sistema.setIcon(icon24)
        self.btn_configuracao_sistema.setIconSize(QSize(25, 25))
        self.btn_configuracao_sistema.setFlat(True)

        self.vrl_submenu_configuracao.addWidget(self.btn_configuracao_sistema)

        self.grl_menu.addWidget(self.fra_submenu_configuracao, 9, 0, 1, 1)

        self.fra_submenu_movimento = QFrame(self.fra_menu_vertical)
        self.fra_submenu_movimento.setObjectName(u"fra_submenu_movimento")
        self.fra_submenu_movimento.setMinimumSize(QSize(0, 61))
        self.fra_submenu_movimento.setStyleSheet(u"QFrame {\n"
                                                 "	border: 1px solid rgba(31,31,31,.1);\n"
                                                 "	background: rgba(31,31,31,.1);\n"
                                                 "}")
        self.fra_submenu_movimento.setFrameShape(QFrame.StyledPanel)
        self.fra_submenu_movimento.setFrameShadow(QFrame.Raised)

        self.vrl_submenu_movimento = QVBoxLayout(self.fra_submenu_movimento)
        self.vrl_submenu_movimento.setSpacing(0)
        self.vrl_submenu_movimento.setObjectName(u"vrl_submenu_movimento")
        self.vrl_submenu_movimento.setContentsMargins(0, 0, 0, 0)

        self.btn_movimento_pesar = QPushButton(self.fra_submenu_movimento)
        self.btn_movimento_pesar.setObjectName(u"btn_movimento_pesar")
        self.btn_movimento_pesar.setMaximumSize(QSize(212, 32))
        self.btn_movimento_pesar.setFont(font1)
        self.btn_movimento_pesar.setFocusPolicy(Qt.ClickFocus)
        self.btn_movimento_pesar.setStyleSheet(u"QPushButton{\n"
                                               "	color: white;\n"
                                               "	text-align: left;\n"
                                               "	padding: 0 26px;\n"
                                               "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                               "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                               "}\n"
                                               "QPushButton#btn_movimento_pesar:hover{\n"
                                               "	border: 1px solid rgba(31,31,31,.0);\n"
                                               "	background: rgba(31,31,31,.1);\n"
                                               "}\n"
                                               "QPushButton#btn_movimento_pesar:pressed {\n"
                                               "	border: 1px solid rgba(31,31,31,.0);\n"
                                               "	background: rgba(31,31,31,.2);\n"
                                               "}\n"
                                               "QPushButton#btn_movimento_pesar:disabled {\n"
                                               "	border: 1px solid rgba(166,166,166,1);\n"
                                               "	color: #6a6767;"
                                               "}")
        icon25 = QIcon()
        icon25.addFile(u"./imagens/pesar_veiculo-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_movimento_pesar.setIcon(icon25)
        self.btn_movimento_pesar.setIconSize(QSize(25, 25))
        self.btn_movimento_pesar.setFlat(True)

        self.vrl_submenu_movimento.addWidget(self.btn_movimento_pesar)

        self.btn_movimento_caixa = QPushButton(self.fra_submenu_movimento)
        self.btn_movimento_caixa.setObjectName(u"btn_movimento_caixa")
        self.btn_movimento_caixa.setMaximumSize(QSize(212, 32))
        self.btn_movimento_caixa.setFont(font1)
        self.btn_movimento_caixa.setFocusPolicy(Qt.ClickFocus)
        self.btn_movimento_caixa.setStyleSheet(u"QPushButton{\n"
                                               "	color: white;\n"
                                               "	text-align: left;\n"
                                               "	padding: 0 26px;\n"
                                               "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                               "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                               "}\n"
                                               "QPushButton#btn_movimento_caixa:hover{\n"
                                               "	border: 1px solid rgba(31,31,31,.0);\n"
                                               "	background: rgba(31,31,31,.1);\n"
                                               "}\n"
                                               "QPushButton#btn_movimento_caixa:pressed {\n"
                                               "	border: 1px solid rgba(31,31,31,.0);\n"
                                               "	background: rgba(31,31,31,.2);\n"
                                               "}\n"
                                               "QPushButton#btn_movimento_caixa:disabled {\n"
                                               "	border: 1px solid rgba(166,166,166,1);\n"
                                               "	color: #6a6767;"
                                               "}")
        icon26 = QIcon()
        icon26.addFile(u"./imagens/moeda-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_movimento_caixa.setIcon(icon26)
        self.btn_movimento_caixa.setIconSize(QSize(25, 25))
        self.btn_movimento_caixa.setFlat(True)

        self.vrl_submenu_movimento.addWidget(self.btn_movimento_caixa)

        self.grl_menu.addWidget(self.fra_submenu_movimento, 5, 0, 1, 1)

        self.btn_inicio = QPushButton(self.fra_menu_vertical)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setMaximumSize(QSize(212, 32))
        self.btn_inicio.setFont(font)
        self.btn_inicio.setFocusPolicy(Qt.ClickFocus)
        self.btn_inicio.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	text-align: left;\n"
                                      "	padding: 0 22px;\n"
                                      "	border-top: 1px solid rgba(250,250,250,.1);\n"
                                      "    border-bottom: 1px solid rgba(250,250,250,.1);\n"
                                      "}\n"
                                      "QPushButton#btn_inicio:hover{\n"
                                      "	border: 1px solid rgba(31,31,31,.0);\n"
                                      "	background: rgba(31,31,31,.1);\n"
                                      "}\n"
                                      "QPushButton#btn_inicio:pressed {\n"
                                      "	border: 1px solid rgba(31,31,31,.0);\n"
                                      "	background: rgba(31,31,31,.2);\n"
                                      "}\n"
                                      "QPushButton#btn_inicio:disabled {\n"
                                      "	border: 1px solid rgba(166,166,166,1);\n"
                                      "	color: #6a6767;"
                                      "}")
        icon27 = QIcon()
        icon27.addFile(u"./imagens/inico-vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inicio.setIcon(icon27)
        self.btn_inicio.setIconSize(QSize(30, 30))
        self.btn_inicio.setFlat(True)

        self.grl_menu.addWidget(self.btn_inicio, 1, 0, 1, 2)

        self.grl_menu_vertical.addLayout(self.grl_menu, 4, 0, 1, 3)

        self.grl_principal.addWidget(self.fra_menu_vertical, 0, 0, 2, 1)

        frm_principal.setCentralWidget(self.cwd_corpo_principal)

        self.retranslateUi(frm_principal)

        self.btn_slider.setDefault(False)

        QMetaObject.connectSlotsByName(frm_principal)

    def retranslateUi(self, frm_principal):
        frm_principal.setWindowTitle(QCoreApplication.translate("frm_principal", u"Balan\u00e7a", None))
        self.btn_minimizar.setText("")
        self.btn_close.setText("")
        self.btn_maximize_rest.setText("")
        self.btn_slider.setText("")
        self.btn_maximize.setText("")
        self.lbl_logo.setText("")
        self.btn_movimento.setToolTip(QCoreApplication.translate("frm_principal", u"Movimento", None))
        self.btn_movimento.setText(QCoreApplication.translate("frm_principal", u"    Movimento", None))
        self.btn_configuracao.setToolTip(QCoreApplication.translate("frm_principal", u"Relat\u00f3rio", None))
        self.btn_configuracao.setText(QCoreApplication.translate("frm_principal", u"    Configura\u00e7\u00e3o", None))
        self.btn_sobre.setToolTip(QCoreApplication.translate("frm_principal", u"Sobre", None))
        self.btn_sobre.setText(QCoreApplication.translate("frm_principal", u"    Sobre", None))
        self.btn_sobre_informacoes.setToolTip(QCoreApplication.translate("frm_principal", u"Informa\u00e7\u00f5es", None))
        self.btn_sobre_informacoes.setText(QCoreApplication.translate("frm_principal", u"      Informa\u00e7\u00f5es", None))
        self.btn_cadastro.setToolTip(QCoreApplication.translate("frm_principal", u"Cadastro", None))
        self.btn_cadastro.setText(QCoreApplication.translate("frm_principal", u"    Cadastro", None))
        self.btn_relatorio.setToolTip(QCoreApplication.translate("frm_principal", u"Relat\u00f3rio", None))
        self.btn_relatorio.setText(QCoreApplication.translate("frm_principal", u"    Relat\u00f3rio", None))
        self.btn_relatorio_cadastros.setToolTip(QCoreApplication.translate("frm_principal", u"Cadastros", None))
        self.btn_relatorio_cadastros.setText(QCoreApplication.translate("frm_principal", u"      Cadastros", None))
        self.btn_relatorio_caixa.setToolTip(QCoreApplication.translate("frm_principal", u"Caixa", None))
        self.btn_relatorio_caixa.setText(QCoreApplication.translate("frm_principal", u"      Caixa", None))
        self.btn_relatorio_pesos.setToolTip(QCoreApplication.translate("frm_principal", u"Pesos", None))
        self.btn_relatorio_pesos.setText(QCoreApplication.translate("frm_principal", u"      Pesos", None))
        self.btn_cadastro_empresa.setToolTip(QCoreApplication.translate("frm_principal", u"Empresa", None))
        self.btn_cadastro_empresa.setText(QCoreApplication.translate("frm_principal", u"      Empresa", None))
        self.btn_cadastro_cliente.setToolTip(QCoreApplication.translate("frm_principal", u"Cliente", None))
        self.btn_cadastro_cliente.setText(QCoreApplication.translate("frm_principal", u"      Cliente", None))
        self.btn_cadastro_fornecedor.setToolTip(QCoreApplication.translate("frm_principal", u"Fornecedor", None))
        self.btn_cadastro_fornecedor.setText(QCoreApplication.translate("frm_principal", u"      Fornecedor", None))
        self.btn_cadastro_transportadora.setToolTip(QCoreApplication.translate("frm_principal", u"Transportadora", None))
        self.btn_cadastro_transportadora.setText(QCoreApplication.translate("frm_principal", u"      Transportadora", None))
        self.btn_cadastro_motorista.setToolTip(QCoreApplication.translate("frm_principal", u"Motorista", None))
        self.btn_cadastro_motorista.setText(QCoreApplication.translate("frm_principal", u"      Motorista", None))
        self.btn_cadastro_veiculo.setToolTip(QCoreApplication.translate("frm_principal", u"Ve\u00edculo", None))
        self.btn_cadastro_veiculo.setText(QCoreApplication.translate("frm_principal", u"      Ve\u00edculo", None))
        self.btn_cadastro_usuario.setToolTip(QCoreApplication.translate("frm_principal", u"Usu\u00e1rio", None))
        self.btn_cadastro_usuario.setText(QCoreApplication.translate("frm_principal", u"      Usu\u00e1rio", None))
        self.btn_cadastro_permissao.setToolTip(QCoreApplication.translate("frm_principal", u"Permiss\u00e3o", None))
        self.btn_cadastro_permissao.setText(QCoreApplication.translate("frm_principal", u"      Permiss\u00e3o", None))
        self.btn_configuracao_balanca.setToolTip(QCoreApplication.translate("frm_principal", u"Balan\u00e7a", None))
        self.btn_configuracao_balanca.setText(QCoreApplication.translate("frm_principal", u"      Balan\u00e7a", None))
        self.btn_configuracao_sistema.setToolTip(QCoreApplication.translate("frm_principal", u"Sistema", None))
        self.btn_configuracao_sistema.setText(QCoreApplication.translate("frm_principal", u"      Sistema", None))
        self.btn_movimento_pesar.setToolTip(QCoreApplication.translate("frm_principal", u"Pesar", None))
        self.btn_movimento_pesar.setText(QCoreApplication.translate("frm_principal", u"      Pesar", None))
        self.btn_movimento_caixa.setToolTip(QCoreApplication.translate("frm_principal", u"Caixa", None))
        self.btn_movimento_caixa.setText(QCoreApplication.translate("frm_principal", u"      Caixa", None))
        self.btn_inicio.setToolTip(QCoreApplication.translate("frm_principal", u"Cadastro", None))
        self.btn_inicio.setText(QCoreApplication.translate("frm_principal", u"    In\u00edcio", None))
