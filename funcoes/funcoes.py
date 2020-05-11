

class Funcoes:

    def limpa_formulario(self, frm):
        for i in reversed(range(len(frm.children()))):
            frm.children()[i].deleteLater()
