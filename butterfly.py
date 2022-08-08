
# AAACoder Cute Butterfly 🦋 Art
import turtle

turtle.Screen().bgcolor("white")

t = turtle.Turtle()
t.pensize(4)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
# Left down feather

go(-130,-50)
t.seth(-130)

t.fillcolor("red")

t.begin_fill()
t.circle(130,90)
t.circle(40,80)
t.circle(200,50)
t.end_fill()

go(-110,-50)
t.seth(-130)

t.fillcolor("#ebc173")

t.begin_fill()
t.circle(120,80)
t.circle(50,90)
t.circle(180,50)
t.end_fill()

# Right down feather

go(140,-50)
t.seth(-50)

t.fillcolor("red")

t.begin_fill()
t.circle(-130,90)
t.circle(-40,80)
t.circle(-200,50)
t.end_fill()

go(120,-50)
t.seth(-50)

t.fillcolor("#ebc173")

t.begin_fill()
t.circle(-120,80)
t.circle(-50,90)
t.circle(-180,50)
t.end_fill()

# Right Upper Feather
go(0,-70)
t.fillcolor("red")
t.seth(-20)
t.begin_fill()
t.circle(220,45)
t.circle(50,60)
t.circle(-120,40)
t.circle(50,160)
t.circle(250,60)
t.end_fill()

go(150,90)
t.seth(-150)
t.fillcolor("#ebc173")
t.begin_fill()
t.circle(90,40)
t.circle(30,140)
t.circle(90,40)
t.circle(30,140)
t.end_fill()

go(145,70)
t.seth(-150)
t.fillcolor("red")
t.begin_fill()
t.circle(40,40)
t.circle(20,140)
t.circle(40,40)
t.circle(20,140)
t.end_fill()

# Left Upper Feather
go(10,-75)
t.fillcolor("red")
t.seth(-160)
t.begin_fill()
t.circle(-220,45)
t.circle(-50,60)
t.circle(120,40)
t.circle(-50,160)
t.circle(-250,60)
t.end_fill()

go(-150,90)
t.seth(-30)
t.fillcolor("#ebc173")
t.begin_fill()
t.circle(-90,40)
t.circle(-30,140)
t.circle(-90,40)
t.circle(-30,140)
t.end_fill()

go(-145,75)
t.seth(-30)
t.fillcolor("red")
t.begin_fill()
t.circle(-40,40)
t.circle(-20,140)
t.circle(-40,40)
t.circle(-20,140)
t.end_fill()

# Body
t.fillcolor("#ebc173")
go(-20,-80)
t.seth(-120)
t.begin_fill()
t.circle(90,70)
t.circle(-70,40)
t.seth(90)
t.circle(-70,40)
t.circle(90,70)
t.end_fill()

# Head
t.fillcolor("red")
go(-13,-90)
t.seth(-27)
t.begin_fill()
t.circle(40,60)
t.circle(30,120)
t.circle(40,60)
t.circle(30,120)
t.end_fill()

go(-10,-30)
t.seth(-27)
t.begin_fill()
t.circle(30,60)
t.circle(20,120)
t.circle(30,60)
t.circle(20,120)
t.end_fill()

# Eyes
t.fillcolor("white")

# Left Eye
go(10,30)
t.seth(-120)
t.begin_fill()
t.circle(30,60)
t.circle(15,120)
t.circle(30,60)
t.circle(15,120)
t.end_fill()

t.fillcolor("black")
go(20,20)
t.begin_fill()
t.circle(8)
t.end_fill()

t.pencolor("white")
t.fillcolor("white")
go(18,18)
t.begin_fill()
t.circle(3)
t.end_fill()

# Right Eye
t.pencolor("black")
go(-25,30)
t.seth(-120)
t.begin_fill()
t.circle(30,60)
t.circle(18,120)
t.circle(30,60)
t.circle(18,120)
t.end_fill()

t.fillcolor("black")
go(-15,20)
t.begin_fill()
t.circle(10)
t.end_fill()

t.pencolor("white")
t.fillcolor("white")
go(-15,12)
t.begin_fill()
t.circle(4)
t.end_fill()

# Antena
t.pencolor("black")
go(6,30)
t.seth(90)
t.circle(60,50)
t.circle(10,180)
t.circle(5,160)

go(10,30)
t.seth(80)
t.circle(-60,55)
t.circle(-10,180)
t.circle(-5,160)

t.hideturtle()

turtle.done()
