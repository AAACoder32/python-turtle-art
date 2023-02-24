
# AAACoder Art-302
from turtle import *
import colorsys

bgcolor("black")
tracer(5)
pensize(3)
h = 0

def aaa(ang):
    seth(ang)
    forward(70)
    circle(50,120)
    seth(90+ang)
    circle(50,-150)
    seth(-167+ang)
    forward(50)
    
goto(-160,-100)
    
for i in range(30):
    c = colorsys.hsv_to_rgb(h,1,1)
    fillcolor(c)
    begin_fill()
    aaa(180+i*12)
    circle(20)
    left(60)
    forward(10)
    end_fill()
    h += 1/30

done()
