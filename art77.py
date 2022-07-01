

import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Pen()

c = [colorsys.hsv_to_rgb(h*0.14,1,0.8) for h in range(6)]


t.speed(0)

for i in range(150):
    t.width(i//100+1)
    t.pu()
    t.pencolor(c[i%3])
    t.forward(i*2)
    t.pd()
    t.circle(i,180)
    t.left(59)
    t.pu()
    t.forward(i*2)
    t.pd()
    t.circle(i*2,-120)
    

turtle.done()
