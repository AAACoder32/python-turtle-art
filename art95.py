
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
    t.left(100)
    t.circle(i,90)
    t.right(60)
    t.circle(i,90)
    h += 0.015
    
turtle.done()