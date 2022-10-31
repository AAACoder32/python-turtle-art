
# AAACoder Art-222
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0
t.pensize(3)

def design(len,ang=0):
    t.seth(ang)
    t.forward(len)
    t.circle(0.3*len,90)
    t.forward(len)
    t.seth(180+ang)
    t.forward(len)
    t.circle(0.3*len,90)
    t.forward(len)
    
for i in range(8):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    
    for j in range(12):
        design(100-(j*5),i*45)
    
    h += 0.15
    
t.ht()

tu.done()