import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')

#t.hideturtle()
t.pensize(1)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def midpoint(p1, p2):
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)


def getbranchpoints(p1, p2):
    m = midpoint(p1, p2)
    m1 = midpoint(p1, m)
    m2 = midpoint(m, p2)
    return m1, m2


def dokoch(p1, p2, c, angle, heading, lv):

    if lv < 1:
        return

    t.penup()
    t.goto(p1.x, p1.y)
    t.color(c)
    t.pendown()

    t.setheading(heading)
    t.goto(p2.x, p2.y)

    (b1, b2) = getbranchpoints(p1, p2)

    d_b1_b2 = math.dist((b1.x, b1.y), (b2.x, b2.y))

    t.goto(b1.x, b1.y)
    t.left(angle)
    t.begin_fill()
    t.forward(d_b1_b2)
    p3 = Point(t.pos()[0], t.pos()[1])
    t.right(angle * 2)
    t.forward(d_b1_b2)
    t.end_fill()
    t.left(angle)

    dokoch(p1, b1, 'white', angle, heading, lv - 1)
    dokoch(b2, p2, 'white', angle, heading, lv - 1)
    dokoch(b1, p3, 'white', angle, heading + angle, lv - 1)
    dokoch(p3, b2, 'white', angle, heading - angle, lv - 1)

dokoch(Point(-200, -100), Point(200, -100), 'white', 60, 0, 3)

turtle.update()
screen.exitonclick()
