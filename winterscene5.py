import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("powderblue")

t = turtle.Turtle()
t.speed(10)

# Bottom Circle
t.penup()
t.goto(-100, -100)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(30)
t.end_fill()

# Middle Circle
t.penup()
t.goto(-100, -50)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(20)
t.end_fill()

# Top Circle
t.penup()
t.goto(-100, -10)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(10)
t.end_fill()

# Eyes
t.penup()
t.goto(-104, 0)
t.pendown()
t.dot(5, "black")
t.penup()
t.goto(-96, 0)
t.pendown()
t.dot(5, "black")

# Carrot Nose
t.penup()
t.goto(-100, -10)
t.pendown()
t.setheading(0)
t.color("orange")
t.begin_fill()
t.circle(5, 180)
t.end_fill()

# Christmas Tree (second object)
t.penup()
t.goto(140, 5)
t.pendown()

# Tree shape (triangle)
t.setheading(0)
t.begin_fill()
t.color("forest green")
for _ in range(3):
    t.forward(60)
    t.left(120)
t.end_fill()

# Draw Ornaments on the Christmas Tree
# First row of ornaments
t.penup()
t.goto(155, 10)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(180, 15)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(5)
t.end_fill()

# Second row of ornaments
t.penup()
t.goto(170, 30)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(5)
t.end_fill()

# Third row of ornaments
t.penup()
t.goto(170, 50)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(5)
t.end_fill()

# Tree Trunk
t.penup()
t.goto(165, -5)
t.pendown()
t.begin_fill()
t.color("saddle brown")
for _ in range(4):
    t.forward(10)
    t.left(90)
t.end_fill()

# Draw Gifts (third object)
t.penup()
t.goto(-200, 50)
t.pendown()

# First Gift Box
t.begin_fill()
t.color("red")
for _ in range(4):
    t.forward(20)
    t.left(90)
t.end_fill()

# Ribbon on Gift Box
t.penup()
t.goto(-190, 60)
t.pendown()
t.color("gold")
t.setheading(90)
t.forward(20)
t.backward(10)
t.setheading(0)
t.forward(20)
t.backward(10)

# Second Gift Box
t.penup()
t.goto(-150, 150)
t.pendown()

t.begin_fill()
t.color("blue")
for _ in range(4):
    t.forward(20)
    t.left(90)
t.end_fill()

# Ribbon on Second Gift Box
t.penup()
t.goto(-140, 160)
t.pendown()
t.color("gold")
t.setheading(90)
t.forward(20)
t.backward(10)
t.setheading(0)
t.forward(20)
t.backward(10)

# Draw Snowflakes
# First Snowflake
t.penup()
t.color('white')
t.goto(0, 100)
t.pendown()
for _ in range(6):
    t.forward(10)
    t.backward(10)
    t.right(60)

# Second Snowflake
t.penup()
t.goto(-200, 200)
t.pendown()
for _ in range(6):
    t.forward(10)
    t.backward(10)
    t.right(60)

# Draw Holly Berries
# First set of berries
t.penup()
t.goto(200, 200)
t.pendown()
t.color("red")
for _ in range(2):
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

# Holly Leaves
t.penup()
t.goto(210, 208)
t.pendown()
t.color("forest green")
t.begin_fill()
t.setheading(45)
t.circle(10, 90)
t.setheading(180)
t.circle(10, 90)
t.end_fill()

t.penup()
t.goto(0, 250)
t.pendown()
t.color("red")
t.write("Happy Holidays!", align="center", font=("Lora", 24, "bold"))

t.hideturtle()
turtle.done()

