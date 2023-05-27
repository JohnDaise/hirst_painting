from turtle import *
import random

"""Requirements:
    Draw 10 by 10 rows of spots
    Each spot will have random color
    Each spot will be 20 in size and 50 paces apart
    
"""

# RGB Color List from Palette
color_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62), (197, 144, 171), (143, 180, 206),
              (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132),
              (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41),
              (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145),
              (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

colormode(255)

# Initialize number of spots
num_spots = 10

# Initialize Turtle
tim = Turtle()
tim.shape("turtle")
tim.color("bisque")
tim.penup()
tim.setposition(-250, -250)


# creates single row of spots
def draw_spot_row(spots):
    for i in range(spots - 1):
        spot_color = random.choice(color_list)
        tim.pendown()
        tim.pencolor(spot_color)
        tim.dot(20)
        tim.penup()
        tim.forward(50)
    tim.dot(20)


# setup for swapping values
a = 180
b = 0
left_right = a
total = a + b

# loop to create multiple rows
for _ in range(num_spots):
    draw_spot_row(num_spots)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(left_right)
    left_right = total - left_right  # swaps value

screen = Screen()
screen.exitonclick()
