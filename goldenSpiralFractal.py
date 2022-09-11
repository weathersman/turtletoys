import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
turtle.tracer(5)
screen = turtle.Screen()
screen.bgcolor('black')
t.hideturtle()
t2.hideturtle()
x = 0
y = 0
t.pensize(1)


def dogoldenspiral(c, s, x, y, f, l):

    if l < 1:
        return

    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    for i in range(35):
        t.penup()
        t.forward(s+i)
        t.left(30 - i/1.5)
        t.pendown()

        t2.penup()
        t2.goto(t.pos())
        t2.pendown()

        t2.color(c)
        t2.pensize(l)
        if f < 1:
            t2.circle(i)
        else:
            t2.begin_fill()
            t2.circle(i)
            t2.end_fill()


    dogoldenspiral('black', s, x + 1, y + 1, 0, l - 1)
    dogoldenspiral('gold', s, x + 2, y + 2, f, l - 1)

dogoldenspiral('gold3', 15, 0, 0, 1, 2)
turtle.update()
screen.exitonclick()
