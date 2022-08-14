
# AAACoder Art
import turtle

turtle.Screen().bgcolor("black")

t = turtle.Pen()
t.pensize(3)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# Orange Strip 
t.goto(0,-150)
t.seth(13)
t.circle(420,30)
t.circle(120,50)
t.pencolor("orange")
t.fillcolor("orange")
t.begin_fill()
t.circle(120,150)
t.seth(116)
t.circle(120,150)
t.seth(-20)
t.circle(320,40)
t.circle(-320,43)
t.end_fill()

# White Strip 
go(0,-150)
t.seth(13)

t.pencolor("black")
t.circle(420,30)

t.pencolor("white")
t.fillcolor("white")

t.begin_fill()
t.circle(120,48)
t.seth(157)
t.circle(320,43)
t.circle(-320,40)
t.seth(-94)
t.circle(120,60)
t.seth(-20)
t.circle(320,40)
t.circle(-320,27)
t.end_fill()

# Green Strip
go(0,-150)
t.seth(13)
t.pencolor("green")
t.fillcolor("green")

t.begin_fill()
t.circle(420,31)
t.seth(173)
t.circle(320,27)
t.circle(-320,41)
t.seth(-41)
t.circle(420,28)
t.end_fill()

# Chakra
go(10,-48)
t.pencolor("navy")
t.fillcolor("navy")
t.seth(0)
t.pensize(3)

t.circle(45)

t.pendown()

go(10,-4)
t.pensize(2)

for i in range(24):
    t.forward(42)
    t.backward(42)
    t.left(15)

t.hideturtle()

turtle.done()