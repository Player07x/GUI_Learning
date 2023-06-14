from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Janela Quatro')
        self.setMinimumSize(720, 480)
        self.setWindowIcon(QIcon('../images/ico.png'))

        # Cria um objeto de um label
        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Defina um widget central na Janela
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
