import turtle as t

t.bgcolor("black")
t.color("blue")

t.speed(10)
t.pensize(1)

t.penup()
t.goto(-250,-100)
t.pendown()

for i in range (100):
    t.forward(500)
    t.left(125)

t.hideturtle()
t.done()