
# AAACoder Art-239b
from turtle import *
import colorsys

bgcolor("black")
tracer(6)
h = 0

for i in range(280):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    begin_fill()
    left(19)
    forward(i*0.7)
    right(60)
    forward(i*0.3)
    left(30)
    backward(i)
    end_fill()
    h += 0.008

done()