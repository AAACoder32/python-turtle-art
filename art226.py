
# AAACoder Art-226
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0
t.pensize(3)

def design(n):
    t.forward(n)
    t.circle(-10,120)
    t.forward(n)
    t.circle(10,150)

t.setpos(-50,0)
for i in range(200):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    design(i*0.5)
    h += 0.082
    
t.ht()

tu.done()