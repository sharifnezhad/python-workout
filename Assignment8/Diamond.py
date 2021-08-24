
n=int(input('n: '))

for i in range(n):
  print(' '*(n-i),'*'*(((i+1)*2)-1))
print(' '+((2*n)+1)*'*')
for i in range(n):
    print(' ' * (i+1), '*' * (2*n-(((i+1)*2)-1)))
