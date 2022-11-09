
# AAACoder Art-233
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.pensize(3)
t.goto(-170,-100)
h = 0

for i in range(40):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    
    t.left(9)
    t.forward(200)
    t.circle(40,180)
    t.pu()
    t.forward(140)
    t.pd()
    t.left(90)
    t.backward(200)
   
    h += 0.1
    
t.ht()

tu.done()