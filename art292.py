
# AAACoder Art-292
from turtle import *
import colorsys

bgcolor("black")
tracer(600)
pensize(3)
h = 0

goto(100,0)

def des(ang,n):
  circle(60+n,30)
  left(ang)
  circle(60+n,60)

for i in range(550):
  c = colorsys.hsv_to_rgb(h,1,1)
  pencolor(c)
  begin_fill()
  des(120,400-i)
  end_fill()
  h += 1/12
done()