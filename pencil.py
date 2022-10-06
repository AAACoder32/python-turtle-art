
# AAACoder Pencil Logo Art
import turtle as tu

tu.Screen().bgcolor("white")

t = tu.Turtle()

# Pencil colors
p_o = "#f27f33"
p_yo = "#f0a42b"

# Nib colors
cl_1 = "#f7d06d"
cl_2 = "#ffe9b3"
cl_3 = "#f9f0df"

# leaf colours
st_cl = "#141f0e"
f_cl = "#49ab11"

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
t.pensize(9)

# Main Pencil
go(0,-150)
t.seth(50)
t.fillcolor(p_o)

t.begin_fill()
t.forward(120)
t.seth(90)
t.forward(180)
t.circle(60,90)
t.forward(34)
t.circle(60,90)
t.forward(180)
t.seth(-50)
t.forward(120)
t.end_fill()

# 1st
t.seth(50)
t.begin_fill()
t.forward(120)
t.seth(110)
t.circle(35,100)
t.pencolor(cl_1)
t.fillcolor(cl_1)
t.pensize(1)
t.seth(-105)
t.forward(110)
t.end_fill()

# 2nd
t.begin_fill()
t.backward(110)
t.pencolor("black")
t.pensize(9)
t.seth(130)
t.circle(35,100)
t.pencolor(cl_2)
t.fillcolor(cl_2)
t.pensize(1)
t.seth(-77)
t.forward(110)
t.end_fill()

# 3rd
t.begin_fill()
t.backward(110)
t.pencolor("black")
t.pensize(9)
t.seth(150)
t.circle(35,100)
t.fillcolor(cl_3)
t.seth(-51)
t.forward(120)
t.end_fill()

# Pencil nib
t.fillcolor("black")
go(0,-150)
t.seth(50)
t.begin_fill()
t.forward(30)
t.seth(120)
t.circle(22.5,120)
t.seth(-50)
t.forward(30)
t.end_fill()

# Orange- yellow stripe
t.pencolor(p_yo)
t.fillcolor(p_yo)
t.seth(0)
t.pensize(1)
go(-65,-25)

t.begin_fill()
t.seth(30)
t.circle(-30,60)
t.seth(90)
t.forward(145)
t.circle(-50,70)
t.seth(180)
t.circle(62,90)
t.forward(130)
t.end_fill()



def leaf(len,ang=0):    
    t.seth(ang)
    t.circle(len,80)
    t.seth(180+ang)
    t.circle(len,80)

go(0,195)
t.pensize(7)
t.pencolor(st_cl)
t.fillcolor(f_cl)
t.begin_fill()
leaf(80,5)
t.end_fill()

go(-10,195)
t.begin_fill()
leaf(60,100)
t.end_fill()

t.ht()

tu.done()