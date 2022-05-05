
import turtle

t = turtle.Pen()

turtle.bgcolor('black')
t.pencolor('red')
t.penup()
t.goto(0,-74)
t.pensize(8)
t.pendown()

t.fillcolor('red')

t.begin_fill()
for i in range(96):
    if (i==16 or i==32 or i==64 or i==80):
        t.circle(55,79)
    t.left(.45)
    t.fd(10)
t.end_fill()

t.pencolor('white')
t.fillcolor('white')
t.penup()
t.home()
t.goto(-32,0)
t.begin_fill()
t.pendown()
t.left(90)
t.fd(120)
t.right(120)
t.fd(120)
t.right(120)
t.fd(120)
t.end_fill()

turtle.done()