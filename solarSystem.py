import turtle

screen = turtle.Screen()
screen.bgcolor('black')
screen.bgpic('stars.gif')
screen.tracer(0)

mercury = turtle.Turtle()
mercury.hideturtle()
mercury.pensize(1)
mercury.penup()
mercury.goto(0, 3)
mercury.pendown()

venus = turtle.Turtle()
venus.hideturtle()
venus.pensize(1)
venus.penup()
venus.goto(5, -20)
venus.pendown()

earth = turtle.Turtle()
earth.hideturtle()
earth.pensize(1)
earth.penup()
earth.goto(5, -60)
earth.pendown()

moon = turtle.Turtle()
moon.hideturtle()
moon.pensize(1)
moon.penup()
moon.goto(5, -60)
moon.pendown()

mars = turtle.Turtle()
mars.hideturtle()
mars.pensize(1)
mars.penup()
mars.goto(15, -120)
mars.pendown()

jupiter = turtle.Turtle()
jupiter.hideturtle()
jupiter.pensize(1)
jupiter.penup()
jupiter.goto(20, -200)
jupiter.pendown()

saturn = turtle.Turtle()
saturn.hideturtle()
saturn.pensize(1)
saturn.penup()
saturn.goto(25, -300)
saturn.pendown()

uranus = turtle.Turtle()
uranus.hideturtle()
uranus.pensize(1)
uranus.penup()
uranus.goto(30, -350)
uranus.pendown()

neptune = turtle.Turtle()
neptune.hideturtle()
neptune.pensize(1)
neptune.penup()
neptune.goto(35, -375)
neptune.pendown()

sun = turtle.Turtle()
sun.color('yellow')
sun.hideturtle()
sun.penup()
sun.goto(0, 25)
sun.pendown()
sun.begin_fill()
sun.circle(25)
sun.end_fill()
sun.penup()


def move_planet(planet, color, size, angle, distance):
    planet.clear()
    planet.fillcolor(color)
    planet.begin_fill()
    planet.circle(size)
    planet.left(angle)
    planet.forward(distance)
    planet.end_fill()




while True:
    move_planet(mercury, 'orange', 4, 1.3, 1.2)
    move_planet(venus, 'khaki', 5, 1, 1.4)
    move_planet(earth, 'blue', 6, .9, 2.5)
    moon.setposition(earth.pos())
    move_planet(moon, 'gray', 3, 1.2, .1)
    move_planet(mars, 'red', 5, .8, 3.2)
    move_planet(jupiter, 'chocolate', 18, .7, 4.2)
    move_planet(saturn, 'orchid', 10, .6, 5.2)
    move_planet(uranus, 'darkblue', 5, .5, 5.8)
    move_planet(neptune, 'darkgreen', 6, .4, 6.2)
    screen.update()


screen.exitonclick()
