
# AAACoder Art-268
from turtle import *
import colorsys

bgcolor("black")
tracer(150)
h = 0.8

goto(-200,-270)
for i in range(170):
  c = colorsys.hsv_to_rgb(h,1,1)
  color(c)
  begin_fill()
  circle(280-2*i,100)
  seth(180+(120*i))
  circle(280-2*i,100)
  seth(30+(119*i))
  end_fill()
  h += 0.005
  
done()