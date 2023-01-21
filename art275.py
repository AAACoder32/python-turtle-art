
# AAACoder Art-275
from turtle import *
import colorsys

bgcolor("black")
tracer(200)
h = 0

for i in range(450):
  c = colorsys.hsv_to_rgb(h,1,1)
  color(c)
  begin_fill()
  forward(i)
  circle(10)
  right(3)
  backward(i*0.5)
  left(180)
  end_fill()
  h += 0.005
  
done()