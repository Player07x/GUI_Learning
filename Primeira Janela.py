# QApplication é um manipulador de aplicativos
# QWidget é um widget GUI vazio básico
# Os principais módulos do Qt são QtWidgets, QtGui e QtCore
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtGui import QIcon

import sys


# Subclasse QMainWindow para costumizar sua janela principal da aplicação
class MainWindow(QMainWindow):
    def __init__(self):
        # É necessário chamar o super().__init__() para o Qt configurar o objeto
        super().__init__()

        # Serve setWindowTitle muda o título da janela
        self.setWindowTitle('RPG Game')
        self.setWindowIcon(QIcon('images/ico.png'))

        button = QPushButton('Clique Aqui!')  # Widget
        button.setCheckable(True)
        button.clicked.connect(self.o_botao_foi_clicado)
        button.clicked.connect(self.o_botao_foi_alterado)

        # Defina o widget central da janela
        self.setCentralWidget(button)
        self.setMinimumSize(720, 480)

        # Foi usado o QApplication. Em seguida o geometry para obter um objeto QRect que representa a geometria
        # (incluindo a posição e tamanho) da tela
        # A partir do objeto QRect, podemos obter a largura e altura da tela usando os métodos width() e height()
        self.setMaximumSize(app.primaryScreen().geometry().width(),
                            app.primaryScreen().geometry().height())

    def o_botao_foi_clicado(self):
        print('O botão foi clicado!')

    def o_botao_foi_alterado(self, checked):
        print('Checado?', checked)


# Você precisa de um (apenas um) instância QApplication por aplicação
# Passe sys.argv para permitir argumentos de linha de comando para seu aplicativo
# Se você sabe que não usará linhas de comando, QApplication([]) funciona também.
app = QApplication(sys.argv)

# Cria um Qt widget, que será nossa janela
window = MainWindow()
window.show()  # IMPORTANTE! Janelas são ocultas por padrão.

# Começa o Loop de Eventos
app.exec()

# Sua aplicação não alcança está área até o fim do evento
# Loop Parou
