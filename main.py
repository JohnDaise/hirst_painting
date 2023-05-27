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


# Initialize Turtle
tim = Turtle()
tim.shape("turtle")
tim.color("bisque")


def draw_spot():
    spot_color = random.choice(color_list)
    tim.pencolor(spot_color)
    tim.dot(20)
    tim.penup()
    tim.forward(50)


draw_spot()

screen = Screen()
screen.exitonclick()
