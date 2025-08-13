#killer(eyes + smile) smiley
import turtle as t


t.bgcolor("#DDDDDD")
t.speed(10)
t.pensize(2)

#round face
t.color("black","yellow")
t.begin_fill()
t.penup()
t.goto(0,-200)
t.pendown()
t.setheading(360)
t.circle(200)
t.end_fill()

#the eyes never lie
t.color("black","black")
t.begin_fill()
t.penup()
t.goto(-100,0)
t.pendown()
t.circle(50)
t.end_fill()

t.color("black","black")
t.begin_fill()
t.penup()
t.goto(100,0)
t.pendown()
t.circle(50)
t.end_fill()

#nose 
t.pensize(5)
t.penup()
t.goto(0,-30)
t.pendown()
t.setheading(270)
t.forward(20)

#killer smile
t.color("red")
t.pensize(10)
t.penup()
t.goto(-45,-100)
t.pendown()
t.setheading(320)
t.circle(67,95)


t.hideturtle()
t.done()