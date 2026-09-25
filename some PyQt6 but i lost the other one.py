# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QLabel, QLineEdit, QStackedWidget, QToolBar
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QAction
# import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from pathlib import Path
import sys

FILE_PATH = Path(__file__).parent

class bro_app(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Stack = QStackedWidget(self)

        p1 = page1()
        p2 = page2()
        p3 = page3()
        p4 = page4()
        

        self.Stack.addWidget(p1)
        self.Stack.addWidget(p2)
        self.Stack.addWidget(p3)
        self.Stack.addWidget(p4)

        Toolbar = QToolBar("main toolbar")

        self.addToolBar(Toolbar)

        p1_action = QAction("&page 1",self)
        p1_action.setStatusTip("change to page 1")
        p1_action.triggered.connect( lambda:self.display(0))
        Toolbar.addAction(p1_action)

        p2_action = QAction("page 2",self)
        p2_action.setStatusTip("change to page 2")
        p2_action.triggered.connect( lambda:self.display(1))
        Toolbar.addAction(p2_action)

        p3_action = QAction("page 3",self)
        p3_action.setStatusTip("change to page 3")
        p3_action.triggered.connect( lambda:self.display(2))
        Toolbar.addAction(p3_action)

        p4_action = QAction("page 4",self)
        p4_action.setStatusTip("change to page 4")
        p4_action.triggered.connect( lambda:self.display(3))
        Toolbar.addAction(p4_action)
        

        self.setCentralWidget(self.Stack)

        self.setGeometry(30, 40, 400, 400)
        self.setWindowTitle('bro ahh')
        self.show()

    def display(self,i):
        self.Stack.setCurrentIndex(i)
        

class page1(QWidget):
    def __init__(self):
        super().__init__()

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

        self.submit_button = QPushButton("input credentials")
        self.submit_button.clicked.connect(self.user_check)
        self.grid.addWidget(self.submit_button)

        self.submit_label = QLabel()
        self.grid.addWidget(self.submit_label, 6,0)

        self.setLayout(self.grid)

    def user_check(self):
            name = self.name_input.text()
            password = self.password_input.text()
            user_pass = name+password
            if user_pass == "bobblob":
                self.submit_label.setText("YAY PASSWORD (or username) CORRECT")
            else:
                self.submit_label.setText("NOOOO PASSWORD (or username) INCORRECT :(((((")

class page2(QWidget):
     def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop)

        IMG_PATH = str(FILE_PATH/"man.jpg")
        print (IMG_PATH)


        self.pic = QLabel(self)
        pixmap = QPixmap(IMG_PATH)
        pixmap = pixmap.scaled(720, 480)
        self.pic.setPixmap(pixmap)

        self.grid.addWidget(self.pic, 0,0)
        self.setLayout(self.grid)

class page3(QWidget):
    def __init__(self):
        super().__init__()
                
        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(self.updateSpinner)
        self.dial.setNotchTarget(10)
        self.grid.addWidget(self.dial)

        self.message = QLabel()
        self.grid.addWidget(self.message)

        self.setLayout(self.grid)

    def updateSpinner(self):

        self.dial_value = self.dial.value()
        print(self.dial_value)
        if self.dial_value == 86:
            self.message.setText("86 is restaurant slang for out of by the way")
        else: 
            self.message.setText("")

class page4(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["cheese","cheese DLC","sams chewing gum","spinny ball thing"])
        self.grid.addWidget((self.combo_box))

        self.combo_box.currentIndexChanged.connect(self.show_image)

        self.setLayout(self.grid)

    def show_image(self):
        print(self.combo_box.currentText())

app = QApplication(sys.argv)
ex = bro_app()
sys.exit(app.exec())