
import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Pen()
t.speed(0)
h = 0

for i in range(250):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    
    t.right(59)
    t.circle(i*0.6,180)
    t.left(60)
    t.circle(i,90)
    h += 0.004
    
turtle.done()