
# AAACoder Art-282
from turtle import *
import colorsys

bgcolor("black")
tracer(200)
pensize(3)
h = 0
goto(-110,200)

for i in range(400):
  c = colorsys.hsv_to_rgb(h,1,1)
  fillcolor(c)
  begin_fill()
  left(119)
  circle(50,180)
  circle(-50,180)
  circle(20)
  backward(350-i)
  end_fill()
  h += 0.005
done()