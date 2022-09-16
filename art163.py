
# AAACoder Art-163
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0
t.pensize(3)

def design(ang,n):
    t.circle(60+n,90)
    t.left(ang)
    t.circle(60+n,90)
    
t.penup()
t.goto(-30,0)
t.pendown()

t.seth(15)

for i in range(80):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    
    design(60,i)
    design(45,i)
    design(120,i)
    design(45,i)
    
    h += 1/55

tu.done()