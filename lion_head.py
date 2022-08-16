
# AAACoder 🦁 Art

import turtle

turtle.Screen().bgcolor("white")

t = turtle.Turtle()
t.pensize(10)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
go(0,-150)

# Brown Hair
t.fillcolor("#8a4528")
t.seth(60)
t.begin_fill()
t.circle(-280,40)
t.circle(200,180)
t.seth(158)
t.circle(200,180)
t.circle(-280,40)
t.end_fill()

# Left Ears
t.pensize(7)
go(-125,165)
t.fillcolor("#cfac13")
t.seth(0)
t.begin_fill()
t.circle(45)
t.end_fill()

go(-125,185)
t.fillcolor("black")
t.seth(0)
t.begin_fill()
t.circle(25)
t.end_fill()

# Right Ear
go(125,165)
t.fillcolor("#cfac13")
t.seth(0)
t.begin_fill()
t.circle(45)
t.end_fill()

go(125,185)
t.fillcolor("black")
t.seth(0)
t.begin_fill()
t.circle(25)
t.end_fill()

# Head
go(0,20)
t.fillcolor("#cfac13")
t.seth(0)
t.begin_fill()
t.circle(130)
t.end_fill()

# Left Eyes
t.pensize(1)
go(-50,160)
t.seth(-65)
t.fillcolor("black")
t.begin_fill()
t.circle(12,130)
t.circle(30,50)
t.circle(12,130)
t.circle(30,50)
t.end_fill()

t.seth(0)
t.pencolor("white")
t.fillcolor("white")
go(-37,170)
t.begin_fill()
t.circle(7)
t.end_fill()

# Right Eyes
t.pensize(1)
go(25,160)
t.seth(-65)
t.pencolor("black")
t.fillcolor("black")
t.begin_fill()
t.circle(12,130)
t.circle(30,50)
t.circle(12,130)
t.circle(30,50)
t.end_fill()

t.seth(0)
t.pencolor("white")
t.fillcolor("white")
go(37,170)
t.begin_fill()
t.circle(7)
t.end_fill()

# Mouth
go(0,-10)
t.pensize(6)
t.pencolor("black")
t.fillcolor("#edd6ce")
t.begin_fill()
t.circle(80,60)
t.circle(50,60)
t.circle(80,120)
t.circle(50,60)
t.circle(80,60)
t.end_fill()

# Nose
go(-5,130)
t.fillcolor("black")
t.begin_fill()
t.forward(20)
t.circle(-10,130)
t.circle(-40,30)
t.circle(-20,40)
t.circle(-40,30)
t.circle(-10,130)
t.forward(20)
t.end_fill()

go(0,100)
t.seth(-90)
t.pensize(7)
t.forward(50)
t.seth(0)
t.pensize(12)
t.circle(30,50)
t.circle(30,-100)

# Moustache
t.pensize(6)
t.seth(20)
go(40,70)
t.forward(110)

t.seth(0)
go(40,50)
t.forward(120)

t.seth(-20)
go(40,30)
t.forward(110)

t.seth(160)
go(-40,70)
t.forward(110)

t.seth(180)
go(-40,50)
t.forward(120)

t.seth(-160)
go(-40,30)
t.forward(110)

t.hideturtle()

turtle.done()