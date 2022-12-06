
# AAACoder Art-265
from turtle import *
import colorsys

bgcolor("black")
tracer(200)
h = 0

for i in range(300):
  c = colorsys.hsv_to_rgb(h,1,1)
  color(c)
  up()
  forward(i)
  left(95)
  backward(i)
  down()
  begin_fill()
  circle(i*0.1,180)
  end_fill()
  h += 1/17
  
done()