
# AAACoder Art-232
import turtle as tu

tu.Screen().bgcolor("#11171F")

t = tu.Turtle()
t.speed(8)
t.pencolor("red")
t.pensize(4)

c = ["#FF4637","#4FD124","#AA4AFF"]

def aaa(len,ang=0,cl=c):
    t.seth(ang)
    t.pencolor(cl[0])
    t.forward(len)
    t.seth(45+ang)
    t.pencolor(cl[1])
    t.forward(2*len)
    t.seth(-25+ang)
    t.pencolor(cl[2])
    t.circle((5/3)*len,315)
    t.seth(-135+ang)
    t.pencolor(cl[1])
    t.forward(2*len)
    t.seth(-100+ang)
    t.pencolor(cl[0])
    t.forward((28/30)*len)
    
for i in range(12):
    aaa(50,i*30)

t.ht()

tu.done()