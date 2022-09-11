import turtle

t = turtle.Turtle()
turtle.tracer(2)
screen = turtle.Screen()
screen.bgcolor('black')
t.hideturtle()
t.color('green')
t.pensize(1)

colors = ['lavenderblush', 'orchid', 'mediumorchid', 'darkviolet', 'blueviolet', 'indigo', 'blue', 'blue3']


def dodiamonds(s, l, x, y):

    if l < 1:
        return

    t.color(colors[l])

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.forward(s)
    t.left(120)
    t.forward(s)
    t.left(120)
    t.forward(s)
    t.left(120)

    dodiamonds(s / 2, l - 1, x + s / 2, y)
    dodiamonds(s / 2, l - 1, x, y)


dodiamonds(300, 7, -150, -100)

turtle.update()
screen.exitonclick()
