def sum_time():
    list_time = []
    list_time.append(input('time1: ').split(':'))
    list_time.append(input('time2: ').split(':'))
    for i in range(len(list_time)):
        for j in range(len(list_time[i])):
            list_time[i][j]= int(list_time[i][j])
    for i in range(len(list_time)):
        for j in range(len(list_time[i])):
            if list_time[i][j]>=60:
                list_time[i][j]-=60
                list_time[i][j-1]+=1
    sum=[]
    for i in range(len(list_time)-1):
        for j in range(len(list_time[i])):
            sum.append(list_time[i][j]+list_time[i+1][j])
            if sum[j]>=60:
                sum[j]-=60
                sum[j-1]+=1
    return sum
def miuns_time():
    list_time = []
    list_time.append(input('time1: ').split(':'))
    list_time.append(input('time2: ').split(':'))
    for i in range(len(list_time)):
        for j in range(len(list_time[i])):
            list_time[i][j] = int(list_time[i][j])
    for i in range(len(list_time)):
        for j in range(len(list_time[i])):
            if list_time[i][j] < 0:
                list_time[i][j] += 60
                list_time[i][j - 1] -= 1
    miuns = []
    for i in range(len(list_time) - 1):
        for j in range(len(list_time[i])):
            miuns.append(list_time[i][j] - list_time[i + 1][j])
            if miuns[j] < 0:
                miuns[j] += 60
                miuns[j - 1] -= 1
    return miuns
def convert_time_to_secend():
    time = input('enter the time:').split(':')
    result = (int(time[0]) * 3600) + (int(time[1] * 60)) + int(time[2])
    print(result)
def convert_secend_to_time():
    secend = int(input('enter the secend:'))
    day = divmod(secend, 86400)
    h = divmod(day[1], 3600)
    m = divmod(h[1], 60)
    print(day[0], ':', h[0], ':', m[0], ':', m[1])

print('1. sum \n2. miuns \n3. convert secent to the time\n4. convert time to secend')
number_menu=int(input('number:: '))
if number_menu==1:
    print('sum', sum_time())
elif number_menu==2:
    print('miuns:', miuns_time())
elif number_menu==3:
    convert_secend_to_time()
elif number_menu==4:
    convert_time_to_secend()

