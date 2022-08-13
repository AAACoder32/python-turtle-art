# AAACoder Art

import turtle

turtle.Screen().bgcolor("#e8f0fc")

t = turtle.Turtle()
t.pensize(3)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

go(-280,-500)

# Long pole

t.begin_fill()
t.forward(30)
t.seth(90)
t.forward(900)
t.seth(40)
t.circle(30,120)
t.seth(110)
t.forward(20)
t.seth(-110)
t.forward(20)
t.seth(-160)
t.circle(30,120)
t.seth(-90)
t.forward(900)
t.end_fill()

# Orange Strip
go(-250,360)
t.pencolor("orange")
t.fillcolor("orange")
t.seth(30)
t.begin_fill()
t.circle(-180,60)
t.circle(160,60)
t.circle(-120,70)
t.circle(-120,70)
t.seth(140)
t.circle(120,80)
t.circle(-120,80)
t.circle(160,65)
t.seth(90)
t.circle(220,35)
t.end_fill()

# White Strip
go(263,212)
t.pencolor("white")
t.fillcolor("white")
t.seth(-115)
t.begin_fill()
t.circle(140,50)
t.seth(140)
t.circle(120,80)
t.circle(-120,80)
t.circle(160,65)
t.seth(76)
t.circle(230,30)
t.seth(25)
t.circle(-180,55)
t.circle(160,60)
t.circle(-130,72)
t.end_fill()

# Green strip
go(260,100)
t.pencolor("green")
t.fillcolor("green")
t.seth(-70)
t.begin_fill()
t.circle(-140,50)
t.seth(140)
t.circle(110,80)
t.circle(-120,80)
t.circle(160,80)
t.seth(58)
t.circle(230,35)
t.seth(20)
t.circle(-180,55)
t.circle(150,70)
t.circle(-130,65)
t.end_fill()

# Chakra
go(25,80)
t.pencolor("navy")
t.fillcolor("navy")
t.seth(0)
t.pensize(7)

t.circle(62)

go(17,199)
t.pensize(5)

for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()

go(25,145)
t.pensize(2)

for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15)

turtle.done()