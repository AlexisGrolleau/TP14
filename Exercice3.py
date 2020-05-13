from PySide2.QtWidgets import QTextEdit,QGridLayout,QLabel,QWidget,QPushButton,QApplication,QVBoxLayout,QDateEdit
from PySide2.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setFixedSize(400,300)
        myicon = QIcon.addFile("fr-flag.png")
        self.setWindowIcon(myicon)
        layout = QVBoxLayout()


if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
