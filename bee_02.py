
import turtle

turtle.Screen().bgcolor("white")

t = turtle.Turtle()

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
# Head Circle
t.pencolor("yellow")
t.fillcolor("yellow")
go(-120,70)
t.seth(-58)

t.begin_fill()
t.circle(180,120)
t.circle(120,60)
t.circle(180,120)
t.circle(120,60)
t.end_fill()

# Left Eye
t.pencolor("white")
t.fillcolor("white")
go(-80,150)
t.begin_fill()
t.circle(55)
t.end_fill()

t.pencolor("black")
t.fillcolor("black")
go(-40,180)
t.begin_fill()
t.circle(25)
t.end_fill()

t.pencolor("white")
t.fillcolor("white")
go(-20,195)
t.begin_fill()
t.circle(10)
t.end_fill()

# Right Eye
t.pencolor("white")
t.fillcolor("white")
go(50,150)
t.begin_fill()
t.circle(55)
t.end_fill()

t.pencolor("black")
t.fillcolor("black")
go(90,180)
t.begin_fill()
t.circle(25)
t.end_fill()

t.pencolor("white")
t.fillcolor("white")
go(110,195)
t.begin_fill()
t.circle(10)
t.end_fill()

# Mouth
t.pencolor("black")
t.pensize(5)
go(-20,60)
t.seth(-70)
t.circle(80,30)
t.circle(50,80)
t.circle(90,35)

# Bee Antena
# Left
go(10,285)
t.seth(100)

t.circle(120,70)
t.circle(20,200)
t.circle(15,100)
t.circle(10,200)

# Right
go(30,285)
t.seth(80)

t.circle(-120,60)
t.circle(-20,200)
t.circle(-15,100)
t.circle(-10,200)

# Body
go(-120,70)
t.seth(-58)
t.fillcolor("black")
t.pensize(1)
t.penup()
t.circle(180,30)
t.pendown()

t.begin_fill()
t.circle(180,40)
t.seth(-65)
t.circle(-180,35)
t.circle(-150,40)
t.circle(-100,80)
t.seth(185)
t.forward(30)
t.seth(60)
t.forward(30)
t.seth(138)
t.circle(-90,60)
t.circle(-145,55)
t.end_fill()

# Strip
t.pencolor("yellow")
t.fillcolor("yellow")
t.seth(-50)
go(-130,-70)

t.begin_fill()
t.circle(250,52)
t.seth(55)
t.circle(80,35)
t.seth(193)
t.circle(-160,79)
t.seth(-138)
t.circle(120,28)
t.end_fill()

# Feathers
t.pencolor("black")
t.fillcolor("#D8EFF6")
t.pensize(3)

go(-122,-50)
t.seth(120)
t.begin_fill()
t.circle(120,70)
t.circle(50,90)
t.circle(20,110)
t.circle(-120,65)
go(-122,-50)
t.seth(120)
t.circle(120,70)
t.circle(50,70)
t.forward(30)
t.circle(20,135)
t.circle(-120,65)
t.end_fill()

t.hideturtle()

turtle.done()
