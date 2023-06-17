from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6.QtGui import QIcon
import sys
from random import choice

# Lista com nomes para a janela
titulos_janela = [
    'Meu App',
    'Continua Meu App',
    'Algo na terra',
    'Isso é uma surpresa',
    'Algo parece estar errado'
]


# Subclasse de QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_vezes_clicado = 0

        # =================[Configurações da Janela]======================
        self.setWindowTitle('Terceira Janela')
        self.setWindowIcon(QIcon('images/ico.png'))
        self.setMinimumSize(720, 480)
        # ================================================================

        # Criação do botão e verificação se o botão foi clicado
        self.botao = QPushButton('Clique Aqui!')
        self.botao.clicked.connect(self.o_botao_foi_clicado)

        # Comando que disparo o sinal quando o título é alterado
        self.windowTitleChanged.connect(self.o_titulo_da_janela_mudou)

        # Cria um Widget central na tela
        self.setCentralWidget(self.botao)

    # Função que, quando o botão é clicado, escolhe um título aleatóriamente e mud
    def o_botao_foi_clicado(self):
        print('Clicado')
        novo_titulo_janela = choice(titulos_janela)
        print(f'Configurando Título: {novo_titulo_janela}')
        self.setWindowTitle(novo_titulo_janela)

    # Essa função printa o novo título da janela
    # Função que verifica se o título foi alterado para 'Algo parece estar errado'. Se isso acontecer
    # desabilita o botão.
    def o_titulo_da_janela_mudou(self, titulo_janela):
        print(f'Título da janela mudado: {titulo_janela}')

        if titulo_janela == 'Algo parece estar errado':
            self.botao.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
