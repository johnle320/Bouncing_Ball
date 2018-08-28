import pygame


class Ball(object):

    def __init__(self, coor, radius):
        self.radius = radius
        self.x = coor[0]
        self.y = coor[1]

    def display(self, surface, color, thickness):
        pygame.draw.circle(surface, color, [self.x, self.y], self.radius, thickness)
