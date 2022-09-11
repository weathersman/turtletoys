import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')

t.hideturtle()
t.color('orange')
t.pensize(1)
t.penup()
t.goto(-200, 50)
t.pendown()
t.left(45)


def dosquare(s, lv):

    if lv < 1:
        return

    for j in range(4):
        t.forward(s)
        t.right(90)

    dosquare(s/2, lv-1)

dosquare(350, 10)
dosquare(300, 8)
dosquare(250, 6)
dosquare(200, 4)

turtle.update()
screen.exitonclick()
