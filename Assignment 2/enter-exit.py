array=[]
i=0
while True:
    num=input('enternumber:')
    array.append(num)
    if array[i]=='exit':
       break
    i+=1

x=0
resalt=0
while x<len(array):
    resalt=int(array[x])+resalt
    x+=1

print(resalt)
