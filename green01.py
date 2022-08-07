

# AAACoder Art

import turtle

turtle.Screen().bgcolor("white")

t = turtle.Turtle()
t.pensize(7)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
# Right Feather
t.fillcolor("#2cdb1d")
go(120,-100)
t.seth(35)
t.begin_fill()
t.circle(140,80)
t.circle(40,122)
t.circle(140,80)
t.end_fill()

# Main Body
t.fillcolor("#9cf71b")
go(-100,-70)
t.seth(-23)

t.begin_fill()
t.circle(220,40)
t.circle(120,60)
t.circle(220,50)
t.circle(120,90)
t.circle(220,55)
t.circle(120,60)
t.end_fill()

# Left Feather
t.fillcolor("#2cdb1d")
go(-160,-110)
t.seth(30)
t.begin_fill()
t.circle(140,80)
t.circle(40,122)
t.circle(140,80)
t.end_fill()

# Left Leg
go(-70,-85)
t.pensize(16)
t.seth(-85)
t.forward(60)
t.seth(-150)
t.forward(50)
t.backward(50)
t.seth(-95)
t.forward(40)
t.backward(40)
t.seth(-40)
t.forward(45)

# Right Leg
go(50,-85)
t.pensize(16)
t.seth(-80)
t.forward(60)
t.seth(-150)
t.forward(50)
t.backward(50)
t.seth(-95)
t.forward(40)
t.backward(40)
t.seth(-40)
t.forward(45)

# Left Eye
t.fillcolor("black")
t.pensize(7)
go(-90,120)
t.seth(-30)

t.begin_fill()
t.circle(50,60)
t.circle(20,120)
t.circle(50,60)
t.circle(20,120)
t.circle(50,30)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.circle(50,30)
t.circle(20,120)
t.circle(50,30)
t.end_fill()


# Right Eye
t.fillcolor("black")
t.pensize(7)
go(30,120)
t.seth(-30)

t.begin_fill()
t.circle(50,60)
t.circle(20,120)
t.circle(50,60)
t.circle(20,120)
t.circle(50,30)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.circle(50,30)
t.circle(20,120)
t.circle(50,30)
t.end_fill()

# Chonch
t.fillcolor("#f71b4b")
go(-30,100)
t.seth(-95)
t.begin_fill()
t.forward(50)
t.seth(40)
t.forward(55)
t.seth(120)
t.circle(31,80)
t.end_fill()

t.hideturtle()

turtle.done()