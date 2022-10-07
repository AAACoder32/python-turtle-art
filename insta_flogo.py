
# AAACoder Frog Logo Art
import turtle as tu

tu.Screen().bgcolor("white")

t = tu.Turtle()

# Colors
l_blue = "#62c4f5"
green = "#03731a"
orange = "#f28416"
d_blue = "#081e8c"
white = "#ffffff"

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
# Rectangular child module
def rect_cm(len,ang=0):
    t.seth(ang)
    t.forward((30/37)*len)
    t.seth(45+ang)
    t.forward((10/37)*len)
    t.seth(90+ang)
    t.forward((30/37)*len)
    t.seth(180+ang)
    t.forward(len)
    t.seth(-90+ang)
    t.forward(len)
    t.seth(0)
    
# Rectangular parent module
def rect_pm(x,y,len):
    t.pensize(1)
    go(x,y)
    t.pencolor(green)
    t.fillcolor(green)
    t.begin_fill()
    rect_cm(len)
    t.end_fill()
    go(x+(len*2),y)
    t.pencolor(orange)
    t.fillcolor(orange)
    t.begin_fill()
    rect_cm(len,90)
    t.end_fill()
    go(x+(len*2),y+(len*2))
    t.pencolor(l_blue)
    t.fillcolor(l_blue)
    t.begin_fill()
    rect_cm(len,180)
    t.end_fill()
    go(x,y+(len*2))
    t.pencolor(d_blue)
    t.fillcolor(d_blue)
    t.begin_fill()
    rect_cm(len,270)
    t.end_fill()
    
# Frog
def frog(len,ang=0):
    t.seth(-45+ang)
    t.circle(len,45)
    t.penup()
    t.circle(len,45)
    t.pendown()
    t.circle(len/2,90)
    t.seth(70+ang)
    t.circle(len/4,180)
    t.seth(165+ang)
    t.circle(len,30)
    t.seth(115+ang)
    t.circle(len/4,180)
    t.seth(-129.5+ang)
    t.circle(len/2,90)
    
# it
def it_m(len,ang=0):
    t.seth(ang)
    t.forward((5/31)*len)
    t.seth(90+ang)
    t.forward((25/31)*len)
    t.seth(180+ang)
    t.forward((3/62)*len)
    t.circle(-(3/62)*len,180)
    t.forward((13/62)*len)
    t.circle(-(3/62)*len,90)
    t.forward((23/31)*len)
    t.circle((4/31)*len,90)
    t.forward((5/31)*len)
    t.seth(90+ang)
    t.forward((3/31)*len)
    t.seth(180+ang)
    t.forward((2/31)*len)
    t.circle(-(5/62)*len,90)
    t.forward((20/31)*len)
    t.seth(180+ang)
    t.forward((1/31)*len)
    t.circle(-(3/62)*len,180)
    t.forward((6/31)*len)
    t.seth(90+ang)
    t.forward((3/31)*len)
    t.seth(180+ang)
    t.forward((4/31)*len)
    t.circle(-(1/31)*len,90)
    t.forward((8/31)*len)
    t.seth(180+ang)
    t.forward((9/62)*len)
    t.seth(-90+ang)
    t.forward((8/31)*len)
    t.circle(-(1/31)*len,90)
    t.forward((21/62)*len)
    t.seth(-90+ang)
    t.forward(len)
    
# Glob
def glob(len,ang=0,x=0,y=0):
    go(x,y)
    t.seth(ang)
    t.begin_fill()
    t.circle(len)
    t.end_fill()
    t.seth(ang)
    t.circle((2/5)*len,40)
    t.circle((59/50)*len,100)
    t.circle((2/5)*len,80)
    t.circle((59/50)*len,100)
    t.circle((2/5)*len,40)
    t.seth(90+ang)
    t.forward(len*2)
    t.backward(2*len)
    
    t.seth(ang)
    t.circle(len,46)
    t.seth(180+ang)
    t.forward((8/5)*len)
    t.backward((8/5)*len)

    t.seth(46+ang)
    t.circle(len,30)
    t.seth(180+ang)
    t.forward((49/25)*len)
    t.backward((49/25)*len)

    t.seth(76+ang)
    t.circle(len,30)
    t.seth(180+ang)
    t.forward((49/25)*len)
    t.backward((49/25)*len)

    t.seth(106+ang)
    t.circle(len,28)
    t.seth(180+ang)
    t.forward((8/5)*len)
    t.backward((8/5)*len)
    
    go(-len+x,(4/5)*len+y)
    t.seth(-160+ang)
    t.pensize((3/25)*len)
    t.pencolor("black")
    t.circle((3/20)*len,150)
    t.circle((11/5)*len,60)
    t.circle((3/20)*len,150)
    
def cir(r,c):
    t.pencolor(c)
    t.fillcolor(c)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    
# Main Design
t.pensize(9)
t.pencolor(green)
go(-130,0)
frog(200)

go(0,-80)
t.pensize(1)
t.fillcolor(green)
t.begin_fill()
it_m(120)
t.end_fill()

t.pencolor(white)
t.pensize(2)
t.fillcolor(orange)
glob(30,x=15,y=42)

rect_pm(130,-30,50)
rect_pm(250,40,30)
rect_pm(190,110,35)

go(-90,125)
cir(30,green)

go(107,130)
cir(30,green)

tu.done()