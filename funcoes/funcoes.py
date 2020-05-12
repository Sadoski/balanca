from PySide2.QtWidgets import QGridLayout, QLayout


class Funcoes:

    def limpa_formulario(self, frm):
        for i in reversed(range(len(frm.children()))):
            frm.children()[i].deleteLater()
            print(frm.layout())

    def set_grid_layout_conteudo(self, frame):
        self.grl_fra_conteudo = QGridLayout(frame)
        self.grl_fra_conteudo.setSpacing(0)
        self.grl_fra_conteudo.setObjectName(u"grl_fra_conteudo")
        self.grl_fra_conteudo.setSizeConstraint(QLayout.SetMinimumSize)
        self.grl_fra_conteudo.setContentsMargins(0, 0, 0, 0)

class StatusBar:
    pass