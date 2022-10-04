
# AAACoder Art-190
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
    t.forward((155/100)*len)
    t.seth(set_ang+100)
    t.forward(len)
    t.circle(-(60/100)*len,180)
    t.seth(set_ang-130)
    t.forward((155/100)*len)

for i in range(150):
    c = colorsys.hsv_to_rgb(h,.8,1)
    t.pencolor(c)
    t.fillcolor(c)
    t.begin_fill()
    heart((i*120)-20,-i+200)   
    t.end_fill()
    h += 0.01

tu.done()