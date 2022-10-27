
# AAACoder Art-214
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0.3
t.pensize(3)

def design(ang,n):
    t.circle(20+n,75)
    t.left(ang)
    t.circle(20+n,65)

for i in range(150):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    
    design(90,i)
    t.pu()
    design(29,i)
    design(90,i)
    t.pd()
    
    h += 0.006
    
t.ht()

tu.done()