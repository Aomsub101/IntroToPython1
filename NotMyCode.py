import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Majestic Night Sky")

# Create a turtle for drawing the moon
moon = turtle.Turtle()
moon.hideturtle()
moon.speed(0)
moon.penup()
moon.goto(200, 150)
moon.pendown()

# Draw the moon
moon.color("yellow")
moon.begin_fill()
moon.circle(60)
moon.end_fill()

# Create another turtle for stars
stars = turtle.Turtle()
stars.hideturtle()
stars.speed(0)
stars.color("white")

# Function to draw stars at random positions
def draw_star(x, y, size):
    stars.penup()
    stars.goto(x, y)
    stars.pendown()
    stars.begin_fill()
    for _ in range(5):
        stars.forward(size)
        stars.right(144)
    stars.end_fill()

# Function to create multiple stars
def create_stars():
    for _ in range(100):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        size = random.randint(10, 20)
        draw_star(x, y, size)

# Create a turtle for drawing shooting stars
shooting_star = turtle.Turtle()
shooting_star.hideturtle()
shooting_star.color("lightblue")
shooting_star.speed(1)

# Function to draw a shooting star
def draw_shooting_star():
    shooting_star.penup()
    shooting_star.goto(-250, 200)
    shooting_star.pendown()
    shooting_star.pensize(4)
    shooting_star.goto(100, 50)

# Function to draw the majestic night sky
def draw_sky():
    create_stars()
    draw_shooting_star()    

# Draw the sky
draw_sky()

# Hide the turtles and complete the drawing
moon.hideturtle()
stars.hideturtle()
shooting_star.hideturtle()

# Close the window on click
screen.exitonclick()
