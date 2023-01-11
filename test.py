from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.first = ""
        self.action = ""
        self.second = ""

    def initUI(self):
        self.setGeometry(300, 300, 300, 475)
        self.setWindowTitle('Калькулятор')

        self.btn7 = QPushButton('7', self)
        self.btn7.resize(75, 75)
        self.btn7.move(0, 100)
        self.btn7.clicked.connect(self.bttn7)

        self.btn4 = QPushButton('4', self)
        self.btn4.resize(75, 75)
        self.btn4.move(0, 175)
        self.btn4.clicked.connect(self.bttn4)

        self.btn1 = QPushButton('1', self)
        self.btn1.resize(75, 75)
        self.btn1.move(0, 250)
        self.btn1.clicked.connect(self.bttn1)

        self.btnc = QPushButton('c', self)
        self.btnc.resize(75, 75)
        self.btnc.move(0, 325)
        self.btnc.clicked.connect(self.bttnc)

        self.btnt = QPushButton('.', self)
        self.btnt.resize(75, 75)
        self.btnt.move(0, 400)
        self.btnt.clicked.connect(self.bttnt)

        self.btn8 = QPushButton('8', self)
        self.btn8.resize(75, 75)
        self.btn8.move(75, 100)
        self.btn8.clicked.connect(self.bttn8)

        self.btn5 = QPushButton('5', self)
        self.btn5.resize(75, 75)
        self.btn5.move(75, 175)
        self.btn5.clicked.connect(self.bttn5)

        self.btn2 = QPushButton('2', self)
        self.btn2.resize(75, 75)
        self.btn2.move(75, 250)
        self.btn2.clicked.connect(self.bttn2)

        self.btn0 = QPushButton('0', self)
        self.btn0.resize(75, 75)
        self.btn0.move(75, 325)
        self.btn0.clicked.connect(self.bttn0)

        self.btnpm = QPushButton('±', self)
        self.btnpm.resize(75, 75)
        self.btnpm.move(75, 400)
        self.btnpm.clicked.connect(self.bttnpm)

        self.btn9 = QPushButton('9', self)
        self.btn9.resize(75, 75)
        self.btn9.move(150, 100)
        self.btn9.clicked.connect(self.bttn9)

        self.btn6 = QPushButton('6', self)
        self.btn6.resize(75, 75)
        self.btn6.move(150, 175)
        self.btn6.clicked.connect(self.bttn6)

        self.btn3 = QPushButton('3', self)
        self.btn3.resize(75, 75)
        self.btn3.move(150, 250)
        self.btn3.clicked.connect(self.bttn3)

        self.btnce = QPushButton('ce', self)
        self.btnce.resize(75, 75)
        self.btnce.move(150, 325)
        self.btnce.clicked.connect(self.bttnce)

        self.btnra = QPushButton('=', self)
        self.btnra.resize(150, 75)
        self.btnra.move(150, 400)
        self.btnra.clicked.connect(self.bttnra)

        self.btnd = QPushButton('/', self)
        self.btnd.resize(75, 75)
        self.btnd.move(225, 100)
        self.btnd.clicked.connect(self.bttnd)

        self.btnu = QPushButton('*', self)
        self.btnu.resize(75, 75)
        self.btnu.move(225, 175)
        self.btnu.clicked.connect(self.bttnu)

        self.btnm = QPushButton('-', self)
        self.btnm.resize(75, 75)
        self.btnm.move(225, 250)
        self.btnm.clicked.connect(self.bttnm)

        self.btnp = QPushButton('+', self)
        self.btnp.resize(75, 75)
        self.btnp.move(225, 325)
        self.btnp.clicked.connect(self.bttnp)

        self.label1 = QLabel(self)
        self.label1.setText('                                                                  ')
        self.label1.move(15, 30)

        self.label2 = QLabel(self)
        self.label2.setText('                                                                  ')
        self.label2.move(15, 50)

    def bttn7(self):
        self.second = self.second + '7'
        self.label2.setText(self.second)

    def bttn4(self):
        self.second = self.second + '4'
        self.label2.setText(self.second)

    def bttn1(self):
        self.second = self.second + '1'
        self.label2.setText(self.second)

    def bttnc(self):
        self.first = ""
        self.action = ""
        self.second = ""
        self.label1.setText("")
        self.label2.setText("")

    def bttnt(self):
        self.second = self.second + '.'
        self.label2.setText(self.second)

    def bttn8(self):
        self.second = self.second + '8'
        self.label2.setText(self.second)

    def bttn5(self):
        self.second = self.second + '5'
        self.label2.setText(self.second)

    def bttn2(self):
        self.second = self.second + '2'
        self.label2.setText(self.second)

    def bttn0(self):
        self.second = self.second + '0'
        self.label2.setText(self.second)

    def bttnpm(self):
        if self.second:
            pm = int(self.second) * -1
            self.second = str(eval(f"{self.second} * -1"))
            self.label2.setText(self.second)

    def bttn9(self):
        self.second = self.second + '9'
        self.label2.setText(self.second)

    def bttn6(self):
        self.second = self.second + '6'
        self.label2.setText(self.second)

    def bttn3(self):
        self.second = self.second + '3'
        self.label2.setText(self.second)

    def bttnce(self):
        self.first = ""
        self.action = ""
        self.second = ""
        self.label1.setText("")
        self.label2.setText("")

    def bttnra(self):
        if self.action == "/" and self.second == "0":
            self.second = ""
            self.action = ""
            self.first = ""
            self.label1.setText("")
            self.label2.setText("")
        elif not self.second and not self.action and not self.first:
            pass
        elif not self.second:
            self.second = ""
            self.action = ""
            self.first = ""
            self.label1.setText("")
            self.label2.setText("")
        else:
            self.second = str(eval(f"{self.first} {self.action} {self.second}"))
            self.action = ""
            self.first = ""
            self.label1.setText("")
            self.label2.setText(self.second)

    def bttnd(self):
        self.action = "/"
        self.first = self.second
        self.second = ""
        self.label1.setText(self.first + self.action)
        self.label2.setText(self.second)

    def bttnu(self):
        self.action = "*"
        self.first = self.second
        self.second = ""
        self.label1.setText(self.first + self.action)
        self.label2.setText(self.second)

    def bttnm(self):
        if self.second:
            self.action = "-"
            self.first = self.second
            self.second = ""
            self.label1.setText(self.first + self.action)
            self.label2.setText(self.second)
        else:
            self.second = self.second + '-'
            self.label2.setText(self.second)

    def bttnp(self):
        self.action = "+"
        self.first = self.second
        self.second = ""
        self.label1.setText(self.first + self.action)
        self.label2.setText(self.second)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())