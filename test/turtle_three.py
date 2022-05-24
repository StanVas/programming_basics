import turtle
import math

n = turtle.Turtle()
n.color('green')
n.speed(10000)
n.shape('turtle')
n.end_fill()

for i in range(2000):
    n.forward(10)
    n.left(math.sin(i / 10 ) * 25)
    n.left(20)

n.end_fill()
turtle.done()
