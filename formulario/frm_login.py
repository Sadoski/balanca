# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide2.QtGui import (QFont, QIcon, QPixmap)
from PySide2.QtWidgets import *


class UiFrmLogin(object):
    def setupUi(self, frm_login):
        if frm_login.objectName():
            frm_login.setObjectName(u"frm_login")
        frm_login.resize(521, 300)
        frm_login.setMinimumSize(QSize(521, 300))
        frm_login.setMaximumSize(QSize(521, 300))
        frm_login.setStyleSheet(u"")
        frm_login.setAttribute(Qt.WA_NoSystemBackground)
        frm_login.setAttribute(Qt.WA_TranslucentBackground)
        frm_login.setWindowFlags(Qt.FramelessWindowHint)
        
        self.fra_lateral = QFrame(frm_login)
        self.fra_lateral.setObjectName(u"fra_lateral")
        self.fra_lateral.setGeometry(QRect(0, 0, 151, 301))
        self.fra_lateral.setStyleSheet(u"QFrame {\n"
                                       "	background: rgb(255,255,255,.9)\n"
                                       "}")
        self.fra_lateral.setFrameShape(QFrame.StyledPanel)
        self.fra_lateral.setFrameShadow(QFrame.Raised)

        self.lbl_login = QLabel(self.fra_lateral)
        self.lbl_login.setObjectName(u"lbl_login")
        self.lbl_login.setGeometry(QRect(27, 10, 91, 41))
        self.lbl_login.setStyleSheet(u"QLabel {\n"
                                     "	color: gray;\n"
                                     "	font-size:32px;\n"
                                     "	background: transparent;\n"
                                     "}")

        self.lbl_logo = QLabel(self.fra_lateral)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(20, 87, 111, 101))
        self.lbl_logo.setStyleSheet("QLabel {"
                                    "    background: transparent;"
                                    "}")
        self.lbl_logo.setPixmap(QPixmap(u"./imagens/logo-bl-.png"))
        self.lbl_logo.setScaledContents(True)
        self.fra_campos_login = QFrame(frm_login)

        self.fra_campos_login = QFrame(frm_login)
        self.fra_campos_login.setObjectName(u"fra_campos_login")
        self.fra_campos_login.setGeometry(QRect(150, 0, 371, 301))
        self.fra_campos_login.setStyleSheet(u"QFrame {\n"
                                            "    background: rgb(0,0,74,.9);\n"
                                            "}")
        self.fra_campos_login.setFrameShape(QFrame.StyledPanel)
        self.fra_campos_login.setFrameShadow(QFrame.Raised)

        self.txt_senha = QLineEdit(self.fra_campos_login)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(26, 130, 321, 20))
        self.txt_senha.setMinimumSize(QSize(321, 20))
        font = QFont()
        font.setPointSize(11)
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet(u"QLineEdit#txt_senha{\n"
                                     "	background: transparent;\n"
                                     "	border: none;\n"
                                     "	border-bottom: 1px solid white;\n"
                                     "	color: white;\n"
                                     "}\n"
                                     "QLineEdit#txt_senha:focus{\n"
                                     "	border-bottom: 1px solid rgba(81, 203, 238, 1);\n"
                                     "}\n")
        self.txt_senha.setMaxLength(75)

        self.txt_usuario = QLineEdit(self.fra_campos_login)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(26, 80, 321, 20))
        self.txt_usuario.setMinimumSize(QSize(321, 20))
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet(u"QLineEdit#txt_usuario{\n"
                                       "	background: transparent;\n"
                                       "	border: none;\n"
                                       "	border-bottom: 1px solid white;\n"
                                       "	color: white;\n"
                                       "}\n"
                                       "QLineEdit#txt_usuario:focus{\n"
                                       "	border-bottom: 1px solid rgba(81, 203, 238, 1);\n"
                                       "}\n")
        self.txt_usuario.setMaxLength(75)

        self.btn_minimizar = QPushButton(self.fra_campos_login)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setGeometry(QRect(316, 0, 28, 24))
        self.btn_minimizar.setMinimumSize(QSize(28, 24))
        self.btn_minimizar.setFocusPolicy(Qt.NoFocus)
        self.btn_minimizar.setStyleSheet(u"QPushButton#btn_minimizar{\n"
                                         "	color: white;\n"
                                         "	border:1px;\n"
                                         "	background: transparent;\n"
                                         "}\n"
                                         "QPushButton#btn_minimizar:hover{\n"
                                         "	background: rgba(255,255,255,.1);\n"
                                         "}\n"
                                         "QPushButton#btn_minimizar:pressed {\n"
                                         "	background: rgba(255,255,255,.2);\n"
                                         "}")
        icon = QIcon()
        icon.addFile(u"./imagens/minimizar-.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon)
        self.btn_minimizar.setIconSize(QSize(16, 16))
        self.btn_minimizar.setFlat(True)

        self.btn_close = QPushButton(self.fra_campos_login)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(344, 0, 28, 24))
        self.btn_close.setMinimumSize(QSize(28, 24))
        self.btn_close.setFocusPolicy(Qt.NoFocus)
        self.btn_close.setStyleSheet(u"QPushButton#btn_close{\n"
                                     "	border: 0px;\n"
                                     "	background: transparent;\n"
                                     "}\n"
                                     "QPushButton#btn_close:hover{\n"
                                     "	border: 0px solid rgba(255,255,255,.1);\n"
                                     "	background: rgba(255,255,255,.1);\n"
                                     "}\n"
                                     "QPushButton#btn_close:pressed {\n"
                                     "	border: 0px solid rgba(255,255,255,.1);\n"
                                     "	background: rgba(255,255,255,.2);\n"
                                     "}")
        icon1 = QIcon()
        icon1.addFile(u"./imagens/fechar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QSize(16, 16))
        self.btn_close.setFlat(True)

        self.btn_login = QPushButton(self.fra_campos_login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(26, 160, 321, 36))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.btn_login.setFont(font1)
        self.btn_login.setFocusPolicy(Qt.TabFocus)
        self.btn_login.setStyleSheet(u"QPushButton#btn_login{\n"
                                     "	background-color: #0080ff ;\n"
                                     "	color: #fff;\n"
                                     "	border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton#btn_login:hover{\n"
                                     "	background-color:  #0073e6;\n"
                                     "}\n"
                                     "QPushButton#btn_login:pressed {\n"
                                     "	background-color: #0059b3;\n"
                                     "}\n"
                                     "QPushButton#btn_login:disabled {\n"
                                     "	background-color:  #a6a6a6;\n"
                                     "	color: #6a6767;\n"
                                     "}")
        self.btn_login.setIconSize(QSize(36, 36))

        self.btn_esqueci_senha = QPushButton(self.fra_campos_login)
        self.btn_esqueci_senha.setObjectName(u"btn_esqueci_senha")
        self.btn_esqueci_senha.setGeometry(QRect(130, 270, 113, 21))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setItalic(True)
        self.btn_esqueci_senha.setFont(font2)
        self.btn_esqueci_senha.setFocusPolicy(Qt.TabFocus)
        self.btn_esqueci_senha.setStyleSheet(u"QPushButton#btn_esqueci_senha{\n"
                                             "	color: white;\n"
                                             "	border: 1px;\n"
                                             "	font-style:italic;\n"
                                             "	background: transparent;\n"
                                             "}\n"
                                             "QPushButton#btn_esqueci_senha:hover{\n"
                                             "	border-bottom: 1px solid white;\n"
                                             "}\n"
                                             "QPushButton#btn_esqueci_senha:pressed {\n"
                                             "	border-bottom: 1px solid white;\n"
                                             "}")
        self.btn_esqueci_senha.setIconSize(QSize(36, 36))

        QWidget.setTabOrder(self.txt_usuario, self.txt_senha)
        QWidget.setTabOrder(self.txt_senha, self.btn_login)
        QWidget.setTabOrder(self.btn_login, self.btn_esqueci_senha)
        QWidget.setTabOrder(self.btn_esqueci_senha, self.btn_minimizar)
        QWidget.setTabOrder(self.btn_minimizar, self.btn_close)

        self.retranslateUi(frm_login)

        QMetaObject.connectSlotsByName(frm_login)

    def retranslateUi(self, frm_login):
        frm_login.setWindowTitle(QCoreApplication.translate("frm_login", u"Log-In", None))
        self.lbl_login.setText(QCoreApplication.translate("frm_login", u"LOGIN", None))
        self.lbl_logo.setText("")
        self.txt_senha.setWhatsThis(QCoreApplication.translate("frm_login", u"<html><head/><body><p>Campo da senha do "
                                                                            "usu\u00e1rio</p></body></html>", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("frm_login", u"Senha", None))
        self.txt_usuario.setWhatsThis(QCoreApplication.translate("frm_login", u"<html><head/><body><p>Campo do nome de "
                                                                              "usu\u00e1rio</p></body></html>", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("frm_login", u"Usu\u00e1rio", None))
        self.btn_login.setWhatsThis(QCoreApplication.translate("frm_login", u"<html><head/><body><p>Bot\u00e3o para "
                                                                            "autenticar o usu\u00e1rio para acessar o "
                                                                            "sistema</p></body></html>", None))
        self.btn_login.setText(QCoreApplication.translate("frm_login", u"Log-In", None))
        self.btn_esqueci_senha.setWhatsThis(QCoreApplication.translate("frm_login", u"<html><head/><body><p>Bot\u00e3o "
                                                                                    "caso tenha esquecido a senha</p>"
                                                                                    "</body></html>", None))
        self.btn_esqueci_senha.setText(QCoreApplication.translate("frm_login", u"Esqueceu a senha?", None))
