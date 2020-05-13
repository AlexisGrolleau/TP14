from PySide2.QtWidgets import QLabel,QWidget,QPushButton,QApplication,QVBoxLayout,QDateEdit


class Window(QWidget):
    def __init__(self,n):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        widget = []
        for i in range(n):
            widget.append(QLabel("Ceci est un label"))
        for i in widget:
            layout.addWidget(i)
        self.setLayout(layout)


if __name__ == "__main__":
   app = QApplication([])
   win = Window(5)
   win.show()
   app.exec_()
