

import turtle

turtle.Screen().bgcolor("white")

t = turtle.Turtle()
t.pensize(9)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
go(0,-60)
t.seth(50)

t.fillcolor("red")

# Main container
t.begin_fill()

t.forward(350)
t.seth(130)
t.forward(100)
t.seth(180)
t.forward(320)
t.seth(220)
t.forward(100)
t.seth(310)
t.forward(365)

t.end_fill()

# First part
go(0,-15)

t.fillcolor("yellow")
t.begin_fill()
t.seth(50)
t.forward(60)
t.seth(200)
t.circle(-120,37)
t.seth(310)
t.forward(53)
t.end_fill()

# Second part 
go(-110,120)

t.begin_fill()

t.forward(70)
t.seth(50)
t.circle(-40,100)
t.seth(3)
t.forward(70)
t.circle(20,160)
t.circle(390,26)

t.end_fill()

# Third part

go(-195,215)

t.seth(310)

t.begin_fill()

t.forward(30)
t.seth(67)
t.circle(-120,45)
t.seth(180)
t.forward(40)
t.seth(220)
t.forward(60)

t.end_fill()

# Fourth part

go(0,180)
t.seth(-1)

t.begin_fill()

t.forward(50)
t.circle(-90,60)
t.seth(50)
t.forward(90)
t.seth(130)
t.forward(50)
t.seth(-90)
t.forward(35)
t.seth(180)
t.forward(80)
t.seth(90)
t.circle(50,70)
t.circle(120,45)
t.circle(35,160)
t.circle(-90,20)

t.end_fill()

# Fifth part
go(80,260)
t.seth(-35)

t.begin_fill()

t.circle(-60,30)
t.seth(30)
t.circle(20,80)
t.seth(180)
t.forward(30)

t.end_fill()

t.hideturtle()

turtle.done()