
import turtle

cl_wh = 'white'
cl_bl = '#03a5fc'

t = turtle.Pen()
turtle.bgcolor(cl_bl)

t.pencolor(cl_wh)
t.fillcolor(cl_wh)
t.goto(0,-50)
t.begin_fill()
t.circle(100)
t.end_fill()


t.pencolor(cl_bl)
t.fillcolor(cl_bl)
t.penup()
t.home()
t.goto(-32,0)
t.begin_fill()
t.pendown()
t.left(90)
t.fd(90)
t.right(120)
t.fd(90)
t.right(120)
t.fd(90)
t.end_fill()

#This code for M letter
t.penup()
t.home()
t.goto(-150,-90)
t.pencolor(cl_wh)
t.pensize(12)
t.right(90)
t.fd(50)
t.pendown()
t.seth(90)
t.fd(50)
t.right(135)
t.fd(35)
t.right(-90)
t.fd(35)
t.right(135)
t.fd(50)
t.penup()

#This code for X letter
t.seth(0)
#t.right(90)
#t.fd(12)
t.left(90)
t.fd(50)
t.right(90)
t.fd(20)
t.pendown()
t.right(55)
t.fd(60)
t.penup()
t.right(125)
t.fd(34)
t.pendown()
t.right(125)
t.fd(58)

#This code for letter P
t.penup()
t.right(45)
t.fd(15)
t.seth(0)
t.right(90)
t.fd(55)
t.pensize(4)
t.left(180)
t.pendown()
t.fd(55)
t.backward(33)
t.right(90)
t.fd(5)
t.circle(18,180)
t.fd(5)
t.penup()

# This code for L letter
t.seth(0)
t.fd(30)
t.right(90)
t.pendown()
t.fd(55)
t.left(90)
t.fd(27)
t.penup()

# This code for A letter
t.fd(10)
t.left(70)
t.pendown()
t.fd(60)
t.right(140)
t.fd(60)
t.bk(24)
t.right(110)
t.fd(25)
t.bk(25)
t.seth(0)

# This code for Y letter
t.penup()
t.fd(20)
t.right(90)
t.pendown()
t.fd(23)
t.bk(23)
t.seth(0)
t.left(60)
t.fd(38)
t.bk(38)
t.left(60)
t.fd(38)
t.penup()
t.seth(0)
t.fd(48)

# This code for E letter
t.pendown()
t.right(90)
t.fd(55)
t.left(90)
t.fd(25)
t.bk(25)
t.left(90)
t.fd(25)
t.right(90)
t.fd(23)
t.bk(23)
t.left(90)
t.fd(30)
t.right(90)
t.fd(25)

# This code for R letter
t.penup()
t.fd(13)
t.seth(0)
t.right(90)
t.fd(55)
t.pensize(4)
t.left(180)
t.pendown()
t.fd(55)
t.backward(33)
t.right(90)
t.fd(5)
t.circle(18,180)
t.fd(5)
t.left(90)
t.fd(33)
t.left(45)
t.fd(35)
t.hideturtle()

turtle.done()