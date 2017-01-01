import pygame

from random import randint


class Plant:

    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.size = 10
        self.readyToGrow = False

        self.Green = (0, 255, 0)

        self.biomaterial = 100

    def draw(self, screen):
        pygame.draw.rect(screen, self.Green, [self.xpos, self.ypos, self.size, self.size])

    def grow(self):
        temp = randint(0, 100)

        if temp == 0:
            self.readyToGrow = True

