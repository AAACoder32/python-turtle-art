
# AAACoder Bird Art-05
import turtle as tu

tu.Screen().bgcolor("white")

t = tu.Turtle()
t.pensize(3)

# Colours
d_cl = "#19358d"
l_cl = "#3670ab"
black = "#000000"
white = "#ffffff"

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
# Chonch
go(-105,140)
t.seth(170)
t.begin_fill()
t.forward(46)
t.circle(-2,150)
t.forward(55)
t.seth(-100)
t.forward(40)
t.end_fill()

def crest(ang):
    t.seth(ang)
    t.forward(90)
    t.seth(-90+ang)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
# Crest
t.pensize(6)
go(-40,170)
crest(90)
go(-42,170)
crest(110)
go(-27,170)
crest(80)

# Legs
go(-20,-50)
t.seth(-90)
t.pensize(16)
t.forward(70)
go(30,-50)
t.forward(70)
    
# Body
t.pensize(3)
go(-50,-50)
t.seth(-8)
t.pencolor(d_cl)
t.fillcolor(d_cl)
t.begin_fill()
t.forward(175)
t.circle(10,135)
t.forward(150)
t.circle(-130,40)
t.circle(60,176)
t.forward(110)
t.circle(89.5,87)
t.end_fill()

# Feather
go(30,0)
t.pencolor(l_cl)
t.fillcolor(l_cl)
t.seth(0)
t.begin_fill()
t.forward(70)
t.circle(8,140)
t.forward(70)
t.circle(90,30)
t.circle(35,156)
t.circle(90,30)
t.end_fill()

# Eye
go(-45,150)
t.seth(0)
t.pensize(1)
t.pencolor(white)
t.fillcolor(white)
t.begin_fill()
t.circle(15)
t.end_fill()

go(-45,157)
t.pencolor(black)
t.fillcolor(black)
t.begin_fill()
t.circle(7)
t.end_fill()

t.ht()

tu.done()


