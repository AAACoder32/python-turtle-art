
# AAACoder Art-244
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Pen()
t.speed(0)
h = 0.3

for i in range(280):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    t.begin_fill()
    t.left(9)
    t.forward(i*0.2)
    t.right(15)
    t.backward(i*0.2)
    t.left(15)
    t.forward(i*0.2)
    t.right(15)
    t.backward(i*0.2)
    t.end_fill()
    
    h += 0.005
    
tu.done()