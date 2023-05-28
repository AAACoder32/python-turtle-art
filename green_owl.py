
# AAACoder Owl Drawing
import turtle as tu

t = tu.Turtle()
t.speed(0)

# Colors
light_green = "#3bb36f"
dark_green = "#094724"
white = "#ffffff"
black = "#000000"
yellow = "#f7bb14"

# Utility
def go(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

# Main Body
go(0,-250)

t.color(light_green)

t.begin_fill()
t.circle(150)
t.end_fill()


# Head
go(-138,50)
t.seth(-50)

t.begin_fill()
t.circle(170,100)
t.seth(70)
t.circle(300,40)
t.circle(10,130)
t.forward(50)
t.seth(156)
t.circle(200,50)
t.seth(118)
t.forward(50)
t.circle(10,130)
t.circle(300,40)
t.end_fill()

# Eyes
t.color(black)

go(-70,80)
t.seth(0)
t.color(white)
t.begin_fill()
t.circle(50)
t.end_fill()
go(-60,95)
t.color(black)
t.begin_fill()
t.circle(30)
t.end_fill()
go(-75,130)
t.color(white)
t.begin_fill()
t.circle(7)
t.end_fill()

go(60,80)
t.begin_fill()
t.circle(50)
t.end_fill()
go(50,95)
t.color(black)
t.begin_fill()
t.circle(30)
t.end_fill()
go(43,135)
t.color(white)
t.begin_fill()
t.circle(7)
t.end_fill()

# Chonch
go(-27,90)
t.seth(35)
t.color(yellow)
t.begin_fill()
t.circle(-40,70)
t.seth(-118)
t.forward(50)
t.seth(118)
t.forward(50)
t.end_fill()

# Legs
#Left
go(-60,-230)
t.seth(-90)

t.begin_fill()
t.forward(20)
t.circle(6,180)
t.forward(20)
t.circle(6,180)
t.end_fill()

go(-48,-230)
t.seth(-90)

t.begin_fill()
t.forward(20)
t.circle(6,180)
t.forward(20)
t.circle(6,180)
t.end_fill()

go(-36,-230)
t.seth(-90)

t.begin_fill()
t.forward(20)
t.circle(6,180)
t.forward(20)
t.circle(6,180)
t.end_fill()


# Right
go(20,-230)
t.seth(-90)

t.begin_fill()
t.forward(20)
t.circle(6,180)
t.forward(20)
t.circle(6,180)
t.end_fill()

go(32,-230)
t.seth(-90)

t.begin_fill()
t.forward(20)
t.circle(6,180)
t.forward(20)
t.circle(6,180)
t.end_fill()


go(44,-230)
t.seth(-90)

t.begin_fill()
t.forward(20)
t.circle(6,180)
t.forward(20)
t.circle(6,180)
t.end_fill()

# Feathers

# Left
go(-90,20)
t.seth(160)
t.color(dark_green)
t.begin_fill()
t.circle(150,60)
t.circle(10,120)
t.circle(80,40)
t.seth(-160)
t.circle(80,30)
t.circle(5,130)
t.circle(60,30)

t.seth(-150)
t.circle(40,30)
t.circle(7,130)
t.circle(130,60)
t.circle(10,180)
t.end_fill()

# Right
go(80,20)
t.seth(20)

t.begin_fill()
t.circle(-150,60)
t.circle(-10,120)
t.circle(-80,40)
t.seth(-20)
t.circle(-80,30)
t.circle(-5,130)
t.circle(-60,30)

t.seth(-30)
t.circle(-40,30)
t.circle(-7,130)
t.circle(-130,60)
t.circle(-10,180)
t.end_fill()

# other
def other(x,y):
    go(x,y)
    t.begin_fill()
    t.seth(-60)
    t.circle(20,120)
    t.seth(-140)
    t.circle(-26,90)
    t.end_fill()
    
other(-90,-100)
other(-20,-100)
other(50,-100)

other(-55,-150)
other(20,-150)

t.ht()
tu.done()
