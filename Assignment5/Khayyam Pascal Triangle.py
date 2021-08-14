n=int(input())
kh= [[[] for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        kh[i][0]=1
        kh[i][i]=1
for i in range(2,n):
    for j in range(1,i):
        kh[i][j]=kh[i-1][j]+kh[i-1][j-1]

for i in range(n):
    for j in range(i+1):
        print(kh[i][j],end='\t')
    print()