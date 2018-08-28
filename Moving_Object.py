"""
REMARKS:
1. pygame.draw.circle(screen, color, center coordinate, radius, thickness pixel)
"""

import pygame

from Model.Ball import Ball
from Model.Rect import Rect

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


# set up circle shape:
ball = Ball([300, 200], 15)


# set up the paddle:
paddle_x = wth - 200
paddle_y = hght - 80
paddle_color = [0, 255, 0]
paddle_w = 160
paddle_len = 40

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
            if mouse_x >= wth - paddle_w / 2:
                paddle_x = wth - paddle_w
            elif mouse_x <= paddle_w / 2:
                paddle_x = 0
            else:  # while the mouse is inside the window
                # move the x_coordinate
                # te of the paddle to that of the mouse
                paddle_x = mouse_x - (paddle_w / 2)

    # Erase the whole screen:
    screen.fill(scrn_colr)  # set the screen background to this color

    # Update the ball's position
    ball.x += delta_x
    ball.y += delta_y

    ''' Test if the ball and the paddle collide'''
    # #  Imaginary rectangles boxing the circle and paddle for collide detection
    # ball_rect = pygame.Rect(paddle_x, paddle_y, paddle_w, paddle_len)
    # paddle_rect = pygame.Rect(ball_x - radius, ball_y - radius, radius * 2, radius * 2)
    paddle_center_x = paddle_x + paddle_w / 2
    paddle_center_y = paddle_y + paddle_len / 2
    distance_x = abs(paddle_center_x - ball.x)
    distance_y = abs(paddle_center_y - ball.y)

    if distance_x <= paddle_w / 2 + ball.radius and distance_y <= paddle_len / 2 + ball.radius:
        # if paddle_y > ball_y:  # the ball is above the paddle
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
    circle_color = [255, 0, 0]
    cir_thick = 0  # pixels
    ball.display(screen, circle_color, cir_thick)

    pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_w, paddle_len], 0)

    # refresh the screen
    pygame.display.update()
    clock.tick(40)