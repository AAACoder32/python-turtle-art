

import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Pen()
t.speed(12)

h = 0
n = 36
t.penup()
t.goto(550,0)
t.pendown()

t.penup()
t.left(119)
t.forward(350)
t.pendown()
    
k = 250

while(k!=0):
    c = colorsys.hsv_to_rgb(h,0.6,0.8)
    t.pencolor(c)
    t.fillcolor(c)
    t.left(49)
    t.pu()
    t.forward(k)
    t.pd()
    t.begin_fill()
    t.circle(k,50)
    t.end_fill()
    t.pu()
    t.forward(k)
    t.circle(k,90)
    t.pd()
        
    k -= 2
    h += 5/n

turtle.done()