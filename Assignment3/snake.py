number=int(input('enter number:'))
list=['*'for i in range(number)]
for i in range(1,number):
    if list[i-1]=='*':
        list[i]='#'
str=''
print(str.join(list))