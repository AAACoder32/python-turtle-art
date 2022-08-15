
# AAACoder Art
import turtle

turtle.Screen().bgcolor("#E6F3FA")

t = turtle.Turtle()

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
go(0,-100)
t.pensize(20)
t.pencolor("navy")
t.circle(150)

go(-20,190)
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(37)
    t.right(15)
    t.pendown()
    
go(0,50)
t.pensize(5)

for i in range(24):
    t.forward(150)
    t.backward(150)
    t.left(15)
    
# Kesariya Colour
t.pencolor("orange")
t.fillcolor("orange")
go(-350,300)
t.seth(-20)
t.begin_fill()
t.forward(100)
t.circle(30,70)
t.circle(-290,100)
t.circle(-10,90)
t.circle(-20,90)
t.circle(120,80)
t.circle(10,150)
t.circle(-100,50)
t.circle(-20,90)
t.circle(-10,80)
t.circle(150,80)
t.circle(-180,60)
t.forward(120)
t.seth(90)
t.forward(86)
t.end_fill()

# Green Colour
t.pencolor("green")
t.fillcolor("green")
go(320,-280)
t.seth(150)
t.begin_fill()
t.forward(120)
t.circle(30,70)
t.circle(-290,100)
t.circle(-10,90)
t.circle(-20,90)
t.circle(120,80)
t.circle(10,150)
t.circle(-100,50)
t.circle(-20,90)
t.circle(-10,80)
t.circle(150,80)
t.circle(-180,60)
t.forward(93)
t.seth(-90)
t.forward(98)
t.end_fill()

t.hideturtle()

turtle.done()