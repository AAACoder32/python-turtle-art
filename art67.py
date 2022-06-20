
import turtle
import colorsys

turtle.Screen().bgcolor("black")
t = turtle.Pen()

h = 0
n = 100

t.speed(11)

for i in range(300):
    
    c = colorsys.hsv_to_rgb(h,0.6,1)
    t.pencolor(c)
    t.width(i//100+1)
    t.right(150)
    t.forward(i)
    t.left(220)
    t.forward(i*0.01)
    t.right(90)
    t.forward(i)
    
    h += 1/n

turtle.done()
