def gcd (a,b):
    temp=0
    while True:
        if(b==0):
            break
        temp=a%b
        a=b
        b=temp

    return a

number1=int(input('enter the number1:'))
number2=int(input('enter the number2:'))
bmm=gcd(number1,number2)
kmm=0
kmm=(number1*number2)/bmm
print(kmm)


