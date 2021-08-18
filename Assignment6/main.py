import os
import time
from pyqrcode import QRCode
import pyqrcode
def switch():
    while True:
        os.system('cls')
        print('1-add product\n'
              '2-edit product \n'
              '3- search\n'
              '4-Qrcode\n'
              '5-remove product\n'
              '6-buy\n'
              '7-show list\n'
              '8-exit')
        argument = int(input(' enter a number: '))
        if argument==1:
           add_product(PRODUCTS)
        elif argument==2:
           edit_product()
        elif argument==3:
           search()
        elif argument==4:
           qrcode_id()
        elif argument==5:
           remove_product()
        elif argument==6:
            buy_shop()
        elif argument==7:
            show_list()
        elif argument==8:
            save_info()
def save_info():
    my_file=open('database.txt','w')
    for i in range(len(PRODUCTS)):
        if i!=len(PRODUCTS)-1:
            my_file.write(str(PRODUCTS[i]['id'])+','+PRODUCTS[i]['name']+','+str(PRODUCTS[i]['price'])+','+str(PRODUCTS[i]['count'])+'\n')
        else:
            my_file.write(str(PRODUCTS[i]['id'])+','+PRODUCTS[i]['name']+','+str(PRODUCTS[i]['price'])+','+str(PRODUCTS[i]['count']))
    exit()


    my_file.close()
def add_product(products):
    my_file=open('database.txt','a')
    
    while True:
        my_dict={}
        while True:
            id=int(input('id: '))
            found=False
            for i in PRODUCTS:
                if id== i['id']:
                    found=True
                    break

            if found==True:
                print('try again')
            else:
                my_dict['id']=id
                break
        name=input('name: ')
        my_dict['name']=name
        price=int(input('price: '))
        my_dict['price'] = price
        count=int(input('count: '))
        my_dict['count'] = count
        products.append(my_dict)
        print('Do you want to import new goods? (y/n)')
        if input()=='n':
            break

    my_file.close()
def edit_product():
    found=False
    while True:
        number = -1
        id= int(input('id:'))
        for i in PRODUCTS:
            number += 1
            if id==i['id']:
                found=True
                break
        if found==False:
            print('id vojod nadarad')
        else: break
    print('1.name\n2.price\n3.count')
    if int(input())==1:
        PRODUCTS[number]['name']=input('name:')
    elif int(input())==2:
        PRODUCTS[number]['price'] = int('price:')
    elif int(input())==3:
        PRODUCTS[number]['count'] = input('count:')

def search():
    name=input('name: ')
    for i in PRODUCTS:
        if name==i['name']:
          return  print('Goods are available')

    return print('The product is not available')
def qrcode_id():
    id=int(input('id: '))

    # Generate QR code
    url = pyqrcode.create(id)

    # Create and save the svg file naming "myqr.svg"
    url.svg("myqr.svg", scale=8)

    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale=6)
def remove_product():
    id=int(input('id: '))
    for i in PRODUCTS:
        if id==i['id']:
            break

    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']==id:
            del PRODUCTS[i]
            break

    # file=open('database.txt','r')
    # lines=file.readlines()
    # file.close()
    # del lines[line_number-1]
    # new_file=open('database.txt','w')
    # for line in lines:
    #     new_file.write(line)
    # new_file.close()
def buy_shop():
    product_infor={}
    cart=[[]]
    value=sum=0
    while True:
        found = False
        id = int(input('id: '))
        for i in PRODUCTS:
            if id== i['id']:
                found=True
                product_infor=i
                break
        if found==True:
            print('Goods are available')

            while True:
                count=int(input('count: '))
                if count<=product_infor['count']:
                    product_infor['count']-=count
                    break
                else:
                    print('Inventory is not enough\n',
                    'Currently only', product_infor['count'] ,'of these products are available in stock')
            sum+=(product_infor['price']*count)
            cart[value].append(product_infor['id'])
            cart[value].append(product_infor['name'])
            cart[value].append(product_infor['price'])
            cart[value].append(count)
            cart[value].append(sum)
            value+=1
            print('Do you want to add another product? (y/n)')
            if input()=='n':
                for i in range(len(cart)):
                    for j in range(5):
                        print(cart[i][j],end='\t')
                    print()

                print('sum total: ',sum)
                for i in PRODUCTS:
                    if id==i['id']:
                        i['count']=product_infor['count']

                break
            else:
                cart.append([])
        else:
            print('The product is not available')
    time.sleep(4)
def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i]['id'], PRODUCTS[i]['name'], PRODUCTS[i]['price'], PRODUCTS[i]['count'], end='\n')


my_file =open('database.txt','r')
data= my_file.read()
my_file.close()
product_list=data.split('\n')
PRODUCTS=[]
for i in range(len(product_list)):
    product_info=product_list[i].split(',')
    mydict={}
    mydict['id']=int(product_info[0])
    mydict['name']=product_info[1]
    mydict['price']=int(product_info[2])
    mydict['count']=int(product_info[3])
    PRODUCTS.append(mydict)

switch()
