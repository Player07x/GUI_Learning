from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6.QtGui import QIcon
import sys
from random import choice

titulos_janela = [
    'Meu App',
    'Continua Meu App',
    'Algo na terra',
    'Isso é uma surpresa',
    'Algo parece estar errado'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_vezes_clicado = 0

        self.setWindowTitle('Terceira Janela')
        self.setWindowIcon(QIcon('images/ico.png'))
        self.setMinimumSize(720, 480)

        self.botao = QPushButton('Clique Aqui!')
        self.botao.clicked.connect(self.o_botao_foi_clicado)

        self.windowTitleChanged.connect(self.o_titulo_da_janela_mudou)

        self.setCentralWidget(self.botao)

    def o_botao_foi_clicado(self):
        print('Clicado')
        novo_titulo_janela = choice(titulos_janela)
        print(f'Configurando Título: {novo_titulo_janela}')
        self.setWindowTitle(novo_titulo_janela)

    def o_titulo_da_janela_mudou(self, titulo_janela):
        print(f'Título da janela mudado: {titulo_janela}')

        if titulo_janela == 'Algo parece estar errado':
            self.botao.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
