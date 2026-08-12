import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
square = turtle.Turtle()

num_sides = 4
side_length = 100
angle = 90

for i in range(num_sides):
    square.forward(side_length)
    square.right(angle)

turtle.done()
