a=int (input('Enter a number:'))
b=int (input('Enter a number:'))
c=int (input('Enter a number:'))
if c<a+b:
    if b<a+c:
        if a<b+c:
            print('This triangle can be drawn :)')
        else:
            print('The triangle cannot be drawn ://')
    else:
        print('The triangle cannot be drawn ://')
else:
    print('The triangle cannot be drawn ://')

