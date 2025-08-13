import turtle as t

t.bgcolor("black")
t.color("blue","cyan")

t.speed(10)
t.pensize(1)

t.goto(-100,0)

for i in range (50):
    t.forward(250)
    t.left(130)

t.hideturtle()
t.done()