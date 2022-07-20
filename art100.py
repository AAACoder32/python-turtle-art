
import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Pen()
t.speed(0)
h = 0

for i in range(400):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    t.left(59)
    t.circle(i*0.4,-90)
    t.circle(-i*0.4,60)
    t.circle(i,-90)
    h += 0.005
    
turtle.done()