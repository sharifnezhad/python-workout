def  Chess_pitch (a,b):
    for i in range(a):
        for j in range(b):
            if i%2==0:
                if j%2==0:
                    print('#',end='')
                else:
                    print('*',end='')
            else:
                if j%2==0:
                        print('*',end='')
                else:
                    print('#',end='')
    print(end='\n')


n=int(input('enter n:'))
m=int(input('enter m:'))
Chess_pitch(n,m)