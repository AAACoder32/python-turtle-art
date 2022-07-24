

import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Turtle()
t.speed(0)

t.pencolor("white")
t.pensize(8)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

go(0,-150)
t.fillcolor("red")
t.begin_fill()
t.circle(220)
t.end_fill()

t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
go(-100,-50)
t.seth(-90)
t.forward(30)
t.circle(30,89)
t.forward(90)
t.circle(90,170)
t.seth(9)
t.circle(90,170)
t.forward(90)
t.circle(30,90)
t.forward(270)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
go(-60,-40)
t.forward(10)
t.circle(30,90)
t.forward(40)
t.circle(60,180)
t.forward(40)
t.circle(30,90)
t.forward(50)
t.end_fill()

go(-60,135)
t.begin_fill()
t.forward(10)
t.circle(30,90)
t.forward(40)
t.circle(60,180)
t.forward(40)
t.circle(30,90)
t.forward(45)
t.end_fill()

t.hideturtle()

turtle.done()