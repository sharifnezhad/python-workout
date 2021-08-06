array=[]
message=True
number=int(input('Array length:'))
for i in range(number):
    member=input('enter the number:')
    array.append(member)
for i in range(len(array)):
    if i==0:
        min=array[i]
    elif min>array[i]:
        message=False
        break
print (message)