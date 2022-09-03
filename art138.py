# AAACoder Art-138
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0

def design(ang,n):
    t.circle(60+n,90)
    t.left(ang)
    t.circle(60+n,90)
    
def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
go(0,150)

for i in range(30):
    t.pensize(i//100+2)
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    design(90,i)
    design(180,i)
    design(45,i)
    design(45,i)
    design(180,i)
    design(90,i)
    h += 0.01

tu.done()