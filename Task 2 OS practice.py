from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from pathlib import Path
import sys
import sqlite3

FILE_PATH = Path(__file__).parent

class Toka_Fitness_Main(QMainWindow): #creates the overlay for the pages including the task bar
    def __init__(self):
        super().__init__()

        self.Stack = QStackedWidget(self)

        login = Login()
        home = Home()

        self.Stack.addWidget(home)
        self.Stack.addWidget(login)

        Toolbar = QToolBar("Toolbar")
        self.addToolBar(Toolbar)

        login_action = QAction("login",self)
        login_action.setStatusTip("Login page")
        login_action.triggered.connect(lambda:self.display(0))
        Toolbar.addAction(login_action)

        home_action = QAction("home",self)
        home_action.setStatusTip("home page")
        home_action.triggered.connect(lambda:self.display(0))
        Toolbar.addAction(home_action)

        self.setCentralWidget(self.Stack)

        self.setGeometry(30, 40, 400, 400)
        self.setWindowTitle('Toka Fitness App')
        self.show()

    def display(self,i):
            self.Stack.setCurrentIndex(i)


class Login(QWidget):
    def __init__(self):
        super().__init__()


class Home(QWidget):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
ex = Toka_Fitness_Main()
sys.exit(app.exec())





        


    