
# AAACoder Art-203
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()

t.speed(0)
h = 0.99
t.pensize(3)
    
def aaa_coder(len,ang=0):
    t.seth(ang)
    t.forward(len)
    t.circle(0.13*len,180)
    t.seth(29.1+ang)
    t.circle(0.13*len,180)
    t.forward(len)

for i in range(12):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    t.fillcolor(c)
    for j in range(25):
        aaa_coder(250-(j*5),i*30)
        if j>=24:
            t.begin_fill()
            aaa_coder(250-(j*5),i*30)
            t.end_fill()
    h += 0.1299

t.ht()

tu.done()