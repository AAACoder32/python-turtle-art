
import turtle

turtle.Screen().bgcolor("black")

t = turtle.Pen()

t.pencolor("red")
t.pensize(5)

t.seth(45)
t.forward(200)
t.circle(90,170)

t.seth(-125)
t.forward(45)
t.seth(-55)
t.forward(60)
t.seth(-120)
t.forward(80)
t.seth(-70)
t.forward(40)
t.seth(130)
t.forward(50)
t.seth(70)
t.forward(70)
t.seth(130)
t.forward(60)
t.seth(60)
t.forward(40)

t.seth(135)
t.circle(90,180)
t.forward(200)

t.hideturtle()

turtle.done()