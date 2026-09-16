from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QLabel, QLineEdit
from PyQt6.QtCore import Qt

import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100,100 , 300, 200)

        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.instruct_label = QLabel("Enter your name")
        self.grid.addWidget(self.instruct_label, 0,0)

        self.name_input = QLineEdit(placeholderText = "provide name")
        self.grid.addWidget(self.name_input)

        self.submit_button = QPushButton("Say Hello")
        self.submit_button.clicked.connect(self.say_hello)
        self.grid.addWidget(self.submit_button)

        self.hello_label = QLabel()
        self.grid.addWidget(self.hello_label, 4,0)

        self.setLayout(self.grid)
        self.show()

    def say_hello(self):
        name = "hello " + self.name_input.text()
        self.hello_label.setText(name)


app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())