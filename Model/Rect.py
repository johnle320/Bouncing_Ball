import pygame


class Rect(object):

    def __init__(self, top, left, width, length):
        self.top = top
        self.left = left
        self.width = width
        self.length= length
        self.x = left + length / 2
        self.y = top + length / 2

    def display(self, surface, color, thickness):
        pygame.draw.rect(surface, color, [self.top, self. left, self.width, self.length], thickness)