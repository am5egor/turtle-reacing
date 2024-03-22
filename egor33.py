from turtle import *
from random import randint

Mike = Turtle()
Dobbi = Turtle()

Mike.shape('turtle')
Mike.color('black')

Dobbi.shape('turtle')
Dobbi.color('yellow')

Dobbi.penup()
Dobbi.goto(-225,90)

Mike.penup()
Mike.goto(150,200)
Mike.pendown()
Mike.right(90)

x = 150
for i in range(10):
    Mike.forward(400)
    Mike.penup()
    Mike.goto(x,200)
    Mike.pendown()

    x -= 40

Mike.color('red')
Mike.forward(400)

Mike.penup()
Mike.goto(190,200)
Mike.pendown()
Mike.color('green')
Mike.forward(400)

Mike.penup()
Mike.goto(-225,-60)
Mike.left(90)

while Mike.xcor() < 190 and Dobbi.xcor() < 190:
    Mike.forward(randint(1, 10))
    Dobbi.forward(randint (1, 10))

if Mike.xcor() > Dobbi.xcor():
    Mike.color('orange')
    Mike.goto(230,-60)
    Mike.pendown()
    Mike.begin_fill()
    Mike.circle(30)
    Mike.end_fill()

else:
    Dobbi.goto(210,90)
    for i in range(5):
        Dobbi.forward(30)
        left(145)



hideturtle()
exitonclick()
