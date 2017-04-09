import pygame

from random import randint


class Plant:

    def __init__(self, x, y, camera):
        self.xpos = x
        self.ypos = y
        self.size = 10
        self.readyToGrow = False
        self.camera = camera
        self.color = (0, 179, 0)
        self.adult = False
        self.biomaterial = 15
        self.wood = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.xpos + self.camera.xpos), int(self.ypos + self.camera.ypos)), self.size)


    def grow(self):
        temp = randint(0, 100)

        if temp == 0:
            self.readyToGrow = True


    def is_wood(self):

        temp = randint(0,1000)

        if temp == 0:
            self.wood = True