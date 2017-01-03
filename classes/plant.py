import pygame

from random import randint


class Plant:

    def __init__(self, x, y, camera):
        self.xpos = x
        self.ypos = y
        self.size = 10
        self.readyToGrow = False
        self.camera = camera
        self.color = (0, 255, 0)

        self.biomaterial = 100

    def draw(self, screen):
        # pygame.draw.rect(screen, self.color, [self.xpos + self.camera.xpos, self.ypos + self.camera.ypos, self.size, self.size])

        pygame.draw.circle(screen, self.color, (int(self.xpos + self.camera.xpos), int(self.ypos + self.camera.ypos)), self.size)


    def grow(self):
        temp = randint(0, 100)

        if temp == 0:
            self.readyToGrow = True
