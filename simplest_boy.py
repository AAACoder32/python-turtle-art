
# AAACoder Simplest Boy Art
import turtle as tu

tu.Screen().bgcolor("#ffacff")
t = tu.Turtle()
h = 0
t.pensize(3)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
#Feet 
go(-70,-100)
t.seth(60)
t.forward(120)
t.seth(-60)
t.forward(120)
t.backward(120)

# Belly
t.seth(90)
t.forward(150)
t.backward(20)

# Hands
t.seth(0)
t.backward(80)
t.forward(160)
t.backward(80)

# Head
t.seth(90)
t.forward(20)
t.seth(0)
t.circle(60)

# Eyes
go(20,220)
t.begin_fill()
t.circle(5)
t.end_fill()

go(-40,220)
t.begin_fill()
t.circle(5)
t.end_fill()

# Mouth
go(-35,190)
t.seth(-60)
t.circle(30,120)

t.ht()
tu.done()