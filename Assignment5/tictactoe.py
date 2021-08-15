import random
import os
from termcolor import colored, cprint
import time


def one_player(variable,variable_com):
    while True:
        while True:
            x=int(input('X: '))
            y=int(input('Y: '))
            if x<=3 or y<=3 :
                if tictactoe[x][y]=='_':
                    tictactoe[x][y]=colored(variable,'green')
                    show_game()
                    winner(variable)
                    break;
                else:
                    print('jauegah por ast')
            else:
                print('adad vared shode nadorost ast')
        while True:
            x=random.randint(0,2)
            y=random.randint(0,2)
            if tictactoe[x][y]=='_':
                tictactoe[x][y]=colored(variable_com,'red')
                show_game()
                winner(variable_com)
                break;

def two_player(variable,variable_two):
    while True:
        while True:
            print('player 1:')
            x=int(input('X: '))
            y=int(input('Y: '))
            if x<=3 or y<=3 :
                if tictactoe[x][y]=='_':
                    tictactoe[x][y]=colored(variable,'green')
                    show_game()
                    winner(variable)
                    break
                else:
                    print('jauegah por ast')
            else:
                print('adad vared shode nadorost ast')
        while True:
            print('player 2:')
            x=int(input('X: '))
            y=int(input('Y: '))
            if tictactoe[x][y]=='_':
                tictactoe[x][y]=colored(variable_two,'green')
                show_game()
                winner(variable_two)
                break
            else:
                print('jauegah por ast')

def show_game():
    os.system('cls')
    for i in range(len(tictactoe)):
        for j in range(len(tictactoe)):
            print(tictactoe[i][j],end='\t')
        print()
   
def winner(var):
    num=0
    #Line search
    for i in range(len(tictactoe)):
        for k in range(3):
            if var in tictactoe[i][k]:
                num+=1

        if num==3:
            print(var, 'barande')
            print('{time.time() - start}')
            exit()
        else:
            num=0

    #Vertical search
    for j in range(len(tictactoe)):
        for k in range(3):
            if var in tictactoe[k][j]:
                num+=1
        if num==3:
            print(var, 'barande')
            print(f'{time.time() - start_time} s')
            exit()
        else:
            num=0
    #Search the main column
    for i in range(len(tictactoe)):
        if var in tictactoe[i][i]:
            num+=1

    if num==3:
        print(var, 'barande')
        print(f'{time.time() - start_time} s')
        exit()
    else:
        num=0
    #The main pillar of the last
    for i in range(len(tictactoe),0):
        if var in tictactoe[i][i]:
            num+=1

    if num==3:
        print(var, 'barande')
        print(f'{time.time() - start_time} s')
        exit();
    else:
        num=0
    #Check that the matrix is full
    equal=0
    for i in range(len(tictactoe)):
        for j in range(len(tictactoe)):
            if tictactoe[i][j]!='_':
                equal+=1
    if equal==9:
        print('The game equalised')
        print(f'{time.time() - start_time} s')
        exit()
           

tictactoe=[['_' for j in range(3)] for i in range(3)]
variable='X'
variable_two='O'
variable_com='O'
start_time= time.time()
print('menu:\n 1.onplayer\n 2.two player')
multiplayer=int(input('Enter a number:'))
if multiplayer==1:
    print('X or O')
    if input()=='o':
        variable='O'
        variable_com='X'
    one_player(variable,variable_com)
else:
    print('X or O')
    if input()=='o':
        variable='O'
        variable_two='X'
    two_player(variable,variable_two)



        
