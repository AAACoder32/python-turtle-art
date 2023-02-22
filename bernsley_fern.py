
# Bernskey Fern
from turtle import *
import colorsys
from random import random

bgcolor("black")
tracer(5000)

x = 0
y = 0
h = 0

def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))

def next_point():
    nextX = 0
    nextY = 0 
    global x
    global y 
    r = random()    
    if r < 0.01: 
        nextY = 0.16 * y
        nextX = 0
    elif r < 0.85:
        nextX = 0.85 * x + 0.04 * y
        nextY = -0.04*x+0.85 *y+1.6
    elif r < 0.93:
        nextX = 0.2 * x -0.26 * y;
        nextY = 0.23 * x+0.22*y + 1.6
    else:
        nextX = -0.15 * x + 0.28 * y;
        nextY = 0.26*x+0.24*y + 0.44; 
    x = nextX;
    y = nextY;

def go(x,y):
    pu()
    goto(x,y)
    pd()
    
   
hideturtle()
    
for i in range(20000):
    c = colorsys.hsv_to_rgb(h,1,1)
    next_point()
    px = num_to_range(x,-1,1,-100,100)
    py = num_to_range(y,-1,1,-200,0)
    go(px-40,py-300)
    color(c)
    begin_fill()
    circle(0.1)
    end_fill()
    h += 0.003
    
done()