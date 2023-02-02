
# AAACoder Art-289
from turtle import *
import colorsys

bgcolor("black")
tracer(400)
pensize(3)
goto(-50,200)

h = 0

for i in range(400):
    c = colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)
    begin_fill()
    circle(20)
    right(179)
    forward(200-i)
    circle(40,240)
    left(29)
    backward(200-i)
    end_fill()
    h += 1/4
done()
    