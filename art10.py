

import turtle

cl = ['#9400d3','#0000ff','#00ff00','#ffff00','#ff7f00','#ff0000']


s = turtle.getscreen()
s.bgcolor('#0b091a')

t = turtle.Turtle()
t.pensize(3)
t.speed(11)

for i in range(100):
    turtle.speed(10)
    t.pencolor(cl[i%6])
    t.left(59)
    t.forward(150)
    t.circle(88)
    t.backward(75)
    t.circle(44)
    t.backward(75)

turtle.done()