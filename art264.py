
# AAACoder Art-264
from turtle import *
import colorsys

bgcolor("black")
tracer(200)
h = 0

for i in range(300):
  c = colorsys.hsv_to_rgb(h,1,1)
  color(c)
  forward(i)
  left(59)
  backward(i)
  begin_fill()
  circle(i*0.1)
  end_fill()
  h += 1/6

done()