import pygame


class Paddle(object):

    def __init__(self, top, left, width, length, thick):
        self.x = top
        self.y = left
        self.width = width
        self.length = length
        self.thick = thick

    def center_coor(self):
        center_x = self.x + self.width / 2
        center_y = self.y + self.length / 2
        return [center_x, center_y]

    def display(self, surface, color):
        pygame.draw.rect(surface, color, [self.x, self. y, self.width, self.length], self.thick)
