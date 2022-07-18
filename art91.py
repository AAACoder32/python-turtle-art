

import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Pen()
t.speed(11)
h = 0

for i in range(220):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    t.width(i//100+1)
    t.pencolor(c)
    t.circle(-i*0.6,-45)
    t.circle(-i*0.6,-90)
    t.circle(-i*0.6,-45)
    t.left(119)
    t.circle(-i*0.3,-30)
    t.circle(-i*0.3,-60)
    t.circle(-i*0.3,-30)
    h += 0.005
    
turtle.done()