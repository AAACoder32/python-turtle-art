
# AAACoder Art-262
from turtle import *
import colorsys

bgcolor("black")
tracer(80)
h = 0
goto(-300,0)

for i in range(300):
  c = colorsys.hsv_to_rgb(h,1,1)
  color(c)
  begin_fill()
  forward(300-i)
  left(19)
  backward(300-i)
  circle(30-i*0.1)
  end_fill()
  h += 0.07
done()
