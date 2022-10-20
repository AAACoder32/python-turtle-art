
# AAACoder Art-189
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")

t = tu.Turtle()
t.pensize(4)
t.speed(0)
h = 0.8

def heart(set_ang,len=100):
    t.seth(set_ang)
    t.forward(len)
    t.circle((60/100)*len,180)
    t.seth(set_ang-130)
    t.penup()
    t.forward((155/100)*len)
    t.pendown()
    t.seth(set_ang+100)
    t.forward(len)
    t.circle(-(60/100)*len,180)
    t.seth(set_ang-130)
    t.penup()
    t.forward((155/100)*len)
    t.pendown()

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def circ(r):
    go(0,-250+r)
    t.circle(270-r)

r = 0
for i in range(50):
    c = colorsys.hsv_to_rgb(h,.8,1)
    t.pencolor(c)
    t.fillcolor(c)
    if i==49:
        t.fillcolor("black")
    t.begin_fill()
    r = 2*i+30
    circ(r)
    t.end_fill()
    h += 0.01
    
h = 0.9

go(0,145-r)
    
for i in range(40):
    c = colorsys.hsv_to_rgb(h,.8,1)
    t.pencolor(c)
    t.fillcolor(c)
    t.begin_fill()
    heart((i*120)-20,-2*i+75)   
    t.end_fill()
    h += 0.01

tu.done()