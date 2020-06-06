import turtle


def buttonclick(x, y):
    print("You clicked at this coordinate({0},{1})".format(x,y))

# onscreen function to send coordinate
turtle.onscreenclick(buttonclick, 1)
# hold the screen

#This to make turtle object
tess = turtle.Turtle()
polygon = turtle.Turtle()
circle = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

r = 50

triangle = turtle.Turtle()

triangle.forward(100)  # draw base

triangle.left(120)
triangle.forward(100)

triangle.left(120)
triangle.forward(100)

turtle.done()

turtle.circle(r)
turtle.done()

turtle.listen()
turtle.listen()


# self defined function to print coordinate