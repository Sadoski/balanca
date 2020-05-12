# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class FrmRegistroEmpresa(object):

    def set_frm_registro_empresa(self, frm_registro_empresa):
        if frm_registro_empresa.objectName():
            frm_registro_empresa.setObjectName(u"frm_registro_empresa")
        frm_registro_empresa.resize(590, 555)
        #frm_registro_empresa.setMinimumSize(QSize(590, 555))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        frm_registro_empresa.setFont(font)
        icon = QIcon()
        icon.addFile(u"./imagens/empresa.png", QSize(), QIcon.Normal, QIcon.Off)
        frm_registro_empresa.setWindowIcon(icon)
        frm_registro_empresa.setStyleSheet(u"QDialog{\n"
                                           "	background-color: white;\n"
                                           "}")

        self.grl_registro_empresa = QGridLayout(frm_registro_empresa)
        self.grl_registro_empresa.setSpacing(0)
        self.grl_registro_empresa.setObjectName(u"grl_registro_empresa")
        self.grl_registro_empresa.setContentsMargins(0, 0, 0, 0)

        self.fra_main_registro_empresa = QFrame(frm_registro_empresa)
        self.fra_main_registro_empresa.setObjectName(u"fra_main_registro_empresa")
        self.fra_main_registro_empresa.setMinimumSize(QSize(590, 555))
        #self.fra_main_registro_empresa.setMaximumSize(QSize(10000, 10000))
        #self.fra_main_registro_empresa.setFrameShape(QFrame.StyledPanel)
        #self.fra_main_registro_empresa.setFrameShadow(QFrame.Raised)

        self.vrl_main_registro_empresa = QVBoxLayout(self.fra_main_registro_empresa)
        self.vrl_main_registro_empresa.setObjectName(u"vrl_main_registro_empresa")

        self.grb_botoes = QGroupBox(self.fra_main_registro_empresa)
        self.grb_botoes.setObjectName(u"grb_botoes")
        self.grb_botoes.setMaximumSize(QSize(16777215, 51))
        font1 = QFont()
        font1.setPointSize(11)
        self.grb_botoes.setFont(font1)

        self.hzl_botoes = QHBoxLayout(self.grb_botoes)
        self.hzl_botoes.setObjectName(u"hzl_botoes")
        self.hzl_botoes.setContentsMargins(-1, 6, -1, -1)

        self.btn_primeiro = QPushButton(self.grb_botoes)
        self.btn_primeiro.setObjectName(u"btn_primeiro")
        self.btn_primeiro.setEnabled(False)
        self.btn_primeiro.setMinimumSize(QSize(36, 36))
        self.btn_primeiro.setMaximumSize(QSize(36, 36))
        self.btn_primeiro.setFocusPolicy(Qt.NoFocus)
        self.btn_primeiro.setStyleSheet(u"QPushButton#btn_primeiro{\n"
                                        "	border-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton#btn_primeiro:hover{\n"
                                        "	border: 1px solid rgba(33,33,33,.2);\n"
                                        "	background: rgba(33,33,33,.1);\n"
                                        "}\n"
                                        "QPushButton#btn_primeiro:pressed {\n"
                                        "	border: 1px solid rgba(33,33,33,.5);\n"
                                        "	background: rgba(33,33,33,.2);\n"
                                        "}")
        icon1 = QIcon()
        icon1.addFile(u"./imagens/nextAll.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_primeiro.setIcon(icon1)
        self.btn_primeiro.setIconSize(QSize(36, 36))
        self.btn_primeiro.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_primeiro)

        self.btn_anterior = QPushButton(self.grb_botoes)
        self.btn_anterior.setObjectName(u"btn_anterior")
        self.btn_anterior.setEnabled(False)
        self.btn_anterior.setMinimumSize(QSize(36, 36))
        self.btn_anterior.setMaximumSize(QSize(36, 36))
        self.btn_anterior.setFocusPolicy(Qt.NoFocus)
        self.btn_anterior.setStyleSheet(u"QPushButton#btn_anterior{\n"
                                        "	border-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton#btn_anterior:hover{\n"
                                        "	border: 1px solid rgba(33,33,33,.2);\n"
                                        "	background: rgba(33,33,33,.1);\n"
                                        "}\n"
                                        "QPushButton#btn_anterior:pressed {\n"
                                        "	border: 1px solid rgba(33,33,33,.5);\n"
                                        "	background: rgba(33,33,33,.2);\n"
                                        "}")
        icon2 = QIcon()
        icon2.addFile(u"./imagens/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_anterior.setIcon(icon2)
        self.btn_anterior.setIconSize(QSize(36, 36))
        self.btn_anterior.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_anterior)

        self.btn_proximo = QPushButton(self.grb_botoes)
        self.btn_proximo.setObjectName(u"btn_proximo")
        self.btn_proximo.setEnabled(False)
        self.btn_proximo.setMinimumSize(QSize(36, 36))
        self.btn_proximo.setMaximumSize(QSize(36, 36))
        self.btn_proximo.setFocusPolicy(Qt.NoFocus)
        self.btn_proximo.setStyleSheet(u"QPushButton#btn_proximo{\n"
                                       "	border-radius: 5px;\n"
                                       "}\n"
                                       "QPushButton#btn_proximo:hover{\n"
                                       "	border: 1px solid rgba(33,33,33,.2);\n"
                                       "	background: rgba(33,33,33,.1);\n"
                                       "}\n"
                                       "QPushButton#btn_proximo:pressed {\n"
                                       "	border: 1px solid rgba(33,33,33,.5);\n"
                                       "	background: rgba(33,33,33,.2);\n"
                                       "}")
        icon3 = QIcon()
        icon3.addFile(u"./imagens/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_proximo.setIcon(icon3)
        self.btn_proximo.setIconSize(QSize(36, 36))
        self.btn_proximo.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_proximo)

        self.btn_ultimo = QPushButton(self.grb_botoes)
        self.btn_ultimo.setObjectName(u"btn_ultimo")
        self.btn_ultimo.setEnabled(False)
        self.btn_ultimo.setMinimumSize(QSize(36, 36))
        self.btn_ultimo.setMaximumSize(QSize(36, 36))
        self.btn_ultimo.setFocusPolicy(Qt.NoFocus)
        self.btn_ultimo.setStyleSheet(u"QPushButton#btn_ultimo{\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton#btn_ultimo:hover{\n"
                                      "	border: 1px solid rgba(33,33,33,.2);\n"
                                      "	background: rgba(33,33,33,.1);\n"
                                      "}\n"
                                      "QPushButton#btn_ultimo:pressed {\n"
                                      "	border: 1px solid rgba(33,33,33,.5);\n"
                                      "	background: rgba(33,33,33,.2);\n"
                                      "}")
        icon4 = QIcon()
        icon4.addFile(u"./imagens/PreviousAll.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ultimo.setIcon(icon4)
        self.btn_ultimo.setIconSize(QSize(36, 36))
        self.btn_ultimo.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_ultimo)

        self.separacao_botoes_do_meio_do_navegadores = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_botoes.addItem(self.separacao_botoes_do_meio_do_navegadores)

        self.btn_pesquisar_registro = QPushButton(self.grb_botoes)
        self.btn_pesquisar_registro.setObjectName(u"btn_pesquisar_registro")
        self.btn_pesquisar_registro.setMinimumSize(QSize(36, 36))
        self.btn_pesquisar_registro.setMaximumSize(QSize(36, 36))
        self.btn_pesquisar_registro.setFocusPolicy(Qt.NoFocus)
        self.btn_pesquisar_registro.setStyleSheet(u"QPushButton#btn_pesquisar_registro{\n"
                                                  "	border-radius: 5px;\n"
                                                  "}\n"
                                                  "QPushButton#btn_pesquisar_registro:hover{\n"
                                                  "	border: 1px solid rgba(33,33,33,.2);\n"
                                                  "	background: rgba(33,33,33,.1);\n"
                                                  "}\n"
                                                  "QPushButton#btn_pesquisar_registro:pressed {\n"
                                                  "	border: 1px solid rgba(33,33,33,.5);\n"
                                                  "	background: rgba(33,33,33,.2);\n"
                                                  "}")
        icon5 = QIcon()
        icon5.addFile(u"./imagens/edit_find_replace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar_registro.setIcon(icon5)
        self.btn_pesquisar_registro.setIconSize(QSize(36, 30))
        self.btn_pesquisar_registro.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_pesquisar_registro)

        self.btn_pesquisar_codigo = QPushButton(self.grb_botoes)
        self.btn_pesquisar_codigo.setObjectName(u"btn_pesquisar_codigo")
        self.btn_pesquisar_codigo.setMinimumSize(QSize(36, 36))
        self.btn_pesquisar_codigo.setMaximumSize(QSize(36, 36))
        self.btn_pesquisar_codigo.setFocusPolicy(Qt.NoFocus)
        self.btn_pesquisar_codigo.setStyleSheet(u"QPushButton#btn_pesquisar_codigo{\n"
                                                "	border-radius: 5px;\n"
                                                "}\n"
                                                "QPushButton#btn_pesquisar_codigo:hover{\n"
                                                "	border: 1px solid rgba(33,33,33,.2);\n"
                                                "	background: rgba(33,33,33,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_pesquisar_codigo:pressed {\n"
                                                "	border: 1px solid rgba(33,33,33,.5);\n"
                                                "	background: rgba(33,33,33,.2);\n"
                                                "}")
        icon6 = QIcon()
        icon6.addFile(u"./imagens/dialog-ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar_codigo.setIcon(icon6)
        self.btn_pesquisar_codigo.setIconSize(QSize(30, 30))
        self.btn_pesquisar_codigo.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_pesquisar_codigo)

        self.btn_imprimir = QPushButton(self.grb_botoes)
        self.btn_imprimir.setObjectName(u"btn_imprimir")
        self.btn_imprimir.setMinimumSize(QSize(36, 36))
        self.btn_imprimir.setMaximumSize(QSize(36, 36))
        self.btn_imprimir.setFocusPolicy(Qt.NoFocus)
        self.btn_imprimir.setStyleSheet(u"QPushButton#btn_imprimir{\n"
                                        "	border-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton#btn_imprimir:hover{\n"
                                        "	border: 1px solid rgba(33,33,33,.2);\n"
                                        "	background: rgba(33,33,33,.1);\n"
                                        "}\n"
                                        "QPushButton#btn_imprimir:pressed {\n"
                                        "	border: 1px solid rgba(33,33,33,.5);\n"
                                        "	background: rgba(33,33,33,.2);\n"
                                        "}")
        icon7 = QIcon()
        icon7.addFile(u"./imagens/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_imprimir.setIcon(icon7)
        self.btn_imprimir.setIconSize(QSize(36, 36))
        self.btn_imprimir.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_imprimir)

        self.btn_copiar = QPushButton(self.grb_botoes)
        self.btn_copiar.setObjectName(u"btn_copiar")
        self.btn_copiar.setMinimumSize(QSize(36, 36))
        self.btn_copiar.setMaximumSize(QSize(36, 36))
        self.btn_copiar.setFocusPolicy(Qt.NoFocus)
        self.btn_copiar.setStyleSheet(u"QPushButton#btn_copiar{\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton#btn_copiar:hover{\n"
                                      "	border: 1px solid rgba(33,33,33,.2);\n"
                                      "	background: rgba(33,33,33,.1);\n"
                                      "}\n"
                                      "QPushButton#btn_copiar:pressed {\n"
                                      "	border: 1px solid rgba(33,33,33,.5);\n"
                                      "	background: rgba(33,33,33,.2);\n"
                                      "}")
        icon8 = QIcon()
        icon8.addFile(u"./imagens/copy-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_copiar.setIcon(icon8)
        self.btn_copiar.setIconSize(QSize(36, 36))
        self.btn_copiar.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_copiar)

        self.separacao_botes_meio_do_acoes_registro = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_botoes.addItem(self.separacao_botes_meio_do_acoes_registro)

        self.btn_novo = QPushButton(self.grb_botoes)
        self.btn_novo.setObjectName(u"btn_novo")
        self.btn_novo.setMinimumSize(QSize(36, 36))
        self.btn_novo.setMaximumSize(QSize(36, 36))
        self.btn_novo.setFont(font)
        self.btn_novo.setFocusPolicy(Qt.NoFocus)
        self.btn_novo.setStyleSheet(u"QPushButton#btn_novo{\n"
                                    "	background-color: #0080ff ;\n"
                                    "	color: #fff;\n"
                                    "	border-radius: 5px;\n"
                                    "}\n"
                                    "QPushButton#btn_novo:hover{\n"
                                    "	background-color:  #0073e6;\n"
                                    "}\n"
                                    "QPushButton#btn_novo:pressed {\n"
                                    "	background-color: #0059b3;\n"
                                    "}\n"
                                    "QPushButton#btn_novo:disabled {\n"
                                    "	background-color:  #a6a6a6;\n"
                                    "	color: #6a6767;\n"
                                    "}")
        icon9 = QIcon()
        icon9.addFile(u"./imagens/addNew.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_novo.setIcon(icon9)
        self.btn_novo.setIconSize(QSize(36, 36))

        self.hzl_botoes.addWidget(self.btn_novo)

        self.btn_editar = QPushButton(self.grb_botoes)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setEnabled(False)
        self.btn_editar.setMinimumSize(QSize(36, 36))
        self.btn_editar.setMaximumSize(QSize(36, 36))
        self.btn_editar.setFont(font)
        self.btn_editar.setFocusPolicy(Qt.NoFocus)
        self.btn_editar.setStyleSheet(u"QPushButton#btn_editar{\n"
                                      "	background-color: #0080ff ;\n"
                                      "	color: #fff;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton#btn_editar:hover{\n"
                                      "	background-color:  #0073e6;\n"
                                      "}\n"
                                      "QPushButton#btn_editar:pressed {\n"
                                      "	background-color: #0059b3;\n"
                                      "}\n"
                                      "QPushButton#btn_editar:disabled {\n"
                                      "	background-color:  #a6a6a6;\n"
                                      "	color: #6a6767;\n"
                                      "}")
        icon10 = QIcon()
        icon10.addFile(u"./imagens/editFile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editar.setIcon(icon10)
        self.btn_editar.setIconSize(QSize(36, 36))

        self.hzl_botoes.addWidget(self.btn_editar)

        self.btn_salvar = QPushButton(self.grb_botoes)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setEnabled(False)
        self.btn_salvar.setMinimumSize(QSize(36, 36))
        self.btn_salvar.setMaximumSize(QSize(36, 36))
        self.btn_salvar.setFont(font1)
        self.btn_salvar.setFocusPolicy(Qt.NoFocus)
        self.btn_salvar.setStyleSheet(u"QPushButton#btn_salvar{\n"
                                      "	background-color: #0080ff ;\n"
                                      "	color: #fff;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton#btn_salvar:hover{\n"
                                      "	background-color:  #0073e6;\n"
                                      "}\n"
                                      "QPushButton#btn_salvar:pressed {\n"
                                      "	background-color: #0059b3;\n"
                                      "}\n"
                                      "QPushButton#btn_salvar:disabled {\n"
                                      "	background-color:  #a6a6a6;\n"
                                      "	color: #6a6767;\n"
                                      "	border: 1px solid gray;\n"
                                      "}")
        icon11 = QIcon()
        icon11.addFile(u"./imagens/save-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar.setIcon(icon11)
        self.btn_salvar.setIconSize(QSize(36, 36))

        self.hzl_botoes.addWidget(self.btn_salvar)

        self.btn_cancelar = QPushButton(self.grb_botoes)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setEnabled(False)
        self.btn_cancelar.setMinimumSize(QSize(36, 36))
        self.btn_cancelar.setMaximumSize(QSize(36, 36))
        self.btn_cancelar.setFont(font1)
        self.btn_cancelar.setFocusPolicy(Qt.NoFocus)
        self.btn_cancelar.setStyleSheet(u"QPushButton#btn_cancelar{\n"
                                        "	background-color: #0080ff ;\n"
                                        "	color: #fff;\n"
                                        "	border-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton#btn_cancelar:hover{\n"
                                        "	background-color:  #0073e6;\n"
                                        "}\n"
                                        "QPushButton#btn_cancelar:pressed {\n"
                                        "	background-color: #0059b3;\n"
                                        "}\n"
                                        "QPushButton#btn_cancelar:disabled {\n"
                                        "	background-color:  #a6a6a6;\n"
                                        "	color: #6a6767;\n"
                                        "	border: 1px solid gray;\n"
                                        "}")
        icon12 = QIcon()
        icon12.addFile(u"./imagens/cancelfile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar.setIcon(icon12)
        self.btn_cancelar.setIconSize(QSize(36, 36))

        self.hzl_botoes.addWidget(self.btn_cancelar)

        self.btn_deletar = QPushButton(self.grb_botoes)
        self.btn_deletar.setObjectName(u"btn_deletar")
        self.btn_deletar.setEnabled(False)
        self.btn_deletar.setMinimumSize(QSize(36, 36))
        self.btn_deletar.setMaximumSize(QSize(36, 36))
        self.btn_deletar.setFont(font1)
        self.btn_deletar.setFocusPolicy(Qt.NoFocus)
        self.btn_deletar.setStyleSheet(u"QPushButton#btn_deletar{\n"
                                       "	background-color: #0080ff ;\n"
                                       "	color: #fff;\n"
                                       "	border-radius: 5px;\n"
                                       "}\n"
                                       "QPushButton#btn_deletar:hover{\n"
                                       "	background-color:  #0073e6;\n"
                                       "}\n"
                                       "QPushButton#btn_deletar:pressed {\n"
                                       "	background-color: #0059b3;\n"
                                       "}\n"
                                       "QPushButton#btn_deletar:disabled {\n"
                                       "	background-color:  #a6a6a6;\n"
                                       "	color: #6a6767;\n"
                                       "	border: 1px solid gray;\n"
                                       "}")
        icon13 = QIcon()
        icon13.addFile(u"./imagens/delet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_deletar.setIcon(icon13)
        self.btn_deletar.setIconSize(QSize(36, 36))

        self.hzl_botoes.addWidget(self.btn_deletar)

        self.vrl_main_registro_empresa.addWidget(self.grb_botoes)

        self.grb_compos_dados = QGroupBox(self.fra_main_registro_empresa)
        self.grb_compos_dados.setObjectName(u"grb_compos_dados")
        self.grb_compos_dados.setFont(font1)
        self.grb_compos_dados.setStyleSheet(u"color: #474747;\n")

        self.grl_campo_dados = QGridLayout(self.grb_compos_dados)
        self.grl_campo_dados.setObjectName(u"grl_campo_dados")

        self.lbl_codigo = QLabel(self.grb_compos_dados)
        self.lbl_codigo.setObjectName(u"lbl_codigo")
        font2 = QFont()
        font2.setPointSize(10)
        self.lbl_codigo.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_codigo, 0, 0, 1, 1)

        self.lbl_tipo_pessoa = QLabel(self.grb_compos_dados)
        self.lbl_tipo_pessoa.setObjectName(u"lbl_tipo_pessoa")
        self.lbl_tipo_pessoa.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_tipo_pessoa, 0, 1, 1, 1)

        self.lbl_tipo_empresa = QLabel(self.grb_compos_dados)
        self.lbl_tipo_empresa.setObjectName(u"lbl_tipo_empresa")
        self.lbl_tipo_empresa.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_tipo_empresa, 0, 2, 1, 1)

        self.txt_codigo = QLineEdit(self.grb_compos_dados)
        self.txt_codigo.setObjectName(u"txt_codigo")
        self.txt_codigo.setMinimumSize(QSize(141, 0))
        self.txt_codigo.setMaximumSize(QSize(200, 16777215))
        self.txt_codigo.setFont(font2)
        self.txt_codigo.setStyleSheet(u"QLineEdit#txt_codigo{\n"
                                      "	background-color: #fff;\n"
                                      "	border: 1px solid gray;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QLineEdit#txt_codigo:focus{\n"
                                      "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                      "}\n"
                                      "QLineEdit#txt_codigo:disabled {\n"
                                      "	background-color:  #dcdcdc;\n"
                                      "	color: #6a6767;\n"
                                      "	border: 1px solid gray;\n"
                                      "}")
        self.txt_codigo.setReadOnly(False)

        self.grl_campo_dados.addWidget(self.txt_codigo, 1, 0, 1, 1)

        self.cb_tipo_pessoa = QComboBox(self.grb_compos_dados)
        self.cb_tipo_pessoa.setObjectName(u"cb_tipo_pessoa")
        self.cb_tipo_pessoa.setMinimumSize(QSize(135, 0))
        self.cb_tipo_pessoa.setMaximumSize(QSize(200, 16777215))
        self.cb_tipo_pessoa.setFont(font2)
        self.cb_tipo_pessoa.setStyleSheet(u"QComboBox#cb_tipo_pessoa {\n"
                                          "	background-color: #eeeeee;\n"
                                          "	color: #6a6767;\n"
                                          "	border: 1px solid gray;\n"
                                          "	border-radius: 5px;\n"
                                          "}\n"
                                          "QComboBox#cb_tipo_pessoa:focus{\n"
                                          "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                          "}\n"
                                          "QComboBox#cb_tipo_pessoae:disabled {\n"
                                          "	background-color:  #dcdcdc;\n"
                                          "	color: #6a6767;\n"
                                          "	border: 1px solid gray;\n"
                                          "}\n"
                                          "QHeaderView::section QComboBox {\n"
                                          "    background-color: #585A5C;\n"
                                          "    color: #F0F0F0;\n"
                                          "}\n"
                                          "QComboBox::drop-down {\n"
                                          "    border: 0;\n"
                                          "	subcontrol-position: right center;\n"
                                          "    subcontrol-origin: margin;\n"
                                          "}\n"
                                          "QComboBox::down-arrow {\n"
                                          "	subcontrol-position: right center;\n"
                                          "    subcontrol-origin: margin;\n"
                                          "	margin-right: 3px;\n"
                                          "    background-image: url(C:/Users/Cauneto/Documents/RPA/image/dropdown.png);\n"
                                          "	background-position: center;\n"
                                          "	background-repeat: no-repeat;\n"
                                          "}")

        self.grl_campo_dados.addWidget(self.cb_tipo_pessoa, 1, 1, 1, 1)

        self.cb_tipo_empresa = QComboBox(self.grb_compos_dados)
        self.cb_tipo_empresa.setObjectName(u"cb_tipo_empresa")
        self.cb_tipo_empresa.setMinimumSize(QSize(131, 20))
        self.cb_tipo_empresa.setMaximumSize(QSize(200, 16777215))
        self.cb_tipo_empresa.setFont(font2)
        self.cb_tipo_empresa.setStyleSheet(u"QComboBox#cb_tipo_empresa {\n"
                                           "	background-color: #eeeeee;\n"
                                           "	color: #6a6767;\n"
                                           "	border: 1px solid gray;\n"
                                           "	border-radius: 5px;\n"
                                           "}\n"
                                           "QComboBox#cb_tipo_empresa:focus{\n"
                                           "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                           "}\n"
                                           "QComboBox#cb_tipo_empresa:disabled {\n"
                                           "	background-color:  #dcdcdc;\n"
                                           "	color: #6a6767;\n"
                                           "	border: 1px solid gray;\n"
                                           "}\n"
                                           "QHeaderView::section QComboBox {\n"
                                           "    background-color: #585A5C;\n"
                                           "    color: #F0F0F0;\n"
                                           "}\n"
                                           "QComboBox::drop-down {\n"
                                           "    border: 0;\n"
                                           "	subcontrol-position: right center;\n"
                                           "    subcontrol-origin: margin;\n"
                                           "}\n"
                                           "QComboBox::down-arrow {\n"
                                           "	subcontrol-position: right center;\n"
                                           "    subcontrol-origin: margin;\n"
                                           "	margin-right: 3px;\n"
                                           "    background-image: url(C:/Users/Cauneto/Documents/RPA/image/dropdown.png);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-repeat;\n"
                                           "}")

        self.grl_campo_dados.addWidget(self.cb_tipo_empresa, 1, 2, 1, 1)

        self.fra_logo = QFrame(self.grb_compos_dados)
        self.fra_logo.setObjectName(u"fra_logo")
        self.fra_logo.setMinimumSize(QSize(101, 131))
        self.fra_logo.setMaximumSize(QSize(101, 131))
        self.fra_logo.setStyleSheet(u"QFrame#fra_logo{\n"
                                      "	background: white;\n"
                                      "	border: 1px solid gray;\n"
                                      "}")
        self.fra_logo.setFrameShape(QFrame.StyledPanel)
        self.fra_logo.setFrameShadow(QFrame.Raised)

        self.btn_buscar_arquivo_imagem_logo = QPushButton(self.fra_logo)
        self.btn_buscar_arquivo_imagem_logo.setObjectName(u"btn_buscar_arquivo_imagem_logo")
        self.btn_buscar_arquivo_imagem_logo.setGeometry(QRect(10, 99, 31, 25))
        self.btn_buscar_arquivo_imagem_logo.setMinimumSize(QSize(31, 25))
        self.btn_buscar_arquivo_imagem_logo.setMaximumSize(QSize(31, 25))
        self.btn_buscar_arquivo_imagem_logo.setFocusPolicy(Qt.NoFocus)
        self.btn_buscar_arquivo_imagem_logo.setStyleSheet(u"QPushButton#btn_buscar_arquivo_imagem_logo{\n"
                                                          "	background-color: #0080ff ;\n"
                                                          "	color: #fff;\n"
                                                          "	border-radius: 5px;\n"
                                                          "}\n"
                                                          "QPushButton#btn_buscar_arquivo_imagem_logo:hover{\n"
                                                          "	background-color:  #0073e6;\n"
                                                          "}\n"
                                                          "QPushButton#btn_buscar_arquivo_imagem_logo:pressed {\n"
                                                          "	background-color: #0059b3;\n"
                                                          "}\n"
                                                          "QPushButton#btn_buscar_arquivo_imagem_logo:disabled {\n"
                                                          "	background-color:  #a6a6a6;\n"
                                                          "	color: #6a6767;\n"
                                                          "}")
        icon14 = QIcon()
        icon14.addFile(u"./imagens/pasta_imagem.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar_arquivo_imagem_logo.setIcon(icon14)

        self.lbl_logo = QLabel(self.fra_logo)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(10, 16, 80, 80))
        self.lbl_logo.setMinimumSize(QSize(80, 80))
        self.lbl_logo.setFont(font2)
        self.lbl_logo.setStyleSheet(u"QLabel#lbl_logo{\n"
                                    "	background: #eeeeee;\n"
                                    "	border: 1px solid gray;\n"
                                    "}")
        self.lbl_logo.setScaledContents(True)
        self.lbl_logo.setAlignment(Qt.AlignCenter)
        self.lbl_logo.setMargin(5)

        self.btn_deletar_imagem_logo = QPushButton(self.fra_logo)
        self.btn_deletar_imagem_logo.setObjectName(u"btn_deletar_imagem_logo")
        self.btn_deletar_imagem_logo.setGeometry(QRect(60, 99, 31, 25))
        self.btn_deletar_imagem_logo.setMinimumSize(QSize(31, 25))
        self.btn_deletar_imagem_logo.setMaximumSize(QSize(31, 25))
        self.btn_deletar_imagem_logo.setFocusPolicy(Qt.NoFocus)
        self.btn_deletar_imagem_logo.setStyleSheet(u"QPushButton#btn_deletar_imagem_logo{\n"
                                                   "	background-color: #0080ff ;\n"
                                                   "	color: #fff;\n"
                                                   "	border-radius: 5px;\n"
                                                   "}\n"
                                                   "QPushButton#btn_deletar_imagem_logo:hover{\n"
                                                   "	background-color:  #0073e6;\n"
                                                   "}\n"
                                                   "QPushButton#btn_deletar_imagem_logo:pressed {\n"
                                                   "	background-color: #0059b3;\n"
                                                   "}\n"
                                                   "QPushButton#btn_deletar_imagem_logo:disabled {\n"
                                                   "	background-color:  #a6a6a6;\n"
                                                   "	color: #6a6767;\n"
                                                   "}")
        self.btn_deletar_imagem_logo.setIcon(icon12)
        self.lbl_logotipo = QLabel(self.fra_logo)
        self.lbl_logotipo.setObjectName(u"lbl_logotipo")
        self.lbl_logotipo.setGeometry(QRect(30, 0, 47, 13))
        self.lbl_logotipo.setMinimumSize(QSize(47, 13))
        self.lbl_logotipo.setMaximumSize(QSize(47, 13))

        self.grl_campo_dados.addWidget(self.fra_logo, 1, 4, 7, 1)

        self.lbl_nome_razao_social = QLabel(self.grb_compos_dados)
        self.lbl_nome_razao_social.setObjectName(u"lbl_nome_razao_social")
        self.lbl_nome_razao_social.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_nome_razao_social, 2, 0, 1, 1)

        self.txt_nome_razao_social = QLineEdit(self.grb_compos_dados)
        self.txt_nome_razao_social.setObjectName(u"txt_nome_razao_social")
        self.txt_nome_razao_social.setMinimumSize(QSize(431, 20))
        self.txt_nome_razao_social.setFont(font2)
        self.txt_nome_razao_social.setStyleSheet(u"QLineEdit#txt_nome_razao_social{\n"
                                                 "	background-color: #fff;\n"
                                                 "	border: 1px solid gray;\n"
                                                 "	border-radius: 5px;\n"
                                                 "}\n"
                                                 "QLineEdit#txt_nome_razao_social:focus{\n"
                                                 "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                                 "}\n"
                                                 "QLineEdit#txt_nome_razao_social:disabled {\n"
                                                 "	background-color:  #dcdcdc;\n"
                                                 "	color: #6a6767;\n"
                                                 "	border: 1px solid gray;\n"
                                                 "}")
        self.txt_nome_razao_social.setMaxLength(75)

        self.grl_campo_dados.addWidget(self.txt_nome_razao_social, 3, 0, 1, 3)

        self.separacao_logo_campos = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.grl_campo_dados.addItem(self.separacao_logo_campos, 3, 3, 1, 1)

        self.lbl_sobrenome_fantasia = QLabel(self.grb_compos_dados)
        self.lbl_sobrenome_fantasia.setObjectName(u"lbl_sobrenome_fantasia")
        self.lbl_sobrenome_fantasia.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_sobrenome_fantasia, 4, 0, 1, 1)

        self.txt_nome_fantasia = QLineEdit(self.grb_compos_dados)
        self.txt_nome_fantasia.setObjectName(u"txt_nome_fantasia")
        self.txt_nome_fantasia.setMinimumSize(QSize(431, 20))
        self.txt_nome_fantasia.setFont(font2)
        self.txt_nome_fantasia.setStyleSheet(u"QLineEdit#txt_nome_fantasia{\n"
                                             "	background-color: #fff;\n"
                                             "	border: 1px solid gray;\n"
                                             "	border-radius: 5px;\n"
                                             "}\n"
                                             "QLineEdit#txt_nome_fantasia:focus{\n"
                                             "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                             "}\n"
                                             "QLineEdit#txt_nome_fantasia:disabled {\n"
                                             "	background-color:  #dcdcdc;\n"
                                             "	color: #6a6767;\n"
                                             "	border: 1px solid gray;\n"
                                             "}")
        self.txt_nome_fantasia.setMaxLength(75)

        self.grl_campo_dados.addWidget(self.txt_nome_fantasia, 5, 0, 1, 3)

        self.lbl_cnpj = QLabel(self.grb_compos_dados)
        self.lbl_cnpj.setObjectName(u"lbl_cnpj")
        self.lbl_cnpj.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_cnpj, 6, 0, 1, 1)

        self.lbl_inscricao_estadual = QLabel(self.grb_compos_dados)
        self.lbl_inscricao_estadual.setObjectName(u"lbl_inscricao_estadual")
        self.lbl_inscricao_estadual.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_inscricao_estadual, 6, 1, 1, 1)

        self.lbl_inscricao_municipal = QLabel(self.grb_compos_dados)
        self.lbl_inscricao_municipal.setObjectName(u"lbl_inscricao_municipal")
        self.lbl_inscricao_municipal.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_inscricao_municipal, 6, 2, 1, 1)

        self.txt_cpf_cnpj = QLineEdit(self.grb_compos_dados)
        self.txt_cpf_cnpj.setObjectName(u"txt_cpf_cnpj")
        self.txt_cpf_cnpj.setMinimumSize(QSize(141, 0))
        self.txt_cpf_cnpj.setMaximumSize(QSize(200, 16777215))
        self.txt_cpf_cnpj.setFont(font2)
        self.txt_cpf_cnpj.setStyleSheet(u"QLineEdit#txt_cpf_cnpj{\n"
                                        "	background-color: #fff;\n"
                                        "	border: 1px solid gray;\n"
                                        "	border-radius: 5px;\n"
                                        "}\n"
                                        "QLineEdit#txt_cpf_cnpj:focus{\n"
                                        "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                        "}\n"
                                        "QLineEdit#txt_cpf_cnpj:disabled {\n"
                                        "	background-color:  #dcdcdc;\n"
                                        "	color: #6a6767;\n"
                                        "	border: 1px solid gray;\n"
                                        "}")
        self.txt_cpf_cnpj.setMaxLength(18)

        self.grl_campo_dados.addWidget(self.txt_cpf_cnpj, 7, 0, 1, 1)

        self.txt_inscricao_estadual = QLineEdit(self.grb_compos_dados)
        self.txt_inscricao_estadual.setObjectName(u"txt_inscricao_estadual")
        self.txt_inscricao_estadual.setMinimumSize(QSize(135, 0))
        self.txt_inscricao_estadual.setMaximumSize(QSize(200, 16777215))
        self.txt_inscricao_estadual.setFont(font2)
        self.txt_inscricao_estadual.setStyleSheet(u"QLineEdit#txt_inscricao_estadual{\n"
                                                  "	background-color: #fff;\n"
                                                  "	border: 1px solid gray;\n"
                                                  "	border-radius: 5px;\n"
                                                  "}\n"
                                                  "QLineEdit#txt_inscricao_estadual:focus{\n"
                                                  "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                                  "}\n"
                                                  "QLineEdit#txt_inscricao_estadual:disabled {\n"
                                                  "	background-color:  #dcdcdc;\n"
                                                  "	color: #6a6767;\n"
                                                  "	border: 1px solid gray;\n"
                                                  "}")
        self.txt_inscricao_estadual.setMaxLength(15)

        self.grl_campo_dados.addWidget(self.txt_inscricao_estadual, 7, 1, 1, 1)

        self.txt_inscricao_municipal = QLineEdit(self.grb_compos_dados)
        self.txt_inscricao_municipal.setObjectName(u"txt_inscricao_municipal")
        self.txt_inscricao_municipal.setMinimumSize(QSize(131, 20))
        self.txt_inscricao_municipal.setMaximumSize(QSize(200, 16777215))
        self.txt_inscricao_municipal.setFont(font2)
        self.txt_inscricao_municipal.setStyleSheet(u"QLineEdit#txt_inscricao_municipal{\n"
                                                   "	background-color: #fff;\n"
                                                   "	border: 1px solid gray;\n"
                                                   "	border-radius: 5px;\n"
                                                   "}\n"
                                                   "QLineEdit#txt_inscricao_municipal:focus{\n"
                                                   "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                                   "}\n"
                                                   "QLineEdit#txt_inscricao_municipal:disabled {\n"
                                                   "	background-color:  #dcdcdc;\n"
                                                   "	color: #6a6767;\n"
                                                   "	border: 1px solid gray;\n"
                                                   "}")
        self.txt_inscricao_municipal.setMaxLength(15)

        self.grl_campo_dados.addWidget(self.txt_inscricao_municipal, 7, 2, 1, 1)

        self.lbl_telefone = QLabel(self.grb_compos_dados)
        self.lbl_telefone.setObjectName(u"lbl_telefone")
        self.lbl_telefone.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_telefone, 8, 0, 1, 1)

        self.lbl_celular = QLabel(self.grb_compos_dados)
        self.lbl_celular.setObjectName(u"lbl_celular")
        self.lbl_celular.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_celular, 8, 1, 1, 1)

        self.txt_telefone = QLineEdit(self.grb_compos_dados)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setMinimumSize(QSize(141, 0))
        self.txt_telefone.setMaximumSize(QSize(200, 16777215))
        self.txt_telefone.setFont(font2)
        self.txt_telefone.setStyleSheet(u"QLineEdit#txt_telefone{\n"
                                        "	background-color: #fff;\n"
                                        "	border: 1px solid gray;\n"
                                        "	border-radius: 5px;\n"
                                        "}\n"
                                        "QLineEdit#txt_telefone:focus{\n"
                                        "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                        "}\n"
                                        "QLineEdit#txt_telefone:disabled {\n"
                                        "	background-color:  #dcdcdc;\n"
                                        "	color: #6a6767;\n"
                                        "	border: 1px solid gray;\n"
                                        "}")
        self.txt_telefone.setMaxLength(16)

        self.grl_campo_dados.addWidget(self.txt_telefone, 9, 0, 1, 1)

        self.txt_celular = QLineEdit(self.grb_compos_dados)
        self.txt_celular.setObjectName(u"txt_celular")
        self.txt_celular.setMinimumSize(QSize(141, 0))
        self.txt_celular.setMaximumSize(QSize(200, 16777215))
        self.txt_celular.setFont(font2)
        self.txt_celular.setStyleSheet(u"QLineEdit#txt_celular{\n"
                                       "	background-color: #fff;\n"
                                       "	border: 1px solid gray;\n"
                                       "	border-radius: 5px;\n"
                                       "}\n"
                                       "QLineEdit#txt_celular:focus{\n"
                                       "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                       "}\n"
                                       "QLineEdit#txt_celular:disabled {\n"
                                       "	background-color:  #dcdcdc;\n"
                                       "	color: #6a6767;\n"
                                       "	border: 1px solid gray;\n"
                                       "}")
        self.txt_celular.setMaxLength(16)

        self.grl_campo_dados.addWidget(self.txt_celular, 9, 1, 1, 1)

        self.lbl_email = QLabel(self.grb_compos_dados)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setFont(font2)

        self.grl_campo_dados.addWidget(self.lbl_email, 10, 0, 1, 1)

        self.txt_email = QLineEdit(self.grb_compos_dados)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setMinimumSize(QSize(431, 20))
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet(u"QLineEdit#txt_email{\n"
                                     "	background-color: #fff;\n"
                                     "	border: 1px solid gray;\n"
                                     "	border-radius: 5px;\n"
                                      "}\n"
                                     "QLineEdit#txt_email:focus{\n"
                                     "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                     "}\n"
                                     "QLineEdit#txt_email:disabled {\n"
                                     "	background-color:  #dcdcdc;\n"
                                     "	color: #6a6767;\n"
                                     "	border: 1px solid gray;\n"
                                     "}")
        self.txt_email.setMaxLength(255)

        self.grl_campo_dados.addWidget(self.txt_email, 11, 0, 1, 3)

        self.tab_informcoes = QTabWidget(self.grb_compos_dados)
        self.tab_informcoes.setObjectName(u"tab_informcoes")
        self.tab_informcoes.setMinimumSize(QSize(552, 172))
        self.tab_informcoes.setFont(font2)
        self.tab_informcoes.setFocusPolicy(Qt.NoFocus)
        self.tab_informcoes.setStyleSheet(u"QTabWidget{\n"
                                          "	background-color: #f6f6f6;\n"
                                          "}\n"
                                          "QTabBar{\n"
                                          "	background-color:  #eeeeee;\n"
                                          "	border: none;\n"
                                          "	border-top-left-radius: 10px;\n"
                                          "	border-top-right-radius: 10px;\n"
                                          "}\n"
                                          "QTabBar::tab {\n"
                                          "    padding: 8 64 5 20;\n"
                                          "    color:  gray;\n"
                                          "	border-top-left-radius: 10px;\n"
                                          "	border-top-right-radius: 10px;\n"
                                          "	border-left: 1px solid lightgray;\n"
                                          "	border-right: 1px solid lightgray;\n"
                                          "}\n"
                                          "QTabBar::tab:hover {\n"
                                          "     background: #dcdcdc;\n"
                                          "}\n"
                                          "QTabBar::tab:selected {\n"
                                          "    background:  gray;\n"
                                          "    color: white;\n"
                                          "}")

        self.tab_endereco = QWidget()
        self.tab_endereco.setObjectName(u"tab_endereco")

        self.grl_tab_endereco = QGridLayout(self.tab_endereco)
        self.grl_tab_endereco.setObjectName(u"grl_tab_endereco")

        self.lbl_endereco = QLabel(self.tab_endereco)
        self.lbl_endereco.setObjectName(u"lbl_endereco")
        self.lbl_endereco.setFont(font2)

        self.grl_tab_endereco.addWidget(self.lbl_endereco, 2, 0, 1, 1)

        self.lbl_complemento = QLabel(self.tab_endereco)
        self.lbl_complemento.setObjectName(u"lbl_complemento")
        self.lbl_complemento.setFont(font2)

        self.grl_tab_endereco.addWidget(self.lbl_complemento, 2, 2, 1, 1)

        self.txt_cidade = QLineEdit(self.tab_endereco)
        self.txt_cidade.setObjectName(u"txt_cidade")
        self.txt_cidade.setMinimumSize(QSize(330, 20))
        self.txt_cidade.setFont(font2)
        self.txt_cidade.setStyleSheet(u"QLineEdit#txt_cidade{\n"
                                      "	background-color: #fff;\n"
                                      "	border: 1px solid gray;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QLineEdit#txt_cidade:focus{\n"
                                      "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                      "}\n"
                                      "QLineEdit#txt_cidade:disabled {\n"
                                      "	background-color:  #dcdcdc;\n"
                                      "	color: #6a6767;\n"
                                      "	border: 1px solid gray;\n"
                                      "}")
        self.txt_cidade.setMaxLength(100)
        self.txt_cidade.setReadOnly(True)

        self.grl_tab_endereco.addWidget(self.txt_cidade, 1, 1, 1, 2)

        self.txt_endereco = QLineEdit(self.tab_endereco)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setMinimumSize(QSize(251, 20))
        self.txt_endereco.setFont(font2)
        self.txt_endereco.setStyleSheet(u"QLineEdit#txt_endereco{\n"
                                        "	background-color: #fff;\n"
                                        "	border: 1px solid gray;\n"
                                        "	border-radius: 5px;\n"
                                        "}\n"
                                        "QLineEdit#txt_endereco:focus{\n"
                                        "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                        "}\n"
                                        "QLineEdit#ttxt_endereco:disabled {\n"
                                        "	background-color:  #dcdcdc;\n"
                                        "	color: #6a6767;\n"
                                        "	border: 1px solid gray;\n"
                                        "}")
        self.txt_endereco.setMaxLength(100)

        self.grl_tab_endereco.addWidget(self.txt_endereco, 3, 0, 1, 2)

        self.lbl_estado = QLabel(self.tab_endereco)
        self.lbl_estado.setObjectName(u"lbl_estado")
        self.lbl_estado.setFont(font2)

        self.grl_tab_endereco.addWidget(self.lbl_estado, 0, 3, 1, 1)

        self.txt_complemento = QLineEdit(self.tab_endereco)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setMinimumSize(QSize(251, 20))
        self.txt_complemento.setFont(font2)
        self.txt_complemento.setStyleSheet(u"QLineEdit#txt_complemento{\n"
                                           "	background-color: #fff;\n"
                                           "	border: 1px solid gray;\n"
                                           "	border-radius: 5px;\n"
                                           "}\n"
                                           "QLineEdit#txt_complemento:focus{\n"
                                           "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                           "}\n"
                                           "QLineEdit#txt_complemento:disabled {\n"
                                           "	background-color:  #dcdcdc;\n"
                                           "	color: #6a6767;\n"
                                           "	border: 1px solid gray;\n"
                                           "}")
        self.txt_complemento.setMaxLength(80)

        self.grl_tab_endereco.addWidget(self.txt_complemento, 3, 2, 1, 2)

        self.txt_bairro = QLineEdit(self.tab_endereco)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setMinimumSize(QSize(251, 20))
        self.txt_bairro.setFont(font2)
        self.txt_bairro.setStyleSheet(u"QLineEdit#txt_bairro{\n"
                                      "	background-color: #fff;\n"
                                      "	border: 1px solid gray;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QLineEdit#txt_bairro:focus{\n"
                                      "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                      "}\n"
                                      "QLineEdit#txt_bairro:disabled {\n"
                                      "	background-color:  #dcdcdc;\n"
                                      "	color: #6a6767;\n"
                                      "	border: 1px solid gray;\n"
                                      "}")
        self.txt_bairro.setMaxLength(70)

        self.grl_tab_endereco.addWidget(self.txt_bairro, 5, 0, 1, 2)

        self.lbl_cidade = QLabel(self.tab_endereco)
        self.lbl_cidade.setObjectName(u"lbl_cidade")
        self.lbl_cidade.setFont(font2)

        self.grl_tab_endereco.addWidget(self.lbl_cidade, 0, 1, 1, 2)

        self.lbl_cep = QLabel(self.tab_endereco)
        self.lbl_cep.setObjectName(u"lbl_cep")
        self.lbl_cep.setFont(font2)

        self.grl_tab_endereco.addWidget(self.lbl_cep, 0, 0, 1, 1)

        self.txt_estado = QLineEdit(self.tab_endereco)
        self.txt_estado.setObjectName(u"txt_estado")
        self.txt_estado.setMinimumSize(QSize(51, 20))
        self.txt_estado.setMaximumSize(QSize(150, 16777215))
        self.txt_estado.setFont(font2)
        self.txt_estado.setStyleSheet(u"QLineEdit#txt_estado{\n"
                                      "	background-color: #fff;\n"
                                      "	border: 1px solid gray;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QLineEdit#txt_estado:focus{\n"
                                      "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                      "}\n"
                                      "QLineEdit#txt_estado:disabled {\n"
                                      "	background-color:  #dcdcdc;\n"
                                      "	color: #6a6767;\n"
                                      "	border: 1px solid gray;\n"
                                      "}")
        self.txt_estado.setMaxLength(50)
        self.txt_estado.setReadOnly(True)

        self.grl_tab_endereco.addWidget(self.txt_estado, 1, 3, 1, 1)

        self.txt_cep = QLineEdit(self.tab_endereco)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setMinimumSize(QSize(100, 20))
        self.txt_cep.setMaximumSize(QSize(181, 16777215))
        self.txt_cep.setFont(font2)
        self.txt_cep.setStyleSheet(u"QLineEdit#txt_cep{\n"
                                   "	background-color: #fff;\n"
                                   "	border: 1px solid gray;\n"
                                   "	border-radius: 5px;\n"
                                   "}\n"
                                   "QLineEdit#txt_cep:focus{\n"
                                   "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                   "}\n"
                                   "QLineEdit#txt_cep:disabled {\n"
                                   "	background-color:  #dcdcdc;\n"
                                   "	color: #6a6767;\n"
                                   "	border: 1px solid gray;\n"
                                   "}")
        self.txt_cep.setMaxLength(9)

        self.grl_tab_endereco.addWidget(self.txt_cep, 1, 0, 1, 1)

        self.lbl_bairro = QLabel(self.tab_endereco)
        self.lbl_bairro.setObjectName(u"lbl_bairro")
        self.lbl_bairro.setFont(font2)

        self.grl_tab_endereco.addWidget(self.lbl_bairro, 4, 0, 1, 1)

        self.separacao_campos_endereco_borda = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grl_tab_endereco.addItem(self.separacao_campos_endereco_borda, 6, 0, 1, 1)

        self.tab_informcoes.addTab(self.tab_endereco, "")

        self.tab_matriz = QWidget()
        self.tab_matriz.setObjectName(u"tab_matriz")

        self.grl_tab_matriz = QGridLayout(self.tab_matriz)
        self.grl_tab_matriz.setObjectName(u"grl_tab_matriz")

        self.lbl_codigo_matriz = QLabel(self.tab_matriz)
        self.lbl_codigo_matriz.setObjectName(u"lbl_codigo_matriz")
        self.lbl_codigo_matriz.setFont(font2)

        self.grl_tab_matriz.addWidget(self.lbl_codigo_matriz, 0, 0, 1, 1)

        self.lbl_nome_razao_social_matriz = QLabel(self.tab_matriz)
        self.lbl_nome_razao_social_matriz.setObjectName(u"lbl_nome_razao_social_matriz")
        self.lbl_nome_razao_social_matriz.setFont(font2)

        self.grl_tab_matriz.addWidget(self.lbl_nome_razao_social_matriz, 0, 2, 1, 1)

        self.txt_codigo_empresa = QLineEdit(self.tab_matriz)
        self.txt_codigo_empresa.setObjectName(u"txt_codigo_empresa")
        self.txt_codigo_empresa.setMinimumSize(QSize(141, 0))
        self.txt_codigo_empresa.setMaximumSize(QSize(200, 16777215))
        self.txt_codigo_empresa.setFont(font2)
        self.txt_codigo_empresa.setStyleSheet(u"QLineEdit#txt_codigo_empresa{\n"
                                              "	background-color: #fff;\n"
                                              "	border: 1px solid gray;\n"
                                              "	border-radius: 5px;\n"
                                              "}\n"
                                              "QLineEdit#txt_codigo_empresa:focus{\n"
                                              "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                              "}\n"
                                              "QLineEdit#txt_codigo_empresa:disabled {\n"
                                              "	background-color:  #dcdcdc;\n"
                                              "	color: #6a6767;\n"
                                              "	border: 1px solid gray;\n"
                                              "}")

        self.grl_tab_matriz.addWidget(self.txt_codigo_empresa, 1, 0, 1, 2)

        self.txt_nome_razao_social_matriz = QLineEdit(self.tab_matriz)
        self.txt_nome_razao_social_matriz.setObjectName(u"txt_nome_razao_social_matriz")
        self.txt_nome_razao_social_matriz.setMinimumSize(QSize(371, 20))
        self.txt_nome_razao_social_matriz.setFont(font2)
        self.txt_nome_razao_social_matriz.setStyleSheet(u"QLineEdit#txt_nome_razao_social_matriz{\n"
                                                        "	background-color: #fff;\n"
                                                        "	border: 1px solid gray;\n"
                                                        "	border-radius: 5px;\n"
                                                        "}\n"
                                                        "QLineEdit#txt_nome_razao_social_matriz:focus{\n"
                                                        "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                                        "}\n"
                                                        "QLineEdit#txt_nome_razao_social_matriz:disabled {\n"
                                                        "	background-color:  #dcdcdc;\n"
                                                        "	color: #6a6767;\n"
                                                        "	border: 1px solid gray;\n"
                                                        "}")
        self.txt_nome_razao_social_matriz.setMaxLength(75)

        self.grl_tab_matriz.addWidget(self.txt_nome_razao_social_matriz, 1, 2, 1, 2)

        self.lbl_cpf_cnpj_matriz = QLabel(self.tab_matriz)
        self.lbl_cpf_cnpj_matriz.setObjectName(u"lbl_cpf_cnpj_matriz")
        self.lbl_cpf_cnpj_matriz.setFont(font2)

        self.grl_tab_matriz.addWidget(self.lbl_cpf_cnpj_matriz, 2, 0, 1, 1)

        self.lbl_inscricao_estadual_matriz = QLabel(self.tab_matriz)
        self.lbl_inscricao_estadual_matriz.setObjectName(u"lbl_inscricao_estadual_matriz")
        self.lbl_inscricao_estadual_matriz.setFont(font2)

        self.grl_tab_matriz.addWidget(self.lbl_inscricao_estadual_matriz, 2, 2, 1, 1)

        self.txt_cpf_cnpj_matriz = QLineEdit(self.tab_matriz)
        self.txt_cpf_cnpj_matriz.setObjectName(u"txt_cpf_cnpj_matriz")
        self.txt_cpf_cnpj_matriz.setMinimumSize(QSize(141, 0))
        self.txt_cpf_cnpj_matriz.setMaximumSize(QSize(200, 16777215))
        self.txt_cpf_cnpj_matriz.setFont(font2)
        self.txt_cpf_cnpj_matriz.setStyleSheet(u"QLineEdit#txt_cpf_cnpj_matriz{\n"
                                               "	background-color: #fff;\n"
                                               "	border: 1px solid gray;\n"
                                               "	border-radius: 5px;\n"
                                               "}\n"
                                               "QLineEdit#txt_cpf_cnpj_matriz:focus{\n"
                                               "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                               "}\n"
                                               "QLineEdit#txt_cpf_cnpj_matriz:disabled {\n"
                                               "	background-color:  #dcdcdc;\n"
                                               "	color: #6a6767;\n"
                                               "	border: 1px solid gray;\n"
                                               "}")
        self.txt_cpf_cnpj_matriz.setMaxLength(15)

        self.grl_tab_matriz.addWidget(self.txt_cpf_cnpj_matriz, 3, 0, 1, 2)

        self.txt_inscricao_estadual_matriz = QLineEdit(self.tab_matriz)
        self.txt_inscricao_estadual_matriz.setObjectName(u"txt_inscricao_estadual_matriz")
        self.txt_inscricao_estadual_matriz.setMinimumSize(QSize(141, 0))
        self.txt_inscricao_estadual_matriz.setMaximumSize(QSize(200, 16777215))
        self.txt_inscricao_estadual_matriz.setFont(font2)
        self.txt_inscricao_estadual_matriz.setStyleSheet(u"QLineEdit#txt_inscricao_estadual_matriz{\n"
                                                         "	background-color: #fff;\n"
                                                         "	border: 1px solid gray;\n"
                                                         "	border-radius: 5px;\n"
                                                         "}\n"
                                                         "QLineEdit#txt_inscricao_estadual_matriz:focus{\n"
                                                         "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                                         "}\n"
                                                         "QLineEdit#txt_inscricao_estadual_matriz:disabled {\n"
                                                         "	background-color:  #dcdcdc;\n"
                                                         "	color: #6a6767;\n"
                                                         "	border: 1px solid gray;\n"
                                                         "}")
        self.txt_inscricao_estadual_matriz.setMaxLength(15)

        self.grl_tab_matriz.addWidget(self.txt_inscricao_estadual_matriz, 3, 2, 1, 1)

        self.separacao_rg_borda_tb_wiget = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_tab_matriz.addItem(self.separacao_rg_borda_tb_wiget, 3, 3, 1, 1)

        self.separacao_campos_matriz_borda_tab_widget = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grl_tab_matriz.addItem(self.separacao_campos_matriz_borda_tab_widget, 4, 1, 1, 1)

        self.tab_informcoes.addTab(self.tab_matriz, "")

        self.tab_geral = QWidget()
        self.tab_geral.setObjectName(u"tab_geral")

        self.grl_tab_geral = QGridLayout(self.tab_geral)
        self.grl_tab_geral.setObjectName(u"grl_tab_geral")

        self.lbl_situacao = QLabel(self.tab_geral)
        self.lbl_situacao.setObjectName(u"lbl_situacao")
        self.lbl_situacao.setFont(font2)

        self.grl_tab_geral.addWidget(self.lbl_situacao, 0, 0, 1, 1)

        self.lbl_data_cadastro = QLabel(self.tab_geral)
        self.lbl_data_cadastro.setObjectName(u"lbl_data_cadastro")
        self.lbl_data_cadastro.setFont(font2)

        self.grl_tab_geral.addWidget(self.lbl_data_cadastro, 0, 1, 1, 1)

        self.lbl_data_modificacao = QLabel(self.tab_geral)
        self.lbl_data_modificacao.setObjectName(u"lbl_data_modificacao")
        self.lbl_data_modificacao.setFont(font2)

        self.grl_tab_geral.addWidget(self.lbl_data_modificacao, 0, 2, 1, 1)

        self.lbl_usuario_que_criou = QLabel(self.tab_geral)
        self.lbl_usuario_que_criou.setObjectName(u"lbl_usuario_que_criou")
        self.lbl_usuario_que_criou.setFont(font2)

        self.grl_tab_geral.addWidget(self.lbl_usuario_que_criou, 0, 3, 1, 1)

        self.cb_situacao = QComboBox(self.tab_geral)
        self.cb_situacao.setObjectName(u"cb_situacao")
        self.cb_situacao.setMinimumSize(QSize(100, 0))
        self.cb_situacao.setFont(font2)
        self.cb_situacao.setStyleSheet(u"QComboBox#cb_situacao {\n"
                                       "	background-color: #eeeeee;\n"
                                       "	color: #6a6767;\n"
                                       "	border: 1px solid gray;\n"
                                       "	border-radius: 5px;\n"
                                       "}\n"
                                       "QComboBox#cb_situacao:focus{\n"
                                       "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                       "}\n"
                                       "QComboBox#cb_situacao:disabled {\n"
                                       "	background-color:  #dcdcdc;\n"
                                       "	color: #6a6767;\n"
                                       "	border: 1px solid gray;\n"
                                       "}\n"
                                       "QHeaderView::section QComboBox {\n"
                                       "    background-color: #585A5C;\n"
                                       "    color: #F0F0F0;\n"
                                       "}\n"
                                       "QComboBox::drop-down {\n"
                                       "    border: 0;\n"
                                       "subcontrol-position: right center;\n"
                                       "    subcontrol-origin: margin;\n"
                                       "}\n"
                                       "QComboBox::down-arrow {\n"
                                       "	subcontrol-position: right center;\n"
                                       "    subcontrol-origin: margin;\n"
                                       "	margin-right: 3px;\n"
                                       "    background-image: url(C:/Users/Cauneto/Documents/RPA/image/dropdown.png);\n"
                                       "	background-position: center;\n"
                                       "	background-repeat: no-repeat;\n"
                                       "}")

        self.grl_tab_geral.addWidget(self.cb_situacao, 1, 0, 1, 1)

        self.txt_data_registro = QLineEdit(self.tab_geral)
        self.txt_data_registro.setObjectName(u"txt_data_registro")
        self.txt_data_registro.setEnabled(False)
        self.txt_data_registro.setMaximumSize(QSize(151, 25))
        self.txt_data_registro.setFont(font2)
        self.txt_data_registro.setStyleSheet(u"QLineEdit#txt_data_registro{\n"
                                             "	background-color: #fff;\n"
                                             "	border: 1px solid gray;\n"
                                             "	border-radius: 5px;\n"
                                             "}\n"
                                             "QLineEdit#txt_data_registro:focus{\n"
                                             "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                             "}\n"
                                             "QLineEdit#txt_data_registro:disabled {\n"
                                             "	background-color:  #dcdcdc;\n"
                                             "	color: #6a6767;\n"
                                             "	border: 1px solid gray;\n"
                                             "}")
        self.txt_data_registro.setMaxLength(10)

        self.grl_tab_geral.addWidget(self.txt_data_registro, 1, 1, 1, 1)

        self.txt_data_modificacao = QLineEdit(self.tab_geral)
        self.txt_data_modificacao.setObjectName(u"txt_data_modificacao")
        self.txt_data_modificacao.setEnabled(False)
        self.txt_data_modificacao.setMaximumSize(QSize(152, 25))
        self.txt_data_modificacao.setFont(font2)
        self.txt_data_modificacao.setStyleSheet(u"QLineEdit#txt_data_modificacao{\n"
                                                "	background-color: #fff;\n"
                                                "	border: 1px solid gray;\n"
                                                "	border-radius: 5px;\n"
                                                "}\n"
                                                "QLineEdit#txt_data_modificacao:focus{\n"
                                                "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                                "}\n"
                                                "QLineEdit#txt_data_modificacao:disabled {\n"
                                                "	background-color:  #dcdcdc;\n"
                                                "	color: #6a6767;\n"
                                                "	border: 1px solid gray;\n"
                                                "}")
        self.txt_data_modificacao.setMaxLength(10)

        self.grl_tab_geral.addWidget(self.txt_data_modificacao, 1, 2, 1, 1)

        self.txt_usuario_criou = QLineEdit(self.tab_geral)
        self.txt_usuario_criou.setObjectName(u"txt_usuario_criou")
        self.txt_usuario_criou.setEnabled(False)
        self.txt_usuario_criou.setMaximumSize(QSize(250, 16777215))
        self.txt_usuario_criou.setFont(font2)
        self.txt_usuario_criou.setStyleSheet(u"QLineEdit#txt_usuario_criou{\n"
                                             "	background-color: #fff;\n"
                                             "	border: 1px solid gray;\n"
                                             "	border-radius: 5px;\n"
                                             "}\n"
                                             "QLineEdit#txt_usuario_criou:focus{\n"
                                             "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                             "}\n"
                                             "QLineEdit#txt_usuario_criou:disabled {\n"
                                             "	background-color:  #dcdcdc;\n"
                                             "	color: #6a6767;\n"
                                             "	border: 1px solid gray;\n"
                                             "}")

        self.grl_tab_geral.addWidget(self.txt_usuario_criou, 1, 3, 1, 1)

        self.separacao_usuario_borda = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_tab_geral.addItem(self.separacao_usuario_borda, 1, 4, 1, 1)

        self.lbl_observacao = QLabel(self.tab_geral)
        self.lbl_observacao.setObjectName(u"lbl_observacao")
        self.lbl_observacao.setFont(font2)

        self.grl_tab_geral.addWidget(self.lbl_observacao, 2, 0, 1, 1)

        self.txt_observcao = QTextEdit(self.tab_geral)
        self.txt_observcao.setObjectName(u"txt_observcao")
        self.txt_observcao.setMinimumSize(QSize(0, 51))
        self.txt_observcao.setFont(font2)
        self.txt_observcao.setStyleSheet(u"QTextEdit#txt_observcao{\n"
                                         "	background-color: #fff;\n"
                                         "	border: 1px solid gray;\n"
                                         "	border-radius: 5px;\n"
                                         "}\n"
                                         "QTextEdit#txt_observcao:focus{\n"
                                         "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                         "}\n"
                                         "QTextEdit#txt_observcao:disabled {\n"
                                         "	background-color:  #dcdcdc;\n"
                                         "	color: #6a6767;\n"
                                         "	border: 1px solid gray;\n"
                                         "}")

        self.grl_tab_geral.addWidget(self.txt_observcao, 3, 0, 1, 5)

        self.separacao_campo_observacao_borda_tab_widget = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grl_tab_geral.addItem(self.separacao_campo_observacao_borda_tab_widget, 4, 0, 1, 1)

        self.tab_informcoes.addTab(self.tab_geral, "")

        self.grl_campo_dados.addWidget(self.tab_informcoes, 12, 0, 1, 5)

        self.separacao_celular_borda_lateral = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_campo_dados.addItem(self.separacao_celular_borda_lateral, 9, 2, 1, 1)

        self.vrl_main_registro_empresa.addWidget(self.grb_compos_dados)

        self.grl_registro_empresa.addWidget(self.fra_main_registro_empresa, 0, 0, 1, 1)

        QWidget.setTabOrder(self.txt_codigo, self.cb_tipo_pessoa)
        QWidget.setTabOrder(self.cb_tipo_pessoa, self.cb_tipo_empresa)
        QWidget.setTabOrder(self.cb_tipo_empresa, self.txt_nome_razao_social)
        QWidget.setTabOrder(self.txt_nome_razao_social, self.txt_nome_fantasia)
        QWidget.setTabOrder(self.txt_nome_fantasia, self.txt_cpf_cnpj)
        QWidget.setTabOrder(self.txt_cpf_cnpj, self.txt_inscricao_estadual)
        QWidget.setTabOrder(self.txt_inscricao_estadual, self.txt_inscricao_municipal)
        QWidget.setTabOrder(self.txt_inscricao_municipal, self.txt_telefone)
        QWidget.setTabOrder(self.txt_telefone, self.txt_celular)
        QWidget.setTabOrder(self.txt_celular, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.txt_cep)
        QWidget.setTabOrder(self.txt_cep, self.txt_cidade)
        QWidget.setTabOrder(self.txt_cidade, self.txt_estado)
        QWidget.setTabOrder(self.txt_estado, self.txt_endereco)
        QWidget.setTabOrder(self.txt_endereco, self.txt_complemento)
        QWidget.setTabOrder(self.txt_complemento, self.txt_bairro)
        QWidget.setTabOrder(self.txt_bairro, self.txt_codigo_empresa)
        QWidget.setTabOrder(self.txt_codigo_empresa, self.txt_nome_razao_social_matriz)
        QWidget.setTabOrder(self.txt_nome_razao_social_matriz, self.txt_cpf_cnpj_matriz)
        QWidget.setTabOrder(self.txt_cpf_cnpj_matriz, self.txt_inscricao_estadual_matriz)
        QWidget.setTabOrder(self.txt_inscricao_estadual_matriz, self.cb_situacao)
        QWidget.setTabOrder(self.cb_situacao, self.txt_data_registro)
        QWidget.setTabOrder(self.txt_data_registro, self.txt_data_modificacao)
        QWidget.setTabOrder(self.txt_data_modificacao, self.txt_usuario_criou)
        QWidget.setTabOrder(self.txt_usuario_criou, self.txt_observcao)
        QWidget.setTabOrder(self.txt_observcao, self.btn_buscar_arquivo_imagem_logo)
        QWidget.setTabOrder(self.btn_buscar_arquivo_imagem_logo, self.btn_deletar_imagem_logo)

        self.retranslateUi(frm_registro_empresa)

        self.tab_informcoes.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(frm_registro_empresa)

    def retranslateUi(self, frm_registro_empresa):
        frm_registro_empresa.setWindowTitle(QCoreApplication.translate("frm_registro_empresa", u"Cadastro Empresa", None))
        frm_registro_empresa.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Formul\u00e1rio de cadastro de empresa</p></body></html>", None))
        self.grb_botoes.setTitle("")
        self.btn_primeiro.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Primeiro Registro", None))
        self.btn_primeiro.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para ir ao primeiro registro</p></body></html>", None))
        self.btn_primeiro.setText("")
        self.btn_primeiro.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+Alt+Left", None))
        self.btn_anterior.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Registro Anterior", None))
        self.btn_anterior.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para ir ao registro anterior</p></body></html>", None))
        self.btn_anterior.setText("")
        self.btn_anterior.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+Left", None))
        self.btn_proximo.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Pr\u00f3xima Registro", None))
        self.btn_proximo.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para ir ao pr\u00f3ximo registro</p></body></html>", None))
        self.btn_proximo.setText("")
        self.btn_proximo.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+Right", None))
        self.btn_ultimo.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"\u00daltima Registro", None))
        self.btn_ultimo.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para ir ao ultimo registro</p></body></html>", None))
        self.btn_ultimo.setText("")
        self.btn_ultimo.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+Alt+Right", None))
        self.btn_pesquisar_registro.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Pesquisar", None))
        self.btn_pesquisar_registro.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para pesquisar os registros de empresa</p></body></html>", None))
        self.btn_pesquisar_registro.setText("")
        self.btn_pesquisar_registro.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"F12", None))
        self.btn_pesquisar_codigo.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Buscar", None))
        self.btn_pesquisar_codigo.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para buscar empresa pelo codigo</p></body></html>", None))
        self.btn_pesquisar_codigo.setText("")
        self.btn_pesquisar_codigo.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+N", None))
        self.btn_imprimir.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Imprimir", None))
        self.btn_imprimir.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para imprimir registro de empresa</p></body></html>", None))
        self.btn_imprimir.setText("")
        self.btn_imprimir.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+P", None))
        self.btn_copiar.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Duplicar", None))
        self.btn_copiar.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para duplicar registro</p></body></html>", None))
        self.btn_copiar.setText("")
        self.btn_novo.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Novo", None))
        self.btn_novo.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para cadastrar uma novo registro de empresa</p></body></html>", None))
        self.btn_novo.setText("")
        self.btn_novo.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+N", None))
        self.btn_editar.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Editar", None))
        self.btn_editar.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para editar o registro de empresa</p></body></html>", None))
        self.btn_editar.setText("")
        self.btn_editar.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+E", None))
        self.btn_salvar.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Salvar", None))
        self.btn_salvar.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para salvar o registro de empresa</p></body></html>", None))
        self.btn_salvar.setText("")
        self.btn_salvar.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+S", None))
        self.btn_cancelar.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Cancelar", None))
        self.btn_cancelar.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o para cancelar a opera\u00e7\u00e3o</p></body></html>", None))
        self.btn_cancelar.setText("")
        self.btn_cancelar.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+F", None))
        self.btn_deletar.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Deletar", None))
        self.btn_deletar.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Bot\u00e3o de deletar o registro de empresa</p></body></html>", None))
        self.btn_deletar.setText("")
        self.btn_deletar.setShortcut(QCoreApplication.translate("frm_registro_empresa", u"Ctrl+D", None))
        self.grb_compos_dados.setTitle("")
        self.lbl_codigo.setText(QCoreApplication.translate("frm_registro_empresa", u"Codigo", None))
        self.lbl_tipo_pessoa.setText(QCoreApplication.translate("frm_registro_empresa", u"Tipo Pessoa", None))
        self.lbl_tipo_empresa.setText(QCoreApplication.translate("frm_registro_empresa", u"Tipo Empresa", None))
        self.txt_codigo.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Codigo", None))
        self.txt_codigo.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do codigo do registro da empresa</p></body></html>", None))
        self.cb_tipo_pessoa.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Tipo Pessoa", None))
        self.cb_tipo_pessoa.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo de sele\u00e7\u00e3o do tipo da pessoa</p></body></html>", None))
        self.cb_tipo_empresa.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Tipo Empresa", None))
        self.cb_tipo_empresa.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo de sele\u00e7\u00e3o do tipo da empresa</p></body></html>", None))
        self.btn_buscar_arquivo_imagem_logo.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Buscar Logotipo", None))
        self.btn_buscar_arquivo_imagem_logo.setText("")
        self.lbl_logo.setText("")
        self.btn_deletar_imagem_logo.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Excluir Logotipo", None))
        self.btn_deletar_imagem_logo.setText("")
        self.lbl_logotipo.setText(QCoreApplication.translate("frm_registro_empresa", u"Logotipo", None))
        self.lbl_nome_razao_social.setText(QCoreApplication.translate("frm_registro_empresa", u"Nome / Raz\u00e3o Social", None))
        self.txt_nome_razao_social.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Nome / Raz\u00e3o Social", None))
        self.txt_nome_razao_social.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do nome ou razao social da empresa</p></body></html>", None))
        self.lbl_sobrenome_fantasia.setText(QCoreApplication.translate("frm_registro_empresa", u"Sobrenome / Fantasia", None))
        self.txt_nome_fantasia.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Sobrenome / Fantasia", None))
        self.txt_nome_fantasia.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do sobrenome ou nome fantasia da empresa</p></body></html>", None))
        self.lbl_cnpj.setText(QCoreApplication.translate("frm_registro_empresa", u"CPF / CNPJ", None))
        self.lbl_inscricao_estadual.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Expeditor", None))
        self.lbl_inscricao_estadual.setText(QCoreApplication.translate("frm_registro_empresa", u"RG / Ins. Estadual", None))
        self.lbl_inscricao_municipal.setText(QCoreApplication.translate("frm_registro_empresa", u"Ins. Municipal", None))
        self.txt_cpf_cnpj.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"CPF", None))
        self.txt_cpf_cnpj.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do n\u00famero do CPF ou CNPJ da empresa</p></body></html>", None))
        self.txt_inscricao_estadual.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"RG / Ins. Municipal", None))
        self.txt_inscricao_estadual.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do n\u00famero do RG ou Inscri\u00e7\u00e3o Estadual da empresa</p></body></html>", None))
        self.txt_inscricao_municipal.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Ins. Municipal", None))
        self.txt_inscricao_municipal.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do n\u00famero da Inscri\u00e7\u00e3o Municipal da empresa</p></body></html>", None))
        self.lbl_telefone.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Expeditor", None))
        self.lbl_telefone.setText(QCoreApplication.translate("frm_registro_empresa", u"Telefone", None))
        self.lbl_celular.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Expeditor", None))
        self.lbl_celular.setText(QCoreApplication.translate("frm_registro_empresa", u"Celular", None))
        self.txt_telefone.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Telefone", None))
        self.txt_telefone.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do n\u00famero de telefone da empresa</p></body></html>", None))
        self.txt_celular.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Celular", None))
        self.txt_celular.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do n\u00famero de celular da empresa</p></body></html>", None))
        self.lbl_email.setText(QCoreApplication.translate("frm_registro_empresa", u"E-mail", None))
        self.txt_email.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"E-mail", None))
        self.txt_email.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do endere\u00e7o de e-mail da empresa</p></body></html>", None))
        self.lbl_cep.setText(QCoreApplication.translate("frm_registro_empresa", u"CEP", None))
        self.lbl_cidade.setText(QCoreApplication.translate("frm_registro_empresa", u"Cidade", None))
        self.lbl_estado.setText(QCoreApplication.translate("frm_registro_empresa", u"Estado", None))
        self.txt_cep.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"CEP", None))
        self.txt_cep.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do n\u00famero do CEP do endere\u00e7o onde fica sediada a empresa</p></body></html>", None))
        self.txt_cidade.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Cidade", None))
        self.txt_cidade.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do nome da cidade onde fica sediada a empresa</p></body></html>", None))
        self.txt_estado.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Estado", None))
        self.txt_estado.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do nome do estado onde fica seidada a empresa</p></body></html>", None))
        self.lbl_endereco.setText(QCoreApplication.translate("frm_registro_empresa", u"Endere\u00e7o", None))
        self.lbl_complemento.setText(QCoreApplication.translate("frm_registro_empresa", u"Complemento", None))
        self.txt_endereco.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Endere\u00e7o", None))
        self.txt_endereco.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do endere\u00e7o da empresa</p></body></html>", None))
        self.txt_complemento.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Complemento", None))
        self.txt_complemento.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do complemento do endere\u00e7o da empresa</p></body></html>", None))
        self.lbl_bairro.setText(QCoreApplication.translate("frm_registro_empresa", u"Bairro", None))
        self.txt_bairro.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Bairro", None))
        self.txt_bairro.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do nome do bairro do endere\u00e7o da empresa</p></body></html>", None))
        self.tab_informcoes.setTabText(self.tab_informcoes.indexOf(self.tab_endereco), QCoreApplication.translate("frm_registro_empresa", u"Endere\u00e7o", None))
        self.lbl_codigo_matriz.setText(QCoreApplication.translate("frm_registro_empresa", u"Codigo", None))
        self.lbl_nome_razao_social_matriz.setText(QCoreApplication.translate("frm_registro_empresa", u"Nome / Raz\u00e3o Social", None))
        self.txt_codigo_empresa.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Codigo", None))
        self.txt_codigo_empresa.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do codigo do registro da empresa matriz</p></body></html>", None))
        self.txt_nome_razao_social_matriz.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Nome / Raz\u00e3o Social", None))
        self.txt_nome_razao_social_matriz.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do nome ou razao social da empresa matriz</p></body></html>", None))
        self.lbl_cpf_cnpj_matriz.setText(QCoreApplication.translate("frm_registro_empresa", u"CPF / CNPJ", None))
        self.lbl_inscricao_estadual_matriz.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Expeditor", None))
        self.lbl_inscricao_estadual_matriz.setText(QCoreApplication.translate("frm_registro_empresa", u"RG / Ins. Estadual", None))
        self.txt_cpf_cnpj_matriz.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"CPF", None))
        self.txt_cpf_cnpj_matriz.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do n\u00famero do CPF ou CNPJ da empresa matriz</p></body></html>", None))
        self.txt_inscricao_estadual_matriz.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"RG / Ins. Municipal", None))
        self.txt_inscricao_estadual_matriz.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo do n\u00famero do RG ou Inscri\u00e7\u00e3o Estadual da empresa matriz</p></body></html>", None))
        self.tab_informcoes.setTabText(self.tab_informcoes.indexOf(self.tab_matriz), QCoreApplication.translate("frm_registro_empresa", u"Matriz", None))
        self.lbl_situacao.setText(QCoreApplication.translate("frm_registro_empresa", u"Situa\u00e7\u00e3o", None))
        self.lbl_data_cadastro.setText(QCoreApplication.translate("frm_registro_empresa", u"Data Cadastro", None))
        self.lbl_data_modificacao.setText(QCoreApplication.translate("frm_registro_empresa", u"Data Mododifica\u00e7\u00e3o", None))
        self.lbl_usuario_que_criou.setText(QCoreApplication.translate("frm_registro_empresa", u"Usu\u00e1rio que Criou", None))
        self.cb_situacao.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Situa\u00e7\u00e3o", None))
        self.cb_situacao.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo de sele\u00e7\u00e3o da situa\u00e7\u00e3o cadastral da empresa</p></body></html>", None))
        self.txt_data_registro.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Data Cadastro", None))
        self.txt_data_registro.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo da data de cria\u00e7\u00e3o do registro da empresa</p></body></html>", None))
        self.txt_data_registro.setPlaceholderText(QCoreApplication.translate("frm_registro_empresa", u"DIA / M\u00caS / ANO", None))
        self.txt_data_modificacao.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Data Modifica\u00e7\u00e3o", None))
        self.txt_data_modificacao.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo da data de modifica\u00e7\u00e3o do registro da empresa</p></body></html>", None))
        self.txt_data_modificacao.setPlaceholderText(QCoreApplication.translate("frm_registro_empresa", u"DIA / M\u00caS / ANO", None))
        self.txt_usuario_criou.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Usu\u00e1rio que Criou", None))
        self.txt_usuario_criou.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo usu\u00e1rio que criou o registro</p></body></html>", None))
        self.lbl_observacao.setText(QCoreApplication.translate("frm_registro_empresa", u"Observa\u00e7\u00e3o", None))
        self.txt_observcao.setToolTip(QCoreApplication.translate("frm_registro_empresa", u"Observa\u00e7\u00e3o", None))
        self.txt_observcao.setWhatsThis(QCoreApplication.translate("frm_registro_empresa", u"<html><head/><body><p>Campo de observa\u00e7\u00f5es da empresa</p></body></html>", None))
        self.tab_informcoes.setTabText(self.tab_informcoes.indexOf(self.tab_geral), QCoreApplication.translate("frm_registro_empresa", u"Geral", None))
