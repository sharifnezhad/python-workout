
n=int(input('enter the number:'))
if n==1:
    print('Fibonacci series:',0)    
elif n<=0:
    print('adad vared shode dorost nist ://')
else:
    list=[ []for i in range(0,n) ]
    print('Fibonacci series:',end='')
    for i in range(n):
        if i==0 or i==1:
            list[i]=1
        else:
            list[i]=list[i-1]+list[i-2]

    print(list)


    