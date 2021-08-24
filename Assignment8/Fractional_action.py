def sum_frac(fractions):
    array=[0,'/' , 0]
    string = ' '
    if fractions[1]==fractions[3]:
        array[0]=str(fractions[0]+fractions[2])
        array[2]=str(fractions[1])
        return string.join(array)
    else:
        array[0]=str(fractions[0]*fractions[3]+fractions[1]*fractions[2])
        array[2]=str(fractions[1]*fractions[3])
        return string.join(array)
def multiplication(fractions):
    array = [0, '/', 0]
    string = ' '
    array[0]=str(fractions[0]*fractions[2])
    array[2]=str(fractions[1]*fractions[3])
    return string.join(array)

def minus_frac(fractions):
    array = [0, '/', 0]
    string = ' '
    if fractions[1] == fractions[3]:
        array[0] = str(fractions[0] - fractions[2])
        array[2] = str(fractions[1])
        return string.join(array)
    else:
        array[0] = str(fractions[0] * fractions[3] - fractions[1] * fractions[2])
        array[2] = str(fractions[1] * fractions[3])
        return string.join(array)
def division_frac(fractions):
     return (fractions[0]*fractions[3])/(fractions[1]*fractions[2])

while True:
    print('1.sum\n2.minus\n3.Multiplication\n4.Division')
    number_menu = int(input('number:: '))
    if number_menu==-1:
        exit()
    number1=int(input('number1:'))
    denominator=int(input('denominator1:'))
    number2=int(input('number2:'))
    denominator2=int(input('denominator2: '))
    Fractions=[number1,denominator,number2,denominator2 ]
    if denominator==0 or denominator2==0:
        print('error, anjam pazir nist')

    if number_menu==1:
       print('sum:', sum_frac(Fractions))
    elif number_menu==2:
        print('minus:',minus_frac(Fractions))
    elif number_menu==3:
        print('Multiplication: ',multiplication(Fractions))
    elif number_menu==4:
        print('Division:', division_frac(Fractions))
