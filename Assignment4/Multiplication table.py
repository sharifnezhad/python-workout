def multiplication(a,b):
    for i in range(1,a+1):
        for j in range(1,b+1):
            print(i*j , end=' - ')
        print(end='\n')


n=int(input())
m=int(input())
multiplication(n,m)

