from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
import math

class Helloworld(QMainWindow):
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.ui=loader.load('pj-ui.ui',None)
        self.ui.show()
        self.ui.btn_sum.clicked.connect(self.sum_btn)
        self.ui.btn_minus.clicked.connect(self.minus)
        self.ui.cls.clicked.connect(self.cls)
        self.ui.btn_multiplication.clicked.connect(self.multiplication)
        self.ui.btn_division.clicked.connect(self.division)
        self.ui.btn_mn.clicked.connect(self.bt_mn)
        self.ui.btn_decimal.clicked.connect(self.decimal)
        self.ui.btn_result.clicked.connect(self.result)
        self.number=[None for x in range(10)]

        self.number[0]=self.ui.number1
        self.number[1]=self.ui.number2
        self.number[2]=self.ui.number3
        self.number[3]=self.ui.number4
        self.number[4]=self.ui.number5
        self.number[5]=self.ui.number6
        self.number[6]=self.ui.number7
        self.number[7]=self.ui.number8
        self.number[8]=self.ui.number9
        self.number[9]=self.ui.number0
        for i in range(10):
            self.number[i].clicked.connect(self.display_nuber)
            
        self.angle_list=[self.ui.btn_sin,self.ui.btn_cos,self.ui.btn_tan,self.ui.btn_cot]
        
        for i in range(len(self.angle_list)):
            self.angle_list[i].clicked.connect(self.angle)
            
        self.ui.btn_log.clicked.connect(self.logaritm)
        self.ui.btn_sqrt.clicked.connect(lambda :self.ui.textbox.setText(str(math.sqrt(int(self.ui.textbox.text())))))
        self.ui.btn_percent.clicked.connect(self.percent)
        self.number=0
        self.operator=''
        self.bool=False
    def display_nuber(self):
        if self.bool!=True:
            new=self.ui.textbox.text()+f'{self.sender().text()}'
        else:
            self.ui.textbox.setText('')
            new = f'{self.sender().text()}'
        self.ui.textbox.setText(new)

        self.bool=False
    def sum_btn(self):
        self.number=float(self.ui.textbox.text())
        self.operator='+'
        self.ui.textbox.setText('')
    def minus(self):
        self.number = float(self.ui.textbox.text())
        self.operator = '-'
        self.ui.textbox.setText('')
    def multiplication(self):
        self.number = float(self.ui.textbox.text())
        self.operator = '*'
        self.ui.textbox.setText('')
    def division(self):
        self.number = float(self.ui.textbox.text())
        self.operator = '/'
        self.ui.textbox.setText('')
    def bt_mn(self):
        self.number = float(self.ui.textbox.text())
        if self.number>0:
            self.number-=self.number*2
        else:self.number+=self.number*2
        self.ui.textbox.setText(str(self.number))
    def decimal(self):
        if '.' not in self.ui.textbox.text():
            new=self.ui.textbox.text()+'.'
            self.ui.textbox.setText(new)
    def angle(self):
        self.ui.textbox.setText(str(math.sin(math.radians(float(self.ui.textbox.text())))))
    def logaritm(self):
        number=float(self.ui.textbox.text())
        self.ui.textbox.setText(str(math.log2(number)))
    def percent(self):
        number=int(self.ui.textbox.text())/100
        self.ui.textbox.setText(str(number))
    def result(self):
        if self.operator=='+':
            self.ui.textbox.setText(str(self.number+float(self.ui.textbox.text())))
        elif self.operator=='-':
            self.ui.textbox.setText(str(self.number - float(self.ui.textbox.text())))
        elif self.operator=='*':
            self.ui.textbox.setText(str(self.number * float(self.ui.textbox.text())))
        elif self.operator=='/':
            self.ui.textbox.setText(str(self.number / float(self.ui.textbox.text())))
        self.bool=True

    def cls(self):
        self.number = 0
        self.ui.textbox.setText('')





app=QApplication([])
window=Helloworld()
app.exec()
