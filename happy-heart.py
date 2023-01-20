
# AAACoder Smiley Heart ❤️ Art

import turtle as tu

tu.Screen().bgcolor("white")

t = tu.Turtle()
t.speed(6)
t.pensize(5)

# Colors
pink = "#f74fe1"
light_blue = "#d4fafc"

# Unicorn Horns colors
red = "#e61515"
orange = "#bf7b0d"
yellow = "#f0e518"
green = "#18f01c"
blue = "#18f0f0"

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
# Heart
go(00,-150)

t.seth(60)

t.fillcolor(pink)

t.begin_fill()
t.circle(-120,50)
t.circle(220,30)
t.circle(130,190)

t.seth(129)
t.circle(130,190)
t.circle(220,30)
t.circle(-120,50)
t.end_fill()

# Eyes
def eye(x,y):
    t.pensize(2)
    go(x,y)
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    t.circle(40) 
    t.end_fill()
    go(x+27,y+20)
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(15) 
    t.end_fill()

    go(x+5,y+15)
    t.begin_fill()
    t.circle(6) 
    t.end_fill()

    go(x+20,y-5)
    t.begin_fill()
    t.circle(6) 
    t.end_fill()
    
    t.pensize(5)
    
# Left eye
eye(-150,30)

# Right eye
t.pencolor("black")
t.fillcolor("black")
eye(75,30)

# Mouth
t.pensize(8)
t.pencolor("black")
go(-55,0)
t.seth(-78)
t.circle(50,160)

# Feather
# Right
def fu_part(x,y,r=60):
    go(x,y)
    t.seth(-5)
    t.circle(r,60)
    t.circle(r/6,120)
    
go(210,-20)
t.seth(-20)
t.pensize(5)

t.fillcolor(light_blue)
t.begin_fill()
t.circle(120,20)
t.circle(20,120)

fu_part(250,0)
fu_part(270,35)

go(305,70)
t.seth(30)
t.circle(70,60)
t.circle(30,150)
t.circle(-90,48)
t.seth(-69)
t.circle(-130,56)
t.end_fill()

# Left
def fl_part(x,y):
    go(x,y)
    t.seth(180)
    t.circle(-60,60)
    t.circle(-10,120)
    
go(-205,-20)
t.seth(200)
t.begin_fill()
t.circle(-120,20)
t.circle(-20,120)

fl_part(-240,0)
fl_part(-265,40)

go(-295,80)
t.seth(165)
t.circle(-70,70)
t.circle(-30,150)
t.circle(90,60)
t.seth(-120)
t.circle(130,65)
t.end_fill()

# Unicorn Horns

# 1
t.seth(-18)
go(-20,110)
t.fillcolor(blue)
t.begin_fill()
t.circle(90,30)
t.seth(95)
t.forward(140)
t.circle(10,168)
t.forward(138)
t.end_fill()

# 2
t.seth(-18)
go(-20,110)
t.fillcolor(green)
t.begin_fill()
t.circle(90,30)
t.seth(95)
t.forward(115)
t.seth(-175)
t.circle(-30,50)
t.seth(-97)
t.forward(120)
t.end_fill()

# 3
t.seth(-18)
go(-20,110)
t.fillcolor(yellow)
t.begin_fill()
t.circle(90,30)
t.seth(95)
t.forward(85)
t.seth(-175)
t.circle(-37,50)
t.seth(-97)
t.forward(90)
t.end_fill()

# 4
t.seth(-18)
go(-20,110)
t.fillcolor(orange)
t.begin_fill()
t.circle(90,30)
t.seth(95)
t.forward(53)
t.seth(-175)
t.circle(-45,50)
t.seth(-99)
t.forward(60)
t.end_fill()

# 5
t.seth(-18)
go(-20,110)
t.fillcolor(red)
t.begin_fill()
t.circle(90,30)
t.seth(95)
t.forward(25)
t.seth(-175)
t.circle(-53,50)
t.seth(-97)
t.forward(34)
t.end_fill()

t.hideturtle()

tu.done()
