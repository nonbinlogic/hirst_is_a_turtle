from turtle import Turtle, Screen, colormode
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# Parameters
dot_radius = 15
dot_size = dot_radius * 2
spacing = 45
num_dots = 10
margin = 90

grid_size = (num_dots * dot_size) + (num_dots - 1) * spacing

screen_x = screen_y = grid_size + 2 * margin

# Set up the screen
screen = Screen()
screen.setup(screen_x, screen_y)
screen_width = screen.window_width()
screen_height = screen.window_height()

left_edge = -screen_width // 2
right_edge = screen_width // 2
bottom_edge = -screen_height // 2
top_edge = screen_height // 2

timmy = Turtle()
timmy.shape("turtle")
timmy.shapesize(3, 3, 3)

# timmy.hideturtle()

colormode(255)


def draw_dots(turtle_obj, rows, cols, radius, interval, gutter):
    for row in range(rows):
        for col in range(cols):
            if row % 2 == 0:
                x = left_edge + gutter + col * (interval + radius * 2) + radius
                turtle_obj.setheading(0)
            else:
                x = right_edge - gutter - col * (interval + radius * 2) - radius
                turtle_obj.setheading(180)
            y = top_edge - gutter - row * (interval + radius * 2) - radius
            color = random_color()
            turtle_obj.speed(0)
            turtle_obj.penup()
            turtle_obj.goto(x, y)
            turtle_obj.pendown()
            turtle_obj.color(color)
            turtle_obj.dot(radius * 2, color)
    turtle_obj.penup()
    turtle_obj.speed(1)
    turtle_obj.forward(200)
    turtle_obj.hideturtle()


draw_dots(timmy, num_dots, num_dots, dot_radius, spacing, margin)

screen.mainloop()
