
from turtle import *
from time import sleep

bgcolor("black")

t = [Turtle(),Turtle()]
x = 6

colors = ["red","yellow","blue","lime"]

for index,i in enumerate(t):
    i.speed(0)
    i.color("white")
    i.shape("circle")
    i.shapesize(0.3)
    i.width(3)
    i.penup()
    i.seth(90)
    i.forward(350)
    i.seth(-180)
    i.pendown()

delay(0)
speed(0)
hideturtle()

sleep(1)

for i in colors:
    color(i)
    for j in range(360):
        t[0].forward(x)
        t[0].left(1)
        penup()
        goto(t[0].pos())
        pendown()
        t[1].forward(x*2)
        t[1].left(2)
        goto(t[1].pos())

done()