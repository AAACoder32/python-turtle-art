
import turtle

turtle.Screen().bgcolor("#14153d")

t = turtle.Pen()
t.pencolor("#de4baf")
t.pensize(3)
t.fillcolor("#de4baf")
t.speed(0)

# Main Body
t.begin_fill()
t.forward(100)
t.circle(100,90)
t.circle(200,180)
t.circle(100,90)
t.forward(100)
t.end_fill()

#----*********-------#
t.penup()
t.goto(-100,0)
t.seth(-90)
t.pendown()
#----*********-------#

# Tails
t.fillcolor("#de4baf")
t.begin_fill()
t.forward(60)
t.circle(-15,180)
t.forward(20)
t.circle(15,180)
t.forward(20)
t.circle(45,180)
t.forward(60)

#----*********-------#
t.penup()
t.goto(-40,0)
t.seth(-90)
t.pendown()
#----*********-------#

t.forward(150)
t.circle(-15,180)
t.forward(20)
t.circle(15,180)
t.forward(20)
t.circle(45,180)
t.forward(150)

#----*********-------#
t.penup()
t.goto(20,0)
t.seth(-90)
t.pendown()
#----*********-------#

t.forward(150)
t.circle(45,180)
t.forward(20)
t.circle(15,180)
t.forward(20)
t.circle(-15,180)
t.forward(150)

#----*********-------#
t.penup()
t.goto(80,0)
t.seth(-90)
t.pendown()
#----*********-------#

t.forward(60)
t.circle(45,180)
t.forward(20)
t.circle(15,180)
t.forward(20)
t.circle(-15,180)
t.forward(60)

t.end_fill()

#----*********-------#
t.penup()
t.goto(60,120)
t.pendown()
#----*********-------#

#Eye
t.pencolor("black")
t.fillcolor("white")
t.begin_fill()
t.circle(60)
t.end_fill()

#----*********-------#
t.penup()
t.goto(40,120)
t.pendown()
#----*********-------#

t.fillcolor("black")
t.begin_fill()
t.circle(40)
t.end_fill()

#----*********-------#
t.penup()
t.goto(80,280)
t.pendown()
#----*********-------#

# Ear
t.pencolor("#de4baf")
t.fillcolor("#de4baf")
t.pensize(8)
t.circle(-120,60)
t.begin_fill()
t.circle(-20)
t.end_fill()

#----*********-------#
t.penup()
t.goto(-80,280)
t.pendown()
#----*********-------#

t.seth(90)
t.circle(120,60)
t.begin_fill()
t.circle(20)
t.end_fill()

turtle.done()
