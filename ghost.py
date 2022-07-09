
import turtle

turtle.Screen().bgcolor("white")

t = turtle.Pen()
t.pencolor("#7d7e80")
t.fillcolor("#c0c1c2")
t.pensize(15)

t.penup()
t.goto(-150,-100)
t.pendown()

# Main Body 

#----------***********------------#
t.begin_fill()
t.seth(40)
t.circle(-100,80)
t.circle(60,80)
t.circle(-100,80)
t.seth(100)
t.forward(250)
t.seth(10)
t.circle(180,60)
t.seth(-130)
t.circle(-90,60)
t.forward(60)
t.seth(90)
t.circle(120,180)

t.penup()
t.goto(-150,-100)
t.pendown()

t.seth(81)
t.forward(250)
t.seth(0)
t.circle(180,-60)
t.seth(-45)
t.circle(90,60)
t.forward(75)
t.end_fill()
#----------***********------------#

# Mouth 

#----------***********------------#
t.penup()
t.seth(-30)
t.goto(-70,200)
t.pendown()

t.pensize(2)
t.fillcolor("black")
t.begin_fill()
t.circle(180,60)
t.seth(-100)
t.circle(-90,160)
t.end_fill()
#----------***********------------#

# Tongue

#----------***********------------#
t.penup()
t.seth(-90)
t.goto(-10,160)
t.pendown()

t.pensize(8)
t.pencolor("#eb1e36")
t.fillcolor("#f2465a")

t.begin_fill()
t.forward(50)
t.circle(30,90)
t.forward(10)
t.circle(30,90)
t.forward(50)
t.end_fill()

t.penup()
t.seth(-90)
t.goto(25,160)
t.pendown()
t.forward(40)
#----------***********------------#

# Eye

#----------***********------------#
t.penup()
t.goto(30,260)
t.pendown()

t.pencolor("#7d7e80")
t.fillcolor("white")
t.begin_fill()
t.circle(40)
t.end_fill()

t.pencolor("black")
t.penup()
t.goto(55,260)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(15)
t.end_fill()

t.pensize(15)
t.penup()
t.goto(-15,260)
t.seth(140)
t.pendown()

t.circle(35,90)

t.penup()
t.goto(-15,260)
t.seth(105)
t.pendown()

t.circle(35,90)

turtle.done()
