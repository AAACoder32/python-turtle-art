

import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Pen()
h = 0
t.speed(0)

for i in range(150):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,0.6,1)
    t.pencolor(c)
    t.right(90)
    t.forward(i)
    t.circle(i,-10)
    t.left(120)
    t.pu()
    t.forward(i)
    t.pd()
    t.circle(2*i,-90)
    h += 0.025
    
turtle.done()
