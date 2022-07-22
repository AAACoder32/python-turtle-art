# Cute cat 🐈
import turtle
import colorsys

turtle.Screen().bgcolor("white")

t = turtle.Pen()

def go(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# Line 
go(-250,-100)

t.pensize(9)
t.forward(500)
t.backward(90)

t.seth(60)
t.pensize(5)
t.circle(180,240)

# Black dharia

t.fillcolor("#282929")
go(160,-100)
t.seth(60)
t.circle(180,55)

t.begin_fill()
t.seth(60)
t.forward(50)
t.circle(150,30)
t.circle(20,100)
t.circle(150,44)

t.seth(150)
t.circle(180,80)

t.seth(160)
t.forward(30)
t.circle(150,30)
t.circle(20,100)
t.circle(150,46)

t.seth(-95)
t.pensize(1)
t.circle(180,10)
t.seth(-15)
t.circle(120,80)

t.seth(-55)
t.circle(120,118)

t.end_fill()

# Left eye
go(-70,20)

t.fillcolor("black")
t.begin_fill()
t.circle(30)
t.end_fill()

go(-80,40)

t.fillcolor("white")
t.begin_fill()
t.circle(8)
t.end_fill()

# Right Eye
go(70,40)

t.fillcolor("black")
t.begin_fill()
t.circle(30)
t.end_fill()

go(60,60)

t.fillcolor("white")
t.begin_fill()
t.circle(8)
t.end_fill()

# Nose
go(-48,10)
t.pensize(5)
t.seth(-90)

t.fillcolor("black")

t.begin_fill()
t.circle(10,70)
t.circle(20,70)
t.circle(10,70)
t.circle(5,70)
t.forward(20)
t.circle(6,70)
t.end_fill()

# Mouth 
go(-30,0)
t.seth(-80)
t.forward(5)

t.fillcolor("#fa9393")
t.begin_fill()
t.circle(20,140)
t.circle(20,-140)
t.circle(-20,140)
t.circle(-20,-50)
t.seth(-80)
t.circle(20,180)
t.seth(190)
t.circle(-20,60)
t.end_fill()

# Left paw
go(-120,-95)
t.seth(-30)
t.fillcolor("white")
t.begin_fill()
t.circle(20,150)
t.circle(50,80)
t.circle(30,70)
t.forward(22)
t.end_fill()

go(-160,-90)
t.begin_fill()
t.circle(15,200)
t.end_fill()

t.seth(70)
t.begin_fill()
t.circle(-10,-220)
t.end_fill()

# Right paw
go(180,-97)
t.seth(75)
t.begin_fill()
t.circle(120,30)
t.seth(80)
t.circle(120,10)
t.circle(30,40)
t.seth(90)
t.circle(10,120)
t.seth(100)
t.circle(10,120)
t.seth(120)
t.circle(15,120)
t.seth(150)
t.circle(15,150)
t.seth(-120)
t.circle(40,50)
t.circle(-60,30)
t.circle(80,21)
t.end_fill()

go(130,-40)
t.seth(5)

t.pensize(1)
t.pencolor("#fa9393")
t.fillcolor("#fa9393")

t.begin_fill()
t.forward(20)
t.circle(8,90)
t.circle(20,170)
t.circle(10,105)
t.end_fill()

go(165,-15)
t.begin_fill()
t.circle(6)
t.end_fill()

go(150,-2)
t.begin_fill()
t.circle(7)
t.end_fill()

go(130,0)
t.begin_fill()
t.circle(7)
t.end_fill()

go(110,-15)
t.begin_fill()
t.circle(9)
t.end_fill()

# Ear red
go(160,100)
t.seth(45)
t.begin_fill()
t.circle(80,50)
t.circle(10,90)
t.circle(80,50)
t.seth(-25)
t.circle(-120,28)
t.end_fill()

go(-150,90)
t.seth(150)
t.begin_fill()
t.circle(80,50)
t.circle(10,90)
t.circle(80,50)
t.seth(80)
t.circle(-120,28)
t.end_fill()

t.hideturtle()

turtle.done()