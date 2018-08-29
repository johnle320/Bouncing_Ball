import pygame


# Check if the ball touches the screen
# if yes, change the ball to the opposite direction
# by changing the increment = [delta_x, delta_y]
def wall_ball_rebounce(ball, screen, increment):
    # <ball>, <screen> are references to objects
    # <delta_x>, <delta_y> are not

    # readability
    dx = increment[0]
    dy = increment[1]
    width = screen.get_width()
    height = screen.get_height()

    # for x direction
    if ball.x + ball.radius + ball.thick >= width:  # reach the right wall
        ball.x = width - ball.thick - ball.radius
        dx = - dx
    elif ball.x - ball.radius - ball.thick <= 0:  # reach the left wall
        ball.x = ball.radius + ball.thick
        dx = - dx

    # for y direction
    if ball.y + ball.radius + ball.thick >= height:  # reach the bottom
        ball.y = height - ball.radius - ball.thick
        dy = - dy
    elif ball.y - ball.radius - ball.thick <= 0:  # reach the top
        ball.y = ball.radius + ball.thick
        dy = - dy

    increment = [dx, dy]    # readability
    return increment


# Adjust the position of the paddle relatively to the position of the
# mouse when the mouse is inside the screen.
def mouse_paddle_adjustment(screen, paddle):

    [mouse_x, mouse_y] = pygame.mouse.get_pos()  # give mouse coordinate

    # stop the paddle from following the mouse when the mouse is outside of the window
    if mouse_x >= screen.get_width() - paddle.width / 2:
        paddle.x = screen.get_width() - paddle.width
    elif mouse_x <= paddle.width / 2:
        paddle.x = 0
    else:  # while the mouse is inside the window
        # move the x_coordinate
        # te of the paddle to that of the mouse
        paddle.x = mouse_x - (paddle.width / 2)


# check if the ball and the paddle collide
def ball_paddle_rebounce(ball, paddle, increment):

    [delta_x, delta_y] = increment
    [p_center_x, p_center_y] = paddle.center_coor()
    distance_x = abs(p_center_x - ball.x)
    distance_y = abs(p_center_y - ball.y)

    if distance_x <= paddle.width / 2 + ball.radius and distance_y <= paddle.length / 2 + ball.radius:
        # if paddle.y > ball.y:  # the ball is above the paddle
        delta_y = - delta_y

    increment = [delta_x, delta_y]
    return increment