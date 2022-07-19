
import turtle

turtle.Screen().bgcolor("white")

t = turtle.Pen()
t.pensize(6)

t.pu()
t.goto(180,-300)
t.seth(80)
t.pd()

#****-------Wings-----*****#
t.fillcolor("#54a0cc")
t.begin_fill()
t.circle(180,200)
t.end_fill()

t.pu()
t.goto(180,-300)
t.seth(135)
t.pd()

t.fillcolor("white")
t.begin_fill()
t.circle(250,90)
t.end_fill()

#*********-----------***********#
t.pu()
t.goto(110,-280)
t.seth(80)
t.pd()


#********---Main Body------******#
t.begin_fill()
t.forward(380)
t.seth(90)
t.circle(600,30)
t.circle(250,30)
t.seth(-150)
t.circle(250,30)
t.seth(-120)
t.circle(600,30)
t.seth(-80)
t.forward(380)

t.seth(-30)
t.circle(210,60)
t.end_fill()

t.pu()
t.goto(112,360)
t.seth(105)
t.pd()

t.fillcolor("red")

t.begin_fill()
t.circle(190,50)
t.seth(-158)
t.circle(190,50)
t.seth(-30)
t.circle(210,60)
t.end_fill()

#------*****Dotted Holes******------#
t.pensize(9)

t.pu()
t.goto(100,330)
t.pd()
t.circle(5)

t.pu()
t.goto(65,320)
t.pd()
t.circle(5)

t.pu()
t.goto(30,312)
t.pd()
t.circle(5)

t.pu()
t.goto(0,310)
t.pd()
t.circle(5)

t.pu()
t.goto(-30,315)
t.pd()
t.circle(5)

t.pu()
t.goto(-60,325)
t.pd()
t.circle(5)

t.pu()
t.goto(-90,335)
t.pd()
t.circle(5)

#------*******Curve******---#
t.pensize(4)
t.pu()
t.goto(-120,-180)
t.pd()
t.seth(-25)
t.circle(295,50)

#-------****Circular Window-----****#
t.pu()
t.goto(40,100)
t.pd()

t.fillcolor("grey")
t.begin_fill()
t.circle(80)
t.end_fill()

t.pu()
t.goto(33,113)
t.pd()

t.fillcolor("#9ecbe6")
t.begin_fill()
t.circle(65)
t.end_fill()

#********----Fire🔥-----*******#

t.pensize(4)
t.pu()
t.goto(60,-323)
t.seth(-60)
t.pd()

t.fillcolor("#ed461c")
t.begin_fill()
t.circle(-90,70)
t.circle(200,25)
t.seth(160)
t.circle(-120,60)
t.seth(110)
t.circle(-90,60)
t.end_fill()


t.pu()
t.goto(40,-330)
t.seth(-60)
t.pd()

t.fillcolor("#ffc30f")
t.begin_fill()
t.circle(-90,70)
t.circle(120,25)
t.seth(160)
t.circle(-80,60)
t.seth(110)
t.circle(-80,70)
t.end_fill()

#*********-------Nozzle****-----#
t.fillcolor("grey")
t.pu()
t.goto(90,-290)
t.seth(-90)
t.pd()
t.pensize(8)

t.begin_fill()
t.forward(20)
t.seth(-150)
t.circle(-170,60)
t.seth(90)
t.forward(20)
t.seth(-30)
t.circle(165,60)
t.end_fill()

turtle.done()