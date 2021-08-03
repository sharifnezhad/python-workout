import math
i='y'
while i=='y':
    number_one=int(input('please enter number1:'))
    Operator=input('please enter Operator: (+|-|*|/|^|radical|sin|cos|tan|cot|factorial)')
    if Operator == '+' or Operator == '-' or Operator == '*' or Operator == '/' or Operator == '^' :
        number_two=int(input('please enter number2:'))
        if Operator=='+':
            result=number_one+number_two
        elif Operator=='-':
            result=number_one-number_two
        elif Operator=='*':
            result=number_one*number_two
        elif Operator=='/':
            if number_two==0:
                result='error'
            else:
                result=number_one/number_two
        elif Operator=='^':
            result=number_one**number_two
    else:
        if Operator=='radical':
            result=math.sqrt(number_one)
        elif Operator=='sin':
            result=math.sin(number_one)
        elif Operator=='cos':
            result=math.cos(number_one)
        elif Operator=='tan':
            result=math.tan(number_one)
        elif Operator=='cot':
            result=1/math.tan(number_one)
        elif Operator=='factorial':
            result=math.factorial(number_one)


    print('output: ',result)
    print ('\n Do you want to continue calculating? (y/n)')
    i=input()

