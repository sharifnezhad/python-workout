from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from random import randint
from time import sleep
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.ui=loader.load('sodoco.ui')
        self.game=[[None for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                tb=QLineEdit()
                tb.setStyleSheet('font-size:20px')
                tb.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
                tb.setAlignment(QtCore.Qt.AlignCenter)
                self.game[i][j] = tb
                self.ui.grid_sodo.addWidget(tb, i, j)

        self.ui.show()
        self.ui.btn_newgame.clicked.connect(self.newGame)
        self.ui.btn_check.clicked.connect(self.check)
        self.ui.dark_mode.clicked.connect(self.dark_mode)
        for i in range(9):
            for j in range(9):
                self.game[i][j].returnPressed.connect(self.check)


    def newGame(self):
        for i in range(len(self.game)):
            for j in range(len(self.game)):
                self.game[i][j].setText('')
        r=randint(1,6)
        try:
            file_path=f'data/s{r}.txt'
            f=open(file_path,'r')

            big_text=f.read()

            rows=big_text.split('\n')

            for i in range(9):
                NUMBERS=rows[i].split(' ')
                for j in range(9):
                    if NUMBERS[j]!='0':
                        self.game[i][j].setStyleSheet('font-size:20px; color:#000')
                        self.game[i][j].setText(NUMBERS[j])
                        self.game[i][j].setReadOnly(True)
                    else:
                        self.game[i][j].setStyleSheet('font-size:20px; color:blue')
        except:
            self.ui.message.setText('error,file not to open')
            
    def dark_mode(self):
        if self.ui.dark_mode.text()=='Dark Mode':
            self.ui.setStyleSheet('background:#2d3436')
            self.ui.dark_mode.setStyleSheet('background:#fff')
            self.ui.btn_check.setStyleSheet('background:#fff')
            self.ui.btn_newgame.setStyleSheet('background:#fff')
            self.ui.dark_mode.setText('Lite Mode')
        else:
            self.ui.setStyleSheet('background:#fff')
            self.ui.dark_mode.setText('Dark Mode')

        # self.ui.btn_newgame.
    def check(self):
        num=0
        for i in range(9):
            for j in range(9):
                if self.game[i][j].text()!='':
                    num+=1
        if num>=81:
            self.ui.message.setText('you win.')
            
        #check rows
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text()==self.game[row][j].text() and i!=j and self.game[row][i].text() :
                        self.game[row][i].setStyleSheet('background:#ff7979;color:#fff')
        #check col
        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text()==self.game[j][col].text() and i!=j and self.game[i][col].text():
                        self.game[i][col].setStyleSheet('background:#ff7979;color:#fff')

        row=col=[0,0]
        for i in range(3):
            row=[i*3,i*3+3]
            for j in range(3):
                col = [j * 3, j * 3 + 3]
                matrix_ThreeinThree=[[] for m in range(3)]
                count = 0
                for k in range(row[0],row[1]):
                    for y in range(col[0],col[1]):
                        matrix_ThreeinThree[count].append(self.game[k][y].text())
                        # if self.game[k][y].text()!='':
                    count+=1



                list=self.check_matrix_ThreeinThree(matrix_ThreeinThree)
                if list!=[]:
                    print(list)
                    for p in range(0,len(list),2):
                        if row[0]>=0 and row[j]<=3:
                            if col[0]>=0 and col[1]<=3:
                                self.game[list[p]][list[p+1]].setStyleSheet('background:#ff7979;color:#fff')
                            elif col[0]>=3 and col[1]<=6:
                                self.game[list[p]][list[p+1]+3].setStyleSheet('background:#ff7979;color:#fff')
                            elif col[0] >= 6 and col[1] <=9:
                                self.game[list[p]][list[p + 1]+6].setStyleSheet('background:#ff7979;color:#fff')


                        elif row[0]>=3 and row[j]<=6:
                            if col[0]>=0 and col[1]<=3:
                                self.game[list[p] + 3][list[p + 1]].setStyleSheet('background:#ff7979;color:#fff')
                            elif col[0]>=3 and col[1]<=6:
                                self.game[list[p] + 3][list[p+1]+3].setStyleSheet('background:#ff7979;color:#fff')
                            elif col[0] >= 6 and col[1] <= 9:
                                self.game[list[p] + 3][list[p + 1]+6].setStyleSheet('background:#ff7979;color:#fff')

                        elif row[0] >= 6 and row[j] <=9:
                            if col[0] >= 0 and col[1] <= 3:
                                self.game[list[p] + 6][list[p + 1]].setStyleSheet('background:#ff7979;color:#fff')
                            elif col[0] >= 3 and col[1] <= 6:
                                self.game[list[p] + 6][list[p + 1] + 3].setStyleSheet('background:#ff7979;color:#fff')
                            elif col[0] >= 6 and col[1] <= 9:
                                self.game[list[p] + 6][list[p + 1] + 6].setStyleSheet('background:#ff7979;color:#fff')
    def check_matrix_ThreeinThree(self,all):
        number=0
        save_row_col_number=[]
        for i in range(3):
            for j in range(3):
                if all[i][j]:
                    number=int(all[i][j])
                else:
                    continue
                    # print(f'n={number}')
                for k in range(i,3):
                    for l in range(j,3):
                        if l==j and k==i:
                            continue
                        if all[k][l]!='' and number==int(all[k][l])  :
                            save_row_col_number.append(k)
                            save_row_col_number.append(l)
        return save_row_col_number


app=QApplication()
window=MainWindow()
app.exec()
