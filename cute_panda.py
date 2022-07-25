
import turtle

turtle.Screen().bgcolor("white")

t = turtle.Turtle()
t.pensize(6)
t.speed(0)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.seth(0)
    
go(-300,-100)

# Wall line
t.forward(600)

# Ear
t.fillcolor("#282928")
# Right Ear
go(150,95)
t.begin_fill()
t.circle(45)
t.end_fill()

# Left Ear
go(-50,130)
t.begin_fill()
t.circle(45)
t.end_fill()

# Head
t.fillcolor("white")
go(-120,70)
t.seth(-100)
t.begin_fill()
t.circle(90,30)
t.circle(160,120)
t.circle(90,30)
t.circle(151,180)
t.end_fill()

# Eye
t.fillcolor("#424242")
t.pensize(4)
# Left Eye
go(-70,45)
t.seth(-70)
t.begin_fill()
t.circle(20,160)
t.circle(-20,70)
t.circle(20,160)
t.circle(50,105)
t.end_fill()

# Black Ratina
go(-45,70)
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

# Lens
go(-40,75)
t.fillcolor("white")
t.begin_fill()
t.circle(6)
t.end_fill()

# Right Eye
t.fillcolor("#424242")
go(70,25)
t.seth(-120)
t.begin_fill()
t.circle(20,160)
t.circle(50,110)
t.circle(20,160)
t.circle(-20,70)
t.end_fill()

# Black Ratina
go(90,35)
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

# Lens
go(95,40)
t.fillcolor("white")
t.begin_fill()
t.circle(6)
t.end_fill()

# Nose
t.fillcolor("black")
go(20,60)
t.seth(-5)
t.begin_fill()
t.circle(-30,40)
t.circle(-5,90)
t.circle(-20,115)
t.circle(-8,180)
t.end_fill()

go(18,40)
t.seth(-110)
t.pensize(5)
t.forward(5)
t.circle(15,140)
t.circle(15,-140)
t.circle(-15,140)

# Left Hand
t.fillcolor("#323232")
go(-100,-5)
t.seth(-125)
t.begin_fill()
t.forward(40)
t.circle(50,123)
t.forward(50)
t.circle(-10,30)
t.circle(20,120)
t.circle(45,120)
t.circle(45,-17)
t.seth(148)
t.circle(-160,25)
t.end_fill()

# Right Hand
go(150,-30)
t.seth(-39)
t.begin_fill()
t.circle(-55,145)
t.forward(75)
t.circle(10,30)
t.circle(-20,120)
t.circle(-45,100)
t.forward(50)
t.backward(20)
t.seth(19)
t.circle(160,28)
t.end_fill()

t.hideturtle()

turtle.done()
