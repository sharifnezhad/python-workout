secend= int(input('enter the secend:'))
h=divmod(secend,3600)
m=divmod(h[1],60)
print(h[0],':',m[0],':',m[1])