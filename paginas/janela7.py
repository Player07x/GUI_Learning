from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QLabel
from PyQt6.QtGui import QIcon, QAction
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.setWindowTitle('Janela Sete')
        self.setWindowIcon(QIcon('../images/ico.png'))
        self.setMinimumSize(720, 480)

        self.label = QLabel('Texto Central')
        self.setCentralWidget(self.label)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

        context.actionEvent('')


app = QApplication(sys.argv)
window = MainWindow()

app.exec()
