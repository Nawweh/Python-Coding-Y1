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

        self.instruct_label = QLabel("Enter your username")
        self.grid.addWidget(self.instruct_label, 0,0)

        self.name_input = QLineEdit(placeholderText = "provide username")
        self.grid.addWidget(self.name_input)

        self.instruct_label = QLabel("Enter your password")
        self.grid.addWidget(self.instruct_label, 2,0)
        
        self.password_input = QLineEdit(placeholderText = "provide password")
        self.grid.addWidget(self.password_input)

        self.submit_button = QPushButton("Say Hello")
        self.submit_button.clicked.connect(self.user_check)
        self.grid.addWidget(self.submit_button)

        self.submit_label = QLabel()
        self.grid.addWidget(self.submit_label, 6,0)

        self.setLayout(self.grid)
        self.show()

    def user_check(self):
        name = self.name_input.text()
        password = self.password_input.text()
        user_pass = name+password
        if user_pass == "bobblob":
            self.submit_label.setText("YAY PASSWORD (or username) CORRECT")
        else:
            self.submit_label.setText("NOOOO PASSWORD (or username) INCORRECT :(((((")


app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())