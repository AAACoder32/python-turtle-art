
import turtle 

s = turtle.Screen()
s.bgcolor("white")

t = turtle.Pen()
t.pencolor("black")
t.pensize(4)

t.seth(90)
t.pu()
t.goto(160,0)
t.pd()

t.fillcolor("#edb6b2")

# Main body

t.begin_fill()

for i in range(200):
    
    if (i==16 or i==32):
        t.circle(152,80)
        t.lt(10)
        
    elif i>=120 and i<124:
        t.circle(40,180)
        t.fd(25)
        t.bk(25)
        t.seth(-90)
        if i==123:
            t.seth(90)
    else:
        t.fd(3)
t.end_fill()

# Left hand

t.pu()
t.home()
t.goto(-116,-50)
t.seth(-45)
t.pd()
t.fd(30)
t.circle(30,180)
t.fd(30)

# Right Hand
t.pu()
t.home()
t.goto(74,-5)
t.seth(-135)
t.pd()
t.fd(30)
t.circle(30,180)
t.fd(30)

# Goto home position
t.pu()
t.home()
t.goto(74,70)
t.seth(0)
t.pd()

# Right Eye

t.fillcolor("black")
t.begin_fill()
t.circle(25)
t.end_fill()

t.lt(50)
t.fd(30)
t.fillcolor("white")
t.begin_fill()
t.circle(15)
t.end_fill()

# Goto home position
t.pu()
t.home()
t.goto(-74,70)
t.seth(0)
t.pd()

# Left Eye
t.fillcolor("black")
t.begin_fill()
t.circle(25)
t.end_fill()

t.lt(50)
t.fd(30)
t.fillcolor("white")
t.begin_fill()
t.circle(15)
t.end_fill()

# Goto home position
t.pu()
t.home()
t.goto(-30,30)
t.seth(0)
t.pd()

# Mouth
t.seth(-45)
t.circle(50,90)

t.hideturtle()

turtle.done()