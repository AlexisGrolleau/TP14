from PySide2.QtWidgets import QTextEdit,QGridLayout,QLabel,QWidget,QPushButton,QApplication,QVBoxLayout,QDateEdit


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        layout = QVBoxLayout()
        layoutgrid = QGridLayout()
        label = QLabel("Laisser nous un commentaire")
        successbutton = QPushButton("Success")
        cancelbutton = QPushButton("Cancel")
        text = QTextEdit()
        layout.addWidget(label)
        layout.addWidget(text)
        layoutgrid.addWidget(successbutton,0,0)
        layoutgrid.addWidget(cancelbutton,0,1)
        layout.addLayout(layoutgrid)
        self.setLayout(layout)


if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
