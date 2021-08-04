import random

words=['ali','rain','loremipsum','umbrmella','icecream','tosols']
esc='exit'
while esc!='exit':
    chooseTheWord=random.choice(words)
    selectedWord=[ '-' for i in range(len(chooseTheWord)) ]
    str=''
    print(str.join(selectedWord))
    joon=6
    while joon>0:
        user_letter=input('enter a letter: ')
        if user_letter.lower() in chooseTheWord:
            num=0
            for i in chooseTheWord:
                if user_letter==i:
                    selectedWord[num]=user_letter.lower()
                num+=1

            
            print(str.join(selectedWord))
            if str.join(selectedWord)==chooseTheWord: 
                break
        else:
            joon-=1
            print('false and joon=' , joon)
        
    if joon==0:
        print('game over')
    else:
        print('good job')
    esc=input('play again or exit (again/exit):')

