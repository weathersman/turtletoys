import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(10)
t.color('slategray')
t.pensize(1)
t.hideturtle()

t2 = turtle.Turtle()
t2.speed(10)
t2.color('darkred')
t2.pensize(1)
t2.hideturtle()

for x in range(0, 40):
    t.forward(200)
    t2.penup()
    t2.goto(t.pos())
    t2.setheading(t.heading())
    t2.right(98)
    t2.pendown()
    t2.begin_fill()
    t2.forward(17)
    t2.left(120)
    t2.forward(17)
    t2.left(120)
    t2.forward(17)
    t2.end_fill()
    t.left(170)

turtle.update()
screen.exitonclick()