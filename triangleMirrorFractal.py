import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.hideturtle()
t.color('green')
t.pensize(1)

def dodiamonds(h, s, l):

    if l < 1:
        return

    t.penup()
    t.goto(0, 0)
    t.setheading(h)
    t.pendown()

    t.forward(s)
    t.left(120)
    t.forward(s)
    t.left(120)
    t.forward(s)
    t.left(120)

    dodiamonds(h, s / 2, l-1)


dodiamonds(0, 200, 6)
dodiamonds(180, 100, 6)
screen.exitonclick()
