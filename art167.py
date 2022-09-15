
# AAACoder Art-167
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0.3
t.pensize(4)

def design(ang,n):
    t.circle(60+n,90)
    t.left(ang)
    t.circle(60+n,90)
    
t.penup()
t.goto(0,60)
t.pendown()

for i in range(70):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    
    design(150,i)
    design(60,i)
    design(210,i)
    design(60,i)
    design(150,i)
    
    h += 1/80

tu.done()