class time:
    time_list = []
    def __init__(self,h,m,s):
        self.hour=h
        self.minet=m
        self.secend=s
        if h and m and s:
            if self.minet>=60:
                self.hour+=1
                self.minet-=60
            elif self.secend>=60:
                self.minet+=1
                self.secend-=60

    def show(self):
        string=' : '
        print(self.hour,":",self.minet,":",self.secend)


    def sum_time(self,timeB):
        result=time(None,None,None)
        result.hour=self.hour+timeB.hour
        result.minet=self.minet+timeB.minet
        result.secend=self.secend+timeB.secend
        return result

    def subtract(self,timeB):
        result=time(None,None,None)
        result.hour=self.hour=timeB.hour
        result.minet=self.minet-timeB.minet
        result.secend=self.secend-timeB.secend
        return result

    def convert_time_to_secend(self,timeB):
        print('convert time A or time B')
        number_menu=input('number menu::')
        result=time(None,None,None)
        if number_menu=='A' or number_menu=='a':
            result.hour=self.hour*3600
            result.minet=self.minet*60
            result.secend=result.hour+result.minet+self.secend
            return result.secend
        else:
            result.hour = timeB.hour * 3600
            result.minet = timeB.minet * 60
            result.secend = result.hour + result.minet+timeB.secend
            return result.secend


    def convert_secend_to_time(self):
        result=time(None,None,None)
        h=divmod(self.secend, 3600)
        m=divmod(h[1], 60)
        result.hour=h[0]
        result.minet=m[0]
        result.secend=m[1]
        return result



while True:
    print('1.sum (+)\n2.suntract (-)\n3.convert time to the secend\n4.convert secend to the time\n5.exit')
    number_menu=int(input('number menu:: '))
    if number_menu==5:
        exit()
    elif number_menu!=4:
        time_input = input('time: ').split(':')
        time1=time(int(time_input[0]),int(time_input[1]),int(time_input[2]))
        time_input = input('time: ').split(':')
        time2=time(int(time_input[0]),int(time_input[1]),int(time_input[2]))

        if number_menu==1:
            general_answer=time1.sum_time(time2)
            general_answer.show()
        elif number_menu==2:
            general_answer=time1.subtract(time2)
        elif number_menu==3:
            general_answer=time1.convert_time_to_secend(time2)
            print(general_answer)
    else:
        secend_input=int(input('secend: '))
        secend=time(None,None,secend_input)
        general_answer=secend.convert_secend_to_time()
        print(general_answer.show())
