from PySide2.QtWidgets import QLabel,QWidget,QPushButton,QApplication,QVBoxLayout,QDateEdit

app = QApplication([])
mainWidget = QWidget()

layout = QVBoxLayout()

label = QLabel("Ceci est un label")
button = QPushButton("Ceci est un bouton")
date = QDateEdit()

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(date)

mainWidget.setLayout(layout)

mainWidget.show()
app.exec_()

