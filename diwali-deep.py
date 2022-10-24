
# AAACoder Diwali Deep Art
import turtle as tu

tu.Screen().bgcolor("#124067")
t = tu.Turtle()
t.pensize(4)

# Colours
red = "#ff1012"
blue = "#6cc3f5"
orange = "#ed8d26"
yellow = "#f5ca1d"
green = "#92ed24"
r_br = "#2e1b1d"

# Let's start
def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def petals(len,ang=0):
    t.seth(ang)
    t.circle(len,30)
    t.circle((30/110)*len,40)
    t.circle((15/110)*len,90)
    t.circle((30/110)*len,40)
    t.circle(len,30)
 
def fire(len,ang=0):
    t.seth(45+ang)
    t.circle((3/4)*len,90)
    t.circle((-9/16)*len,40)
    t.seth(-120+ang)
    t.circle((-5/16)*len,30)
    t.circle(len,30)
    t.circle((9/16)*len,60)
    t.circle(len,30)
    
def yellow_des(len,ang=0):
    t.seth(ang)
    t.circle(150,15)
    t.circle(30,180)
    t.circle(150,15)
    
# Main semi-circle
go(-230,50)
t.seth(-90)
t.fillcolor(red)

t.begin_fill()
t.circle(230,181)
t.end_fill()

# Blue petals
go(0,-180)
t.seth(0)
t.fillcolor(blue)
t.begin_fill()
t.circle(230,20)
t.circle(30,60)
t.circle(15,90)
t.circle(30,60)
t.end_fill()

go(-0,-180)
t.seth(180)
t.fillcolor(blue)
t.begin_fill()
t.circle(-230,20)
t.circle(-30,60)
t.circle(-15,90)
t.circle(-30,60)
t.end_fill()

go(0,-180)
t.begin_fill()
petals(140,20)
t.end_fill()

go(5,-163)
t.begin_fill()
petals(140,107)
t.end_fill()

go(5,-178)
t.begin_fill()
petals(150,63)
t.end_fill()

# Brown strip
go(-230,52.5)
t.seth(-18)
t.fillcolor(r_br)
t.begin_fill()
t.circle(300,45)
t.seth(-27)
t.circle(300,45.6)
t.seth(90)
t.circle(20,69)
t.circle(600,42)
t.circle(30,60)
t.end_fill()

# Fire flame
t.fillcolor(yellow)
go(30,50)
t.begin_fill()
fire(170)
t.end_fill()

t.fillcolor(orange)
go(20,50)
t.begin_fill()
fire(140)
t.end_fill()

t.fillcolor(red)
go(10,50)
t.begin_fill()
fire(70)
t.end_fill()

# yellow des
go(-225,3)
t.seth(-78)
t.fillcolor(yellow)
t.begin_fill()
t.circle(230,15)
t.circle(30,150)
t.circle(110,18)
t.end_fill()

go(229,30)
t.seth(-95)
t.begin_fill()
t.circle(-230,20)
t.circle(-20,120)
t.circle(-30,120)
t.end_fill()

go(-150,0)
t.begin_fill()
yellow_des(50,-94)
t.end_fill()

go(-90,15)
t.begin_fill()
yellow_des(50,-105)
t.end_fill()

go(-30,26)
t.begin_fill()
yellow_des(50,-105)
t.end_fill()

go(30,20)
t.begin_fill()
yellow_des(50,-105)
t.end_fill()

go(90,15)
t.begin_fill()
yellow_des(50,-105)
t.end_fill()

go(150,5)
t.begin_fill()
yellow_des(50,-105)
t.end_fill()

# orange strip
go(-230,50)
t.seth(-90)
t.circle(230,170)

t.fillcolor(orange)
t.begin_fill()
t.seth(-160)
t.circle(-300,44.5)
t.seth(-154.5)
t.circle(-300,44)

t.seth(103)
t.circle(-230,12)

t.seth(-18)
t.circle(300,45)
t.seth(-27)
t.circle(300,45.5)
t.seth(-89)
t.circle(-230,12)
t.end_fill()

go(0,-330)
t.pencolor(yellow)
t.write("शुभ दीपावली",font=("Verdana",24,"bold"),align="center")

go(0,450)
t.pencolor("#ffffff")
t.write("AAACoder",font=("Courier",18,"bold"),align="center")

t.ht()

tu.done()