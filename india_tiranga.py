
from sketchpy import library as lib
import turtle

t = turtle.Turtle()
t.speed(2)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
go(-180,-380)
t.pencolor("orange")

t.write("Happy",font=("Arial",18,"bold"))

go(-300,-460)
t.pencolor("navy")
t.write("75th Independence",font=("Arial",18,"bold"))

go(-150,-530)
t.pencolor("green")

t.write("Day",font=("Arial",18,"bold"))

l = lib.flag()
go(-400,0)
l.draw()

turtle.done()
