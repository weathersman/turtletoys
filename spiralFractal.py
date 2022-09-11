import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.hideturtle()

t.left(45)
turtle.tracer(10, 1)

colors = ['black', 'lavenderblush', 'mediumorchid', 'darkviolet', 'blueviolet', 'indigo', 'blue', 'darkblue']


def dospiral(a, x, y, level):

    if level < 1:
        return

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(2*(level-1))
    t.color(colors[level])

    for i in range(a):
        t.circle(i, 20)

    dospiral(a, x+2, y, level-1)


dospiral(180, -50, 50, 7)

turtle.update()
screen.exitonclick()



