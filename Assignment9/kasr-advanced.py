class kasr:
    def __init__(self,a,b):
        self.sorat=a
        self.makhrag=b
    def sum(self,fractional_two):
        result = kasr(None, None)
        if self.makhrag==fractional_two.makhrag:
            result.sorat = self.sorat + fractional_two.sorat
            result.makhrag=self.makhrag
        else:
            result.sorat=self.sorat*fractional_two.makhrag+self.makhrag*fractional_two.sorat
            result.makhrag=self.makhrag*fractional_two.makhrag
        return result
    def subtract(self,fractional_two):
        result = kasr(None, None)
        if self.makhrag == fractional_two.makhrag:
            result.sorat = self.sorat - fractional_two.sorat
            result.makhrag = self.makhrag
        else:
            result.sorat = self.sorat * fractional_two.makhrag - self.makhrag * fractional_two.sorat
            result.makhrag = self.makhrag * fractional_two.makhrag
        return result
    def multiply(self,fractional_two):
        result=kasr(None,None)
        result.sorat=self.sorat*fractional_two.sorat
        result.makhrag=self.makhrag*fractional_two.makhrag
        return result

    def divide(self, fractional_two):
        result = kasr(None, None)
        result.sorat = self.sorat * fractional_two.sorat
        result.makhrag = self.makhrag * fractional_two.makhrag
        # result=float(result.sorat/result.makhrag)
        return result
    def show(self):
        if self.sorat==self.makhrag:
            print(1)
        elif self.sorat==0:
            print(0)
        else:
            print(self.sorat,"/",self.makhrag)

while True:
    print('1. sum(+)\n2.subtract(-)\n3.multiply(*)\n4.divide(/)\n5.exit')
    number_menu=int(input('number menu:: '))
    if number_menu==5:
        exit()
    fractional_one=fractional_two=0
    i=0
    while True:
        if i==2:
            break
        number1=int(input('sorat: '))
        number2=int(input('makhrag: '))
        if number2==0:
            print('error')
            continue
        if number1==0 and number_menu==4 and i==1:
            print('chon makhrag 0 hast javab kasr dorost nist!! dobare add vared konid')
            continue
        if i==0:
            fractional_one = kasr(number1,number2)
        else:
            fractional_two = kasr(number1,number2)

        i+=1
    if number_menu==1:
       general_answer=fractional_one.sum(fractional_two)
       general_answer.show()
    elif number_menu==2:
        general_answer=fractional_one.subtract(fractional_two)
        general_answer.show()
    elif number_menu==3:
        general_answer=fractional_one.multiply(fractional_two)
        general_answer.show()
    elif number_menu==4:
        if fractional_one.sorat==0:
            print(0)
        general_answer=fractional_one.divide(fractional_two)
        general_answer.show()




