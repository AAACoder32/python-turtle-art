
import turtle

turtle.Screen().bgcolor("black")

t = turtle.Turtle()

t.pencolor("red")
t.penup()
t.goto(-350,-40)
t.pendown()

t.write("KARNI",font=("Verdana",45,"normal"))

t.pencolor("#e8c423")
t.fillcolor("#e8c423")

t.penup()
t.goto(210,-30)
t.pendown()

t.begin_fill()
t.forward(40)
t.seth(90)
t.circle(-30,90)
t.circle(50,130)
t.circle(-30,60)
t.circle(-10,180)
t.seth(90)
t.forward(50)
t.seth(-155)
t.circle(60,90)
t.circle(-50,135)

t.seth(90)
t.forward(100)
t.seth(0)
t.forward(15)
t.seth(115)
t.forward(55)
t.seth(-120)
t.forward(55)
t.seth(0)
t.forward(15)
t.seth(-90)
t.forward(100)

t.seth(195)
t.circle(-50,135)
t.circle(50,100)
t.seth(-90)
t.forward(50)
t.circle(10,-190)
t.circle(90,-20)
t.circle(-50,-120)
t.circle(20,-110)
t.end_fill()

t.hideturtle()

turtle.done()
