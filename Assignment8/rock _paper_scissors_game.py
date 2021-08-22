import random
score_user=score_computer=0
list=['Rock','paper','scissors']
while True:
    computer_user=random.choice(list)
    print(' 1. Rock\n 2.paper \n 3.scissors')
    user=int(input('number:'))
    if list[user-1]==computer_user:
        print('mosaviiii')
    elif list[user-1]=='Rock' and computer_user=='paper' or list[user-1]=='paper' and computer_user=='scissors' or list[user-1]=='scissors' and computer_user=='Rock':
        print('user barabde')
        score_user+=1
    else :
        score_computer += 1
        print('computer barde')

    print('computer: ',computer_user,'Score: ', score_computer, score_user)
    if score_user==3 or score_computer==3:
        break
