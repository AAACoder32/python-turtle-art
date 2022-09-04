
# AAACoder Art-129
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")

t = tu.Turtle()
t.speed(0)
h = 0
t.pensize(2)

for i in range(300):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    t.fillcolor(c)
    
    t.circle(i,-90)
    t.left(54)
    t.circle(-i,90)
    
    h += 0.006

tu.done()