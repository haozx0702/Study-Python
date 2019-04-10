import uturtle

turtle = uturtle.Turtle()
def rect(x, y, color, x2, y2):
    width = abs(x2 - x)
    height = abs(y2 - y)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor(color)
    # turtle.color(color, color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill() 

turtle.reset()
turtle.speed(0)
#turtle.delay(0)
turtle.bgcolor('black')
turtle.clear()
rect(-75, 50, 'white', 75, 0)
rect(-75, 0, 'red', 75, -50)

turtle.home()
turtle.begin_fill()
turtle.color('blue', 'blue')
turtle.goto(-75, 50)
turtle.goto(-75, -50)
turtle.goto(0, 0)
turtle.end_fill()




