
# AAACoder Art-253
from turtle import *
import colorsys

bgcolor("black")
tracer(40)
speed(0)
h = 0

goto(-209,0)

for i in range(250):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    begin_fill()
    forward(250-i)
    left(50)
    forward(250)
    circle(10,160)
    end_fill()
    h += 0.008

done()