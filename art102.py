
import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Pen()
h = 0
t.speed(0)

for i in range(300):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    t.right(59)
    t.forward(30)
    t.circle(i*0.5,180)
    h += 0.005

turtle.done()