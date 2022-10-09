
# AAACoder twitter Logo Art
import turtle as tu

tu.Screen().bgcolor("white")

t = tu.Turtle()
t.speed(0)

# Colors
l_blue = "#62c4f5"

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
go(-200,0)

t.pencolor(l_blue)
t.fillcolor(l_blue)

t.begin_fill()
t.seth(-30)
t.circle(270,125)
t.seth(15)
t.circle(60,50)
t.seth(215)
t.circle(-70,40)
t.seth(25)
t.circle(70,50)
t.seth(210)
t.circle(-80,40)
t.seth(125)
t.circle(80,180)

t.seth(200)
t.circle(-230,55)
t.seth(-110)
t.circle(80,110)

t.seth(210)
t.circle(-60,70)
t.seth(-100)
t.circle(50,110)

t.seth(215)
t.circle(-40,60)
t.seth(-100)
t.circle(40,120)
t.seth(-127)
t.circle(-110,70)
t.end_fill()

go(0,-200)
t.write("twitter",font=("Arial",24,"bold"),align="center")

t.hideturtle()

tu.done()