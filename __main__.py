# -*- coding: utf-8 -*-
"""
Modulo de inicialização da aplicação
"""
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from view.view_frm_principal import Principal


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Principal()
    main.show()
    sys.exit(app.exec_())
