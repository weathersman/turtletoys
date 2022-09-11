import turtle
import random

t = turtle.Turtle()
turtle.tracer(1)
screen = turtle.Screen()
screen.bgcolor('black')
t.hideturtle()
t.color('yellow')
t.pensize(1)


def dolightning(s, a, l):

    if l < 1:
        return

    t.setheading(a)
    t.pensize(l)
    t.color('yellow')
    t.forward(s)
    pos = t.pos()
    t.color('gold2')
    dolightning(random.randint(75, 150), random.choice(range(30, 120)), l - 1)
    t.penup()
    t.goto(pos)
    t.pendown()
    t.color('gold1')
    dolightning(random.randint(50, 75), random.choice(range(30, 90)), l - 1)
    t.penup()
    t.color('gold')
    t.goto(pos)
    t.pendown()
    dolightning(random.randint(10, 25), random.choice(range(30, 60)), l - 1)


for x in range(1, 5):
    t.penup()
    t.goto(-150, -250)
    t.pendown()
    dolightning(100 * x, 60, 3)

turtle.update()
screen.exitonclick()
