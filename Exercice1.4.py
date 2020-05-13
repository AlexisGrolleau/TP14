from PySide2.QtWidgets import QLabel,QWidget,QPushButton,QApplication,QVBoxLayout,QDateEdit


class Window(QWidget):
    def __init__(self,n):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.label = QLabel("Ceci est un QLabel")
        self.button = QPushButton("Ceci est un QPushButton")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)


if __name__ == "__main__":
   app = QApplication([])
   win = Window(5)
   win.show()
   app.exec_()
