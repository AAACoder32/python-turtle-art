
# AAACoder Turtle Art
import turtle as tu

tu.Screen().bgcolor("white")

t = tu.Turtle()
t.pensize(4)

# Colours
d_green = "#00D700"
l_green = "#87FF35"
pink = "#FFC2C0"

def go(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  
go(-200,300)
t.write("AAACoder",font=('arial', 20, 'bold'))

# Foot1
go(-250,-100)
t.seth(160)
t.fillcolor(l_green)
t.begin_fill()
t.circle(-20,140)
t.circle(-150,40)
t.circle(-20,140)
t.circle(-150,40)
t.end_fill()

# Circuit ring 1
go(-205,-105)
t.seth(170)
t.begin_fill()
t.circle(20,130)
t.circle(50,30)
t.circle(300,60)
t.circle(50,30)
t.circle(20,130)
t.end_fill()

# Foot2
go(-150,-160)
t.seth(-90)
t.fillcolor(l_green)
t.begin_fill()
t.circle(-20,90)
t.circle(140,30)
t.circle(10,125)
t.circle(150,30)
t.circle(50,91)
t.end_fill()

# Circuit ring 2
go(-200,-90)
t.seth(170)
t.begin_fill()
t.circle(20,130)
t.circle(50,30)
t.circle(300,60)
t.circle(50,30)
t.circle(20,130)
t.end_fill()

# Shield
go(-200,-120)
t.seth(-30)
t.pencolor("black")
t.pensize(4)
t.fillcolor(d_green)
t.begin_fill()
t.circle(300,60)
t.seth(90)
t.circle(150,180)
t.end_fill()

# Hexagonal shape
t.pensize(7)
t.pencolor(l_green)
go(-180,-127)
t.seth(60)
t.forward(30)
t.seth(120)
t.forward(40)
t.backward(40)
t.seth(0)
t.forward(60)
t.seth(-60)
t.forward(60)
t.backward(60)
t.seth(60)
t.forward(60)
t.seth(120)
t.forward(60)
t.seth(180)
t.forward(25)
t.backward(25)
t.seth(60)
t.forward(20)
t.backward(20)
t.seth(120)
t.forward(-60)
t.seth(0)
t.forward(60)
t.seth(60)
t.forward(60)
t.seth(120)
t.forward(10)
t.forward(-10)
t.seth(0)
t.forward(15)
t.forward(-15)
t.seth(60)
t.forward(-60)
t.seth(-60)
t.forward(60)
t.seth(-120)
t.forward(60)
t.seth(180)
t.forward(60)
t.forward(-60)
t.seth(-120)
t.forward(-60)
t.seth(0)
t.forward(60)
t.seth(-60)
t.forward(25)
t.forward(-25)
t.seth(60)
t.forward(30)

# Shield
go(-200,-120)
t.seth(-30)
t.pencolor("black")
t.pensize(4)
t.circle(300,60)
t.seth(90)
t.circle(150,180)

# Head
t.seth(60)
t.fillcolor(l_green)
go(80,-150)
t.begin_fill()
t.circle(120,30)
t.seth(170)
t.circle(-70,110)
t.seth(150)
t.circle(-30,210)
t.seth(20)
t.circle(-70,40)
t.seth(63)
t.circle(-30,210)
t.seth(-55)
t.circle(-70,110)
t.seth(-100)
t.circle(-120,30)
t.end_fill()

# Foot 3
go(80,-150)
t.seth(-0)
t.fillcolor(l_green)
t.begin_fill()
t.circle(-5,140)
t.circle(-60,30)
t.circle(90,40)
t.circle(10,110)
t.circle(120,60)
t.circle(32,180)
t.end_fill()

t.pensize(1)
def oval(x,y,ang,l):  
  go(x,y)
  t.seth(ang)
  t.circle((2/3)*l,80)
  t.circle(l,100)
  t.circle((2/3)*l,80)
  t.circle(l,100)
 
# Eyes
t.fillcolor("black")
t.begin_fill()
oval(65,5,-45,25)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
oval(70,25,-45,8)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
oval(80,10,-45,5)
t.end_fill()

t.fillcolor("black")
t.begin_fill()
oval(140,5,-45,25)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
oval(145,25,-45,8)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
oval(155,10,-45,5)
t.end_fill()

# Pink Chick
t.pencolor(pink)
t.fillcolor(pink)
t.begin_fill()
oval(60,-30,-130,15)
t.end_fill()

t.begin_fill()
oval(150,-30,-130,15)
t.end_fill()

# Mouth
go(95,-30)
t.seth(-90)
t.pencolor("black")
t.fillcolor("black")
t.begin_fill()
t.circle(10,60)
t.circle(30,60)
t.circle(10,60)
t.seth(-80)
t.circle(-14,70)
t.circle(-30,43)
t.circle(-14,90)
t.end_fill()

t.ht()

tu.done()