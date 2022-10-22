
# AAACoder Art-206
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0.6
t.pensize(3)

def design(ang,n):
    t.circle(60+n,90)
    t.left(ang)
    t.circle(60+n,90)

for i in range(100):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    
    design(60,i)
    design(30,i)
    design(120,i)
    design(30,i)
    design(60,i)
    
    h += 0.006

tu.done()