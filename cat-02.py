
# AAACoder Cute Cat Art
import turtle as tu
import colorsys

tu.Screen().bgcolor("white")
t = tu.Turtle()

h = 0.99
t.pensize(5)

# Colors
sk_cl = "#f7beba"
l_gr = "#c4c4c4"
r_cl = "#eb2323"

# Let's start
def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def m_shape(len,ang=0):
    t.seth(ang)
    t.circle(len,10)
    t.seth(130+ang)
    t.circle(0.3*len,30)
    t.seth(50+ang)
    t.circle(0.3*len,20)
    t.seth(180+ang)
    t.circle((3/4)*len,10)
    
def heart(len,ang=0):
    t.seth(45+ang)
    t.circle(-len,20)
    t.circle(len,60)
    t.circle(0.4*len,180)
    t.seth(90+ang)
    t.circle(0.4*len,180)
    t.circle(len,60)
    t.circle(-len,20)
    
def tria(len,ang=0):
    t.pensize(1)
    t.seth(ang)
    t.circle(len,20)
    t.seth(150+ang)
    t.circle(len,20)
    t.seth(-105+ang)
    t.circle(0.5*len,20)
    
    
go(0,-100)
t.seth(-5)
# Head sketch
t.forward(70)
t.circle(200,40)
t.circle(60,30)
t.circle(350,50)
t.circle(200,65)
t.forward(50)
t.circle(200,60)
t.circle(330,50)
t.circle(80,30)
t.circle(200,34)
t.forward(80)

# Right m shape
t.fillcolor("white")
go(220,-10)
t.begin_fill()
m_shape(280,-20)
t.end_fill()

# Left m shape 
go(-200,40)
t.begin_fill()
m_shape(280,180)
t.end_fill()

# Left ear
go(220,220)
t.seth(40)
t.begin_fill()
t.circle(120,60)
t.seth(155)
t.circle(130,60)
t.end_fill()

go(220,220)
t.seth(40)
t.circle(120,60)
t.seth(170)
t.circle(110,60)

go(230,260)
t.pencolor(sk_cl)
t.fillcolor(sk_cl)
t.pensize(1)
t.seth(60)
t.begin_fill()
t.circle(90,30)
t.circle(10,90)
t.circle(90,30)
t.circle(15,90)
t.circle(48,60)
t.circle(10,90)
t.end_fill()

# Right ear
t.pencolor("black")
t.fillcolor("white")
t.pensize(5)
go(-180,230)
t.seth(-40)
t.begin_fill()
t.circle(120,-60)
t.seth(23)
t.circle(-130,60)
t.end_fill()

go(-180,230)
t.seth(-40)
t.begin_fill()
t.circle(120,-60)
t.seth(10)
t.circle(-110,60)

go(-190,270)
t.pencolor(sk_cl)
t.fillcolor(sk_cl)
t.pensize(1)
t.seth(120)
t.begin_fill()
t.circle(-90,30)
t.circle(-10,90)
t.circle(-90,30)
t.circle(-15,90)
t.circle(-48,60)
t.circle(-10,90)
t.end_fill()

# Triangular strips
go(0,360)
t.pencolor(l_gr)
t.fillcolor(l_gr)
t.begin_fill()
tria(200,-85)
t.end_fill()

go(-60,355)
t.begin_fill()
tria(200,-75)
t.end_fill()

go(60,360)
t.begin_fill()
tria(200,-95)
t.end_fill()

go(-223,90)
t.begin_fill()
tria(160,3)
t.end_fill()

go(-222,130)
t.begin_fill()
tria(160,-1)
t.end_fill()

go(251,90)
t.begin_fill()
tria(160,182)
t.end_fill()

go(250,135)
t.begin_fill()
tria(160,185)
t.end_fill()

# Right Ear
t.pensize(1)
t.pencolor(sk_cl)
t.fillcolor(sk_cl)
go(-110,50)
t.begin_fill()
t.circle(20)
t.end_fill()
t.pencolor("black")
t.pensize(12)
t.seth(70)
go(-120,50)
t.circle(-30,80)
t.circle(-80,30)

# Left Ear
t.pensize(1)
t.pencolor(sk_cl)
t.fillcolor(sk_cl)
go(125,15)
t.begin_fill()
t.circle(20)
t.end_fill()
t.pencolor("black")
t.pensize(12)
t.seth(30)
go(60,50)
t.circle(-60,30)
t.circle(-30,80)

# Nose
t.pensize(5)
t.seth(0)
go(0,30)
t.forward(10)
t.circle(10,180)
t.forward(10)
t.circle(10,180)

# Mouth
go(0,10)
t.seth(-90)
t.circle(-15,80)
t.circle(4,180)
t.circle(-5,180)
t.circle(4,180)
t.circle(-13,80)

# Heart
t.pensize(1)
t.pencolor(r_cl)
t.fillcolor(r_cl)
go(-60,-70)
t.begin_fill()
heart(50,25)
t.end_fill()

go(-185,-42)
t.begin_fill()
heart(30,-4)
t.end_fill()

go(-250,-80)
t.begin_fill()
heart(20,30)
t.end_fill()

# Belly
t.pensize(5)
t.pencolor("black")
go(-70,-97)
t.seth(-110)
t.circle(300,30)

go(70,-110)
t.seth(-80)
t.circle(-300,30)

# Hand
go(-70,-97)
t.seth(-140)
t.forward(50)
t.seth(-90)
t.circle(-5,150)
t.circle(70,60)
t.circle(5,180)
t.seth(180)
t.forward(4)
t.circle(6,180)
t.seth(180)
t.forward(6)
t.circle(7,170)

t.circle(-90,40)
t.circle(30,120)

# Hide the turtle
t.ht()

tu.done()