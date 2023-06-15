from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtGui import QIcon, QMouseEvent
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Janela Cinco')
        self.setWindowIcon(QIcon('../images/ico.png'))
        self.setMinimumSize(720, 480)

        self.label = QLabel('Clique nessa janela')
        self.setCentralWidget(self.label)
        self.setMouseTracking(True)

    # As funções abaixo são modificações das funções originais da classe
    def mouseMoveEvent(self, e):
        self.label.setText('mouseMoveEvent')

    def mousePressEvent(self, e):
        self.label.setText('mousePressEvent')

    def mouseReleaseEvent(self, e):
        self.label.setText('mouseReleaseEvent')

    def mouseDoubleClickEvent(self, e):
        self.label.setText('mouseDoubleClickEvent')


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
