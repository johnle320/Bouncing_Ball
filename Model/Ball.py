import pygame


class Ball(object):

    def __init__(self, coor, radius, thick):
        self.radius = radius
        self.x = coor[0]
        self.y = coor[1]
        self.thick = thick

    def display(self, surface, color):
        pygame.draw.circle(surface, color, [self.x, self.y], self.radius, self.thick)
