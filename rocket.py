# Import turtle library 
import turtle

s = turtle.Screen()
s.bgcolor("black")

t = turtle.Pen()
t.pencolor("red")
t.pensize(2)

t.penup()
t.goto(-60,-150)
t.pendown()

# Main body
t.fillcolor("red")
t.begin_fill()
t.forward(105)
t.setheading(60)
t.circle(500,68)
t.setheading(229)
t.circle(502,68)
t.end_fill()

t.penup()
t.goto(-57,-160)
t.setheading(0)
t.pendown()

# Down Nozzle
t.begin_fill()
t.forward(100)
t.setheading(-70)
t.forward(100)
t.setheading(180)
t.forward(170)
t.setheading(70)
t.forward(101)
t.end_fill()

t.penup()
t.goto(0,180)
t.setheading(0)
t.pendown()

# White circle 
t.fillcolor("white")
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(110,-60)
t.setheading(-40)
t.pendown()

#Right propeller 
t.fillcolor("red")
t.begin_fill()
t.forward(90)
t.setheading(-95)
t.forward(190)
t.setheading(-180)
t.forward(40)
t.setheading(92)
t.forward(140)
t.setheading(130)
t.forward(60)
t.setheading(63)
t.forward(70)
t.end_fill()

# Left propeller 
t.penup()
t.goto(-120,-62)
t.setheading(210)
t.pendown()

t.begin_fill()
t.forward(90)
t.setheading(-85)
t.forward(200)
t.setheading(0)
t.forward(40)
t.setheading(86)
t.forward(140)
t.setheading(45)
t.forward(60)
t.setheading(118)
t.forward(71)
t.end_fill()

t.hideturtle()
turtle.done()