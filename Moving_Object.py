"""
REMARKS:
1. pygame.draw.circle(screen, color, center coordinate, radius, thickness pixel)
"""

import pygame

from Model.Ball import Ball
from Model.Paddle import Paddle

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


# set up the ball:
circle_color = [255, 0, 0]
cir_thick = 0  # pixels
ball_x = 300
ball_y = 200
radius = 15
ball = Ball([ball_x, ball_y], radius)


# set up the paddle:
paddle_x = wth - 200
paddle_y = hght - 80
paddle_w = 160
paddle_len = 40
paddle_color = [0, 255, 0]
paddle_thick = 0
paddle = Paddle(paddle_x, paddle_y, paddle_w, paddle_len)

# display the screen
pygame.display.flip()

# Limit of frame per second
clock = pygame.time.Clock()

# initial motion set up:
delta_x = 6
delta_y = 2


"""without a loop, the screen would disappear soon because python reaches the end of the program.
So we add a loop in it. So that the program would keep running. """
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
            [mouse_x, mouse_y] = pygame.mouse.get_pos()  # give mouse coordinate

            # stop the paddle from following the mouse when the mouse is outside of the window
            if mouse_x >= wth - paddle.width / 2:
                paddle.x = wth - paddle.width
            elif mouse_x <= paddle.width / 2:
                paddle.x = 0
            else:  # while the mouse is inside the window
                # move the x_coordinate
                # te of the paddle to that of the mouse
                paddle.x = mouse_x - (paddle.width / 2)

    # Erase the whole screen:
    screen.fill(scrn_colr)  # set the screen background to this color

    # Update the ball's position
    ball.x += delta_x
    ball.y += delta_y

    ''' Test if the ball and the paddle collide'''
    # WAY1:
    paddle.center_x = paddle.x + paddle.width / 2
    paddle.center_y = paddle.y + paddle.length / 2
    distance_x = abs(paddle.center_x - ball.x)
    distance_y = abs(paddle.center_y - ball.y)

    # WAY3: DOES NOT WORK
    '''paddle's attributes: center_x and center_y depend on x and y. But x and y are constantly changed,
    but center_x and center_y are not updated accordingly.

    paddle.center_x = paddle.x + paddle.width / 2
    paddle.center_y = paddle.y + paddle.length / 2
    distance_x = abs(paddle.center_x - ball.x)
    distance_y = abs(paddle.center_y - ball.y)
    '''

    # WAY2:
    # distance_x = abs(paddle.center_x - ball.x)
    # distance_y = abs(paddle.center_y - ball.y)

    if distance_x <= paddle.width / 2 + ball.radius and distance_y <= paddle.length / 2 + ball.radius:
        # if paddle_y > ball_y:  # the ball is above the paddle
        print("ball and paddle collided")
        delta_y = - delta_y

    # check if the ball is off the screen
    if ball.x + ball.radius + cir_thick >= screen.get_width():  # reach the right wall
        ball.x = screen.get_width() - cir_thick - ball.radius
        delta_x = - delta_x
    elif ball.x - ball.radius - cir_thick <= 0:  # reach the left wall
        ball.x = ball.radius + cir_thick
        delta_x = - delta_x

    if ball.y + ball.radius + cir_thick >= screen.get_height():  # reach the bottom
        ball.y = screen.get_height() - ball.radius - cir_thick
        delta_y = - delta_y
    elif ball.y - ball.radius - cir_thick <= 0:  # reach the top
        ball.y = ball.radius + cir_thick
        delta_y = - delta_y

    # redraw the whole thing

    ball.display(screen, circle_color, cir_thick)
    paddle.display(screen, paddle_color, paddle_thick)

    # refresh the screen
    pygame.display.update()
    clock.tick(40)