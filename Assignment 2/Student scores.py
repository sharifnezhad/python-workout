std_number=int(input('enter student number:'))
std_sco=[ []for i in range(0,std_number) ]
for i in range(len(std_sco)):
    std_sco[i]=float(input('enter score:'))
print(std_sco)
max=min=std_sco[0]
sum=0
for i in range(len(std_sco)):
    sum=sum+std_sco[i]
    if max<std_sco[i]:
        max=std_sco[i]
    elif min>std_sco[i]:
        min=std_sco[i]
avg=sum/std_number
print('max=', max,'min=', min,'avg=', avg)


