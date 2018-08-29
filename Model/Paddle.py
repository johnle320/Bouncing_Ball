import pygame


class Paddle(object):

    def __init__(self, top, left, width, length):
        self.x = top
        self.y = left
        self.width = width
        self.length = length
        self.center_x = self.x + self.width / 2
        self.center_y = self.y + self.length / 2

    def display(self, surface, color, thickness):
        pygame.draw.rect(surface, color, [self.x, self. y, self.width, self.length], thickness)
