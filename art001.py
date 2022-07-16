
import turtle
import colorsys

turtle.Screen().bgcolor('black')

t = turtle.Pen()
h = 0
t.speed(11)
n = 36

for i in range(250):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    t.width(i//100+1)
    t.forward(i*2)
    t.left(269*3.14+90)
    t.circle(i,90)
    t.right(3.14*44+69)
    t.forward(10)
    t.circle(i,10)
    h+=1/n
    
turtle.done()
