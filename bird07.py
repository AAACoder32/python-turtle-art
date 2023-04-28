
# AAACoder Birt Art-07
import turtle as tu

tu.Screen().bgcolor("white")

t = tu.Pen()
t.pensize(3)

# Colors
pink = "#FF4BAA"
yellow = "#FFD941"
white = "#ffffff"
black = "#000000"
red = "#FF4229"
orange = "#FF6D00"

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
# Feet
t.color(orange)
go(-70,-220)
t.width(12)
t.seth(-95)
t.forward(100)
t.width(8)
t.seth(15)
t.forward(25)
t.backward(25)

t.seth(-20)
t.forward(35)
t.backward(35)

t.seth(-70)
t.forward(25)
t.backward(25)

go(0,-210)
t.width(12)
t.seth(-70)
t.forward(100)
t.width(8)
t.seth(20)
t.forward(25)
t.backward(25)

t.seth(-17)
t.forward(35)
t.backward(35)

t.seth(-60)
t.forward(25)
t.backward(25)
    
# Body
go(-300,0)
t.seth(-90)
t.color(pink)
t.begin_fill()
t.circle(220,70)
t.circle(250,115)
t.forward(70)
t.circle(105,137)
t.circle(900,15)
t.circle(-70,100)
t.circle(-300,17)
t.end_fill()

# Chonch
t.color(red)
go(140,40)
t.seth(90)
t.begin_fill()
t.forward(80)
t.circle(-5,120)
t.forward(80)
t.circle(-8,120)
t.forward(80)
t.circle(-5,120)
t.forward(20)
t.end_fill()

# Eye
go(100,110)
t.color(white)
t.begin_fill()
t.circle(45)
t.end_fill()

go(80,120)
t.color(black)
t.begin_fill()
t.circle(15)
t.end_fill()

go(75,127)
t.color(white)
t.begin_fill()
t.circle(5)
t.end_fill()

# Wing
go(-180,-140)
t.color(yellow)
t.seth(-22)
t.begin_fill()
t.forward(60)
t.circle(200,30)
t.circle(120,40)
t.circle(80,156)
t.circle(300,37)
t.end_fill()

t.color(orange)
go(-130,-130)
t.seth(-30)
t.circle(60,60)
t.seth(-30)
t.circle(60,60)
t.seth(-30)
t.circle(40,60)

go(-100,-95)
t.seth(-30)
t.circle(30,60)
t.seth(-30)
t.circle(50,60)
t.seth(-30)
t.circle(40,60)

go(-70,-60)
t.seth(-30)
t.circle(30,60)
t.seth(-30)
t.circle(20,60)
t.seth(-30)
t.circle(40,60)

t.ht()

tu.done()