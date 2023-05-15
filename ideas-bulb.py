
# AAACoder Art
import turtle as tu

tu.Screen().bgcolor("#77fc9b")

t = tu.Turtle()

t.pensize(20)
t.pencolor("#ffffff")

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# Bulb main
go(-30,-100)
t.forward(100)
t.circle(10,90)
t.forward(120)
t.circle(-20,60)
t.circle(180,300)
t.circle(-20,60)
t.forward(120)
t.circle(10,90)
t.forward(60)

# Connector
go(-71,-100)
t.seth(-70)
t.circle(75,140)

# Lines
t.seth(0)
go(-80,-50)
t.forward(150)

go(-80,0)
t.forward(150)

# Pencil
t.seth(90)
go(-40,0)
t.forward(150)
t.seth(60)
t.forward(80)
t.seth(-60)
t.forward(80)
t.seth(-90)
t.forward(150)

t.seth(90)
go(-40,0)
t.forward(150)
t.seth(-60)
t.circle(45,110)

# Lines
def line(x,y,l,a):
    t.seth(a)
    go(x,y)
    t.forward(l)
    
line(220,210,40,0)
line(-220,210,40,180)

line(190,100,40,-45)
line(-195,100,40,-135)

line(165,350,40,45)
line(-165,350,40,135)

go(0,-300)
t.write("Ideas",font=("Times New Roman",32,"bold"),align="center")

tu.done()