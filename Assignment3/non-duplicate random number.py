import random
n=int(input())
list=[[] for i in range(n)]
for i in range(len(list)):
    r=random.randint(1,100)
    if r not in list:
        list[i]=r
print (list)
