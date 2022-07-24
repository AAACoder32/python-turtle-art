
import turtle

s = turtle.Screen()
s.bgcolor("white")

t = turtle.Pen()
t.pensize(8)

t.fillcolor("#9e9e9e")
t.penup()
t.goto(0,-100)
t.pendown()

# Main head
t.begin_fill()
t.circle(180)
t.end_fill()

t.penup()
t.goto(115,-60)
t.setheading(46)
t.pendown()

# Long nose
t.begin_fill()
t.forward(290)
t.setheading(195)
t.forward(390)
t.end_fill()

t.penup()
t.goto(62,-40)
t.pendown()
t.setheading(60)
t.pensize(3)

# Mouth
t.fillcolor("white")
t.begin_fill()
for i in range(56):
    if i==0:
        t.circle(50,100)
        t.setheading(180)
    t.left(2.2)
    t.forward(2)
t.end_fill()

t.penup()
t.goto(60,-40)
t.pendown()

t.setheading(60)
t.pensize(3)
t.fillcolor("#9e9e9e")

t.begin_fill()

for i in range(42):
    if i==0:
        t.circle(30,90)
        t.setheading(180)
    t.left(2)
    t.forward(2)
t.end_fill()

# Left eye
t.penup()
t.goto(-69,100)
t.pencolor("white")
t.pendown()

t.fillcolor("white")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-49,100)
t.fillcolor("black")
t.begin_fill()
t.circle(13)
t.end_fill()

# Right eye
t.penup()
t.goto(29,120)
t.pencolor("white")
t.pendown()

t.fillcolor("white")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(39,120)
t.fillcolor("black")
t.begin_fill()
t.circle(13)
t.end_fill()

# Right Eyebrow
t.pensize(10)
t.pencolor("black")
t.penup()
t.goto(15,120)
t.setheading(70)
t.pendown()
t.forward(100)

# Left Eyebrow
t.penup()
t.goto(-10,120)
t.setheading(160)
t.pendown()
t.forward(100)


turtle.done()