import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Pen()
t.speed(0)

h = 0

def lerp(a,b,t):
    return a+(b-a)*t

for i in range(300):
    c = colorsys.hsv_to_rgb(h,lerp(0.5,1,0.2),1)
    t.pencolor(c)
    
    t.left(120)
    t.circle(i,90)
    t.circle(i,90)
    
    h += 0.005
    
turtle.done()