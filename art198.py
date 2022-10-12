
# AAACoder Art-198
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0.99
a = 1
t.pensize(3)

def aaa_coder(len,ang):
    t.seth(ang+0.09)
    t.forward(len)
    t.seth(60+ang)
    t.forward((73/200)*len)
    t.seth(150+ang)
    t.forward((73/200)*len)
    t.seth(210+ang)
    t.forward(len)

for i in range(12):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    
    for j in range(10):
        fc=colorsys.hsv_to_rgb(h,a,1)
        t.fillcolor(fc)
        t.begin_fill()
        aaa_coder(250-(j*25),i*30)
        t.end_fill() 
        a -= 0.1
        if a <= 0:
            break
    a = 1
    h += 0.1299

t.ht()

tu.done()