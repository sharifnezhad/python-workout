import os
name=input('enter your name:')
family=input('enter your family:')
print('Enter the grade 3 of your lesson:')
a=float(input('score1:'))
num1=int(input('Number of units of the first lesson:'))
b=float(input('score2:'))
num2=int(input('Number of units of the second lesson:'))
c=float(input('score3:'))
num3=int(input('Number of units of the third lesson:'))

avg= ((a*num1)+(b*num2)+(c*num3))/(num1+num2+num3)
print('avg: ',avg)
os.system('cls||clear')
if avg>=17:
    print('great')
elif avg>=12 and avg<17:
    print('normal')
elif avg<12:
    print('fail')