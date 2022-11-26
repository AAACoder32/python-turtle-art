
# AAACoder Art-251
from turtle import *
import colorsys

bgcolor("black")
tracer(60)
speed(0)
h = 0.6

goto(-200,0)

for i in range(250):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    begin_fill()
    forward(250-i)
    left(60)
    forward(250-i)
    circle(10,160)
    end_fill()
    h += 0.005
    
done()