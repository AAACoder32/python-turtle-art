
# AAACoder Art

import turtle

turtle.Screen().bgcolor("white")

t = turtle.Turtle()
t.pensize(7)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
# Main Body
t.fillcolor("#dcf53b")
go(-150,-70)
t.seth(-30)

t.begin_fill()
t.circle(220,130)
t.circle(120,180)
t.circle(-120,110)
t.seth(-52)
t.circle(220,30)
t.end_fill()

# Feather
t.fillcolor("#9cf71b")
go(-100,90)
t.seth(160)
t.begin_fill()
t.circle(-25,180)
t.circle(-120,60)
t.circle(-40,60)
t.circle(-120,60)
t.circle(-30,180)
t.seth(180)
t.circle(-50,45)
t.circle(-30,190)
t.end_fill()

# Eye
t.fillcolor("#1c0508")
t.pencolor("#1c0508")
t.pensize(7)
go(60,200)
t.seth(-180)

t.begin_fill()
t.circle(35)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.circle(35,180)
t.end_fill()

# Foot
go(-30,-100)
t.seth(-80)
t.pensize(10)
t.circle(-90,40)

go(30,-90)
t.seth(-80)
t.pensize(10)
t.circle(-120,35)

# Chonch
go(180,170)
t.seth(15)
t.circle(60,30)
go(180,160)
t.seth(-15)
t.circle(-50,40)

t.hideturtle()
turtle.done()