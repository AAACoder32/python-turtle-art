
# Code Credit:-Giáo Ộp IT GO.IT
import math
from turtle import*

def heartx(n):
    return 14*math.sin(n)**3

def hearty(n):
    return 12*math.cos(n)-5*\
           math.cos(2*n)-2*\
           math.cos(3*n)-\
           math.cos(4*n)

speed(800)
bgcolor("black")

for i in range(5000):

    goto(heartx(i)*20,hearty(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)
done()