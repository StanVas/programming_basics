import turtle
n = turtle.Turtle()
n.speed(10)

for i in range(180):
    n.forward(100)
    n.right(30)
    n.forward(20)
    n.left(60)
    n.forward(50)
    n.right(30)

    n.penup()
    n.setposition(0, 0)
    n.pendown()
    n.right(2)

turtle.done()
