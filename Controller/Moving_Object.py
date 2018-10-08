"""
REMARKS:
1. pygame.draw.circle(screen, color, center coordinate, radius, thickness pixel)
"""

import pygame
from random import randint

from Model.Ball import Ball
from Model.Paddle import Paddle
from Controller.Collision_Dectector import wall_ball_rebounce
from Controller.Collision_Dectector import ball_paddle_rebounce
from Controller.Collision_Dectector import mouse_paddle_adjustment

# start pygame library
pygame.init()

# set up screen:
caption = "Bounce Game"
wth = 600
hght = 400
scrn_colr = [20, 45, 85]
pygame.display.set_caption(caption)  # set caption for the window
screen = pygame.display.set_mode([wth, hght])  # set screen size
screen.fill(scrn_colr)  # set the screen background to this color
pygame.display.flip()  # display the screen


# set up the ball:
circle_color = [255, 0, 0]
cir_thick = 0  # pixels
ball_x = randint(50, 300)
ball_y = 200
radius = 15
ball = Ball([ball_x, ball_y], radius, cir_thick)


# set up the paddle:
paddle_x = wth - 200
paddle_y = hght - 80
paddle_w = 160
paddle_len = 40
paddle_color = [0, 255, 0]
paddle_thick = 0
paddle = Paddle(paddle_x, paddle_y, paddle_w, paddle_len, paddle_thick)

# Limit of frame per second
clock = pygame.time.Clock()

# increment ball motion:
delta_x = 3
delta_y = 1


running_b = True
while running_b:
    """the thing is, this loop would run for infinite. So we need to check for the user's input
    (known as 'events') using pygame.event.get(), which returns a list of events. We loop through each
     event in <events> and see if there is a QUIT event (the action of user clicking the QUIT button on
     the pygame window"""

    events = pygame.event.get()
    for ea_event in events:
        if ea_event.type == pygame.QUIT:
            running_b = False
            """sometime if running on IDE, it would prevent the pygame window from quiting properly.
             Therefore we should add: pygame.quit()"""

        if ea_event.type == pygame.MOUSEMOTION:
            mouse_paddle_adjustment(screen, paddle)

    # Erase the whole screen:
    screen.fill(scrn_colr)  # set the screen background to this color

    # check for ball-paddle collision
    [delta_x, delta_y] = ball_paddle_rebounce(ball, paddle, [delta_x, delta_y])
    # check for wall-ball collision
    [delta_x, delta_y] = wall_ball_rebounce(ball, screen, [delta_x, delta_y])
    # Update the ball center position
    ball.x += delta_x
    ball.y += delta_y

    # redraw the ball and the paddle
    ball.display(screen, circle_color,)
    paddle.display(screen, paddle_color)

    # refresh the screen
    pygame.display.update()
    clock.tick(60)