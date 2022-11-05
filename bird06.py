
# AAACoder Bird Art-06
import turtle as tu

tu.Screen().bgcolor("white")

t = tu.Turtle()

# Colours
black = "#000000"
white = "#ffffff"
blue = "#78C2FF"
red = "#FF4536"
pink = "#FF00A1"
yellow = "#DAFF00"

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
def feather(ang,len):
    t.seth(ang)
    t.forward(len)
    t.seth(130+ang)
    t.forward(len)
    t.circle((8/7)*len,60)
    t.circle(0.47*len,120)
    t.circle((8/7)*len,60)
    
# Road
t.pensize(3)
go(-300,-200)
t.seth(-20)
t.circle(700,30)
t.circle(-700,20)
    
# Feather 
t.pensize(7)
go(-160,40)
t.fillcolor(red)
t.begin_fill()
feather(-95,85)
t.end_fill()

# Body
go(-120,30)
t.seth(-70)
t.fillcolor(blue)
t.begin_fill()
t.circle(220,60)
t.circle(80,190)
t.circle(-90,120)
t.circle(50,176.8)
t.circle(220,56)
t.end_fill()

# Feather 2nd
go(0,20)
t.fillcolor(red)
t.begin_fill()
feather(-35,75)
t.end_fill()

# Eyes
t.pensize(4)
go(-90,220)
t.pensize(4)
t.seth(-90)
t.circle(20,60)
go(-30,200)
t.seth(-125)
t.circle(-20,60)

# Chonch
go(-80,190)
t.seth(-100)
t.pensize(3)
t.fillcolor(yellow)
t.begin_fill()
t.circle(120,20)
t.seth(50)
t.circle(120,20)
t.seth(154)
t.circle(60,20)
t.end_fill()

# Feet
# Left
t.pensize(5)
go(70,-110)
t.seth(-90)
t.forward(120)
t.pensize(3)
t.seth(30)
t.forward(30)
t.backward(30)
t.seth(50)
t.forward(25)
t.backward(25)
t.seth(-20)
t.forward(20)
t.backward(20)

# Right
t.pensize(5)
go(10,-100)
t.seth(-75)
t.forward(140)
t.pensize(4)
t.seth(-160)
t.forward(30)
t.backward(30)
t.seth(170)
t.forward(25)
t.backward(25)
t.seth(-140)
t.forward(20)
t.backward(20)

# Crest
def crest(len,ang,f_cl,flip=False):
    sign = 1
    if flip:
        sign = -1
    t.seth(ang)
    t.circle(len,sign*60)
    if sign==-1:
        t.seth(ang)
    else:
        t.seth(-60+ang)
    t.fillcolor(f_cl)
    t.begin_fill()
    t.circle((1/8)*len,90)
    t.circle((2/8)*len,90)
    t.circle((1/8)*len,90)
    t.circle((2/8)*len,90)
    t.end_fill()
   
go(130,-70)
crest(60,-45,red)

go(140,-60)
crest(80,-15,pink)

go(-60,260)
crest(60,-65,pink,True)

go(-50,255)
crest(60,-85,yellow,True)

go(-45,253)
crest(50,-109,red,True)

t.ht()

tu.done()