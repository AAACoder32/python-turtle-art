
import turtle

turtle.Screen().bgcolor("white")

t = turtle.Pen()

t.pencolor("black")
t.fillcolor("#ede18e")

# Main Khopadi

t.penup()
t.goto(-40,-200)
t.pendown()

t.begin_fill()
t.forward(80)
t.circle(150,100)

t.seth(0)
t.circle(40,180)

t.seth(90)
t.circle(150,90)

t.forward(80)

t.seth(180)
t.circle(150,90)

t.seth(180)
t.circle(40,180)

t.seth(-100)
t.circle(150,100)
t.forward(10)

t.end_fill()

# Baal tere stylish 
t.fillcolor("black")
t.penup()
t.goto(-170,20)
t.pendown()

t.begin_fill()
t.seth(90)
t.forward(40)
t.circle(-150,35)
t.circle(-20,120)

t.seth(-30)
t.circle(230,60)
t.circle(-20,90)
t.circle(-140,35)

t.forward(20)

t.seth(45)
t.circle(-80,30)
t.seth(70)
t.circle(100,100)

t.seth(120)
t.circle(200,80)
t.seth(-50)
t.circle(30,60)

t.seth(-150)
t.circle(-60,60)
t.seth(-120)
t.circle(60,60)
t.seth(-150)
t.circle(120,106)
t.seth(90)
t.forward(10)

t.end_fill()

# Aankh Mare Re Babua

# Right Eye
t.penup()
t.goto(70,5)
t.pendown()

t.fillcolor("white")
t.seth(5)

t.begin_fill()
t.forward(60)
t.circle(20,90)
t.circle(45,190)
t.circle(16,80)

t.end_fill()
t.penup()
t.goto(105,10)
t.pendown()

t.fillcolor("#2d8aa8")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(105,30)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(60,40)
t.pendown()

t.seth(40)

t.fillcolor("#7d6c65")

t.begin_fill()
t.circle(-80,60)
t.seth(110)
t.circle(40,160)
t.end_fill()

# Left Eye
t.penup()
t.goto(-140,5)
t.pendown()

t.fillcolor("white")
t.seth(-5)

t.begin_fill()
t.forward(60)
t.circle(20,90)
t.circle(45,190)
t.circle(16,80)
t.end_fill()

t.penup()
t.goto(-105,5)
t.pendown()

t.fillcolor("#2d8aa8")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-105,25)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-63,40)
t.pendown()

t.seth(150)

t.fillcolor("#7d6c65")

t.begin_fill()
t.circle(80,60)
t.seth(80)
t.circle(-40,160)
t.end_fill()

# Naak Tere cute
t.penup()
t.goto(-30,-50)
t.pendown()
t.seth(0)

t.fillcolor("#d9754a")

t.begin_fill()
t.forward(60)
t.seth(-110)
t.circle(-31,140)
t.end_fill()

# Moonh
t.penup()
t.goto(-50,-100)
t.pendown()
t.seth(0)

t.fillcolor("#805e38")
t.begin_fill()
t.forward(100)
t.circle(-10,135)
t.circle(-80,90)
t.circle(-10,140)
t.end_fill()

t.hideturtle()

turtle.done()