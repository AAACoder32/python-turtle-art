
# AAACoder N letter Art 
import turtle as tu

tu.Screen().bgcolor("black")

t = tu.Turtle()

t.pencolor("#D1B000")
t.fillcolor("#D1B000")
t.speed(0)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# First Part 
go(-200,-50)

t.begin_fill()
t.seth(-115)
t.circle(30,300)
t.seth(125)
t.circle(-200,180)
t.seth(-135)
t.forward(100)
t.seth(53)
t.forward(75)
t.seth(125)
t.circle(170,180)

t.seth(70)
t.forward(200)
t.seth(0)
t.forward(70)
t.seth(-60)
t.forward(130)
t.seth(45)
t.forward(190)
t.seth(120)
t.circle(230,187)

t.end_fill()

# Second Part
go(230,135)

t.begin_fill()
t.seth(70)
t.circle(30,300)
t.seth(-75)
t.circle(-200,140)
t.seth(70)
t.forward(100)
t.seth(-100)
t.forward(75)
t.seth(-35)
t.circle(170,142)

t.seth(-132)
t.forward(160)
t.seth(180)
t.forward(60)
t.seth(120)
t.forward(130)


t.seth(-110)
t.forward(235)
t.seth(-40)
t.circle(230,152)

t.end_fill()
t.hideturtle()

tu.done()