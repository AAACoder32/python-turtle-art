

import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Turtle()
t.speed(0)
h = 0

for i in range(400):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    
    t.left(179)
    t.circle(i*0.2,-180)
    t.circle(-i*0.5,180)
    
    h+= 0.005
    
turtle.done()