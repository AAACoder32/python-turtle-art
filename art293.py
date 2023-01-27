
# AAACoder Art-293
from turtle import *
import colorsys

bgcolor("black")
tracer(100)
pensize(3)
h = 0

for i in range(500):
  c = colorsys.hsv_to_rgb(h,1,1)
  pencolor(c)
  begin_fill()
  left(80)
  forward(i)
  right(5)
  circle(5)
  circle(50,120)
  circle(10)
  end_fill()
  h += 0.005
done()