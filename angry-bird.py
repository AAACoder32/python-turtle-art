
# AAACoder Angry Bird Art
import turtle as tu

tu.Screen().bgcolor("white")

t = tu.Turtle()
t.pensize(9)
#t.speed(0)

red_color = "#cc3333"
mb_color = "#ffeccf"
upper_chonch_cl = "#f5bc14"
lower_chonch_cl = "#db9b0f"

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# Main body
go(-170,-250)
t.seth(-30)

t.fillcolor(red_color)

t.begin_fill()
t.circle(320,60)
t.circle(220,30)
t.circle(60,10)
t.circle(300,80)
t.seth(110)
t.circle(200,40)
t.circle(30,150)
t.circle(90,40)
t.seth(140)
t.circle(200,40)
t.circle(30,150)
t.circle(90,40)
t.seth(200)
t.circle(300,60)
t.circle(235,65)
t.end_fill()

# Light brown area
go(-170,-250)
t.seth(-30)

t.fillcolor(mb_color)

t.begin_fill()
t.circle(315,65)
t.seth(114)
t.circle(200,129)
t.seth(-55)
t.circle(90,30)
t.end_fill()

# Eyes

def big_wc():
    t.pensize(9)
    t.pencolor("black")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

def small_bc():
    t.pensize(2)
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    t.circle(13)
    t.end_fill()

def small_wc():
    t.pensize(1)
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(4)
    t.end_fill()
    
# Left eye
t.seth(0)
go(-50,-80)
big_wc()
go(-35,-50)
small_bc()
go(-47,-40)
small_wc()

# Right Eye
t.seth(0)
go(30,-80)
big_wc()
go(20,-50)
small_bc()
go(9,-40)
small_wc()

# Eyebrow
t.pensize(9)
go(-10,-30)
t.pencolor("black")
t.fillcolor("black")
t.seth(20)
t.begin_fill()
t.forward(120)
t.seth(100)
t.forward(30)
t.seth(-155)
t.forward(120)
t.seth(155)
t.forward(120)
t.seth(-112)
t.forward(30)
t.seth(-20)
t.forward(125)
t.end_fill()

# Upper Chonch
t.pensize(5)
t.seth(-25)
go(-70,-140)

t.fillcolor(upper_chonch_cl)

t.begin_fill()
t.forward(70)
t.seth(25)
t.forward(70)
t.circle(10,80)
t.circle(120,50)
t.circle(10,50)
t.circle(120,50)
t.circle(10,80)
t.end_fill()

# Lower Chonch
t.seth(-25)
go(-70,-140)

t.fillcolor(lower_chonch_cl)

t.begin_fill()
t.forward(70)
t.seth(25)
t.forward(70)
t.seth(-100)
t.circle(-90,60)
t.circle(-10,40)
t.circle(-100,55)
t.end_fill()

t.hideturtle()

tu.done()