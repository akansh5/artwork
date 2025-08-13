import turtle as t
import random

t.bgcolor("black")
t.speed(0)
t.pensize(3)

t.penup()
t.goto(-250,-100)
t.pendown()

for i in range(125):
    t.color(random.random(), random.random(), random.random())
    t.forward(500)
    t.left(125)

t.hideturtle()
t.done()