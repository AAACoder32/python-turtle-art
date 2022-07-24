

import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Turtle()
t.speed(0)
h = 0


for i in range(300):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    
    t.circle(i,45)
    t.circle(-i,45)
    t.left(119)
    
    h += 0.005
    
turtle.done()