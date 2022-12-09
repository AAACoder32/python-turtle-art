
# AAACoder Art-267
from turtle import *
import colorsys

bgcolor("black")
tracer(80)
h = 0.4
pensize(4)

for i in range(300):
  c = colorsys.hsv_to_rgb(h,1,1)
  color(c)
  forward(i)
  right(119)
  forward(i)
  circle(i*0.1,180)
  left(60)
  backward(i)
  
  h += 1/3
  
done()