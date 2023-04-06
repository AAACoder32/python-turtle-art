
# AAACoder Art-188
import turtle as tu
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0.3
t.pensize(4)
    
def design2(set_ang,len):
    t.seth(set_ang)
    t.forward(300-len)
    t.seth(set_ang+60)
    t.circle(110-((110/300)*len),90)
    t.seth(set_ang-150)
    t.forward(300-len)
 
for i in range(12):
    c = colorsys.hsv_to_rgb(h,.8,1)
    t.pencolor(c)
    
    for j in range(30):    
        if j==29:
            t.fillcolor(c)
            t.begin_fill()
            design2(i*30,j*5)
            t.end_fill()
        else:
            design2(i*30,j*5)
   
    h += 0.15

tu.done()