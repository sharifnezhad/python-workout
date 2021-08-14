import turtle
# colors=['red','purple','blue','green','yellow','orange']
θ=[120, 90, 72, 60, 51.40, 45, 40]
t= turtle.Pen()
t.speed()
turtle.bgcolor('black')
i=0
length=30
sides=3
w=-5

while i<7:
    for j in range(sides):
        t.width(i/100+1)
        t.pencolor('red')
        t.forward(length)
        t.left(θ[i])
    t.penup()
    t.goto(w, 3*w)
    t.pendown()
    i+=1
    length+=20
    sides+=1
    w-=5