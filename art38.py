
import turtle

s = turtle.Screen()
s.bgcolor("white")

t = turtle.Pen()
t.pensize(8)

t.fillcolor("#9e9e9e")

t.pu()
t.goto(0,-100)
t.pd()

# Main head
t.begin_fill()
t.circle(180)
t.end_fill()

t.pu()
t.goto(115,-60)
t.seth(46)
t.pd()

# Long nose
t.begin_fill()
t.fd(290)
t.seth(195)
t.fd(390)
t.end_fill()
    
t.pu()
t.home()
t.goto(62,-40)
t.pd()
t.seth(60)
t.pensize(3)

# Mouth

t.fillcolor("white")

t.begin_fill()
for i in range(56):
    
    if i==0:
        t.circle(50,100)
        t.seth(180)
    t.lt(2.2)
    t.fd(2)
t.end_fill()

t.pu()
t.home()
t.goto(60,-40)
t.pd()
t.seth(60)
t.pensize(3)

t.fillcolor("#9e9e9e")

t.begin_fill()
for i in range(42):
    if i==0:
        t.circle(30,90)
        t.seth(180)
    t.lt(2)
    t.fd(2)
t.end_fill()

# Left eye

t.pu()
t.home()
t.goto(-49,70)
t.pencolor("white")
t.pd()

t.fillcolor("white")
t.begin_fill()
t.circle(30)
t.end_fill()

t.pu()
t.goto(-49,90)
t.pd()

t.fillcolor("black")
t.begin_fill()
t.circle(13)
t.end_fill()

# Right eye

t.pu()
t.home()
t.goto(49,100)
t.pencolor("white")
t.pd()

t.fillcolor("white")
t.begin_fill()
t.circle(30)
t.end_fill()

t.pu()
t.goto(49,120)
t.pd()

t.fillcolor("black")
t.begin_fill()
t.circle(13)
t.end_fill()

# Right Eyebrow
t.pensize(10)
t.pencolor("black")

t.pu()
t.goto(10,120)
t.seth(70)
t.pd()
t.fd(100)

# Left eyebrow
t.pu()
t.goto(-10,120)
t.seth(160)
t.pd()
t.fd(100)

turtle.done()