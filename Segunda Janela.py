from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # =============[Cabeçalho do Programa]===================
        self.setWindowTitle('Segunda Janela')
        self.setWindowIcon(QIcon('images/ico.png'))
        self.setMinimumSize(720, 480)
        # =======================================================

        self.botao = QPushButton('Clique Aqui!')
        self.botao.clicked.connect(self.o_botao_foi_clicado)

        self.setCentralWidget(self.botao)

    def o_botao_foi_clicado(self):
        self.botao.setText('Você já me clicou.')
        self.botao.setEnabled(False)

        self.setWindowTitle('Meu App "One Shot"')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()