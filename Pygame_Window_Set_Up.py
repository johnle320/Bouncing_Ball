"""
REMARKS:
1. pygame.display.set_mode([width, height])
2. color = [red, blue, green]
3. screen.fill(color)
4. pygame.display.set_caption(string)
5. pygame.event.get() : return a list of events
6. <event>.type : return enum of pygame.<event type> (ex: pygame.QUIT)
"""

import pygame
import sys

# start pygame library
pygame.init()

# set up:
wth_i = 640  # screen width
hght_i = 480  # screen height
scrn_sz_i = [wth_i, hght_i]  # choose screen size
screen = pygame.display.set_mode(scrn_sz_i)  # set screen size
pygame.display.set_caption("Bouncing Game")  # set caption for the window
scrn_colr = [25, 50, 85]  # select background color for the screen
screen.fill(scrn_colr)  # set the screen background to this color

# here we go, the screen.
pygame.display.flip()

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
             Therefore we should add: pygame.quit() """

