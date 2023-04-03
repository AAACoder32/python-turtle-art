
# AAACoder Art-245
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")

t = tu.Pen()
t.speed(0)
h = 0.3

for i in range(180):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    t.begin_fill()
    t.left(59)
    t.forward(i)
    t.right(90)
    t.backward(i)
    t.circle(30,120)
    t.forward(i)
    t.end_fill()
    h += 0.005
    
tu.done()
