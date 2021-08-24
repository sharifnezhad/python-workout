def sum_complex(a,b):
    return a+b
def miuns_complex(a,b):
    return a-b
def multiply_complex(a, b):
    return a*b
while True:
    print('1.sum\n2.miuns\n3.multiply')
    number_menu = int(input('number :: '))
    if number_menu==-1:
        exit()
    number1=int(input('number1:'))
    fctitious1=int(input('Fictitious:'))
    number2=int(input('number2:'))
    fctitious2=int(input('Fictitious:'))
    complex_number1=complex(number1,fctitious1)
    complex_number2=complex(number2,fctitious2)
    if number_menu==1:
        print(sum_complex(complex_number1,complex_number2))
    elif number_menu==2:
        print(miuns_complex(complex_number1,complex_number2))
    elif number_menu==3:
        print(multiply_complex(complex_number1,complex_number2))