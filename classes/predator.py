import pygame

from random import randint


class Predator:

    def __init__(self, x, y, color, camera):
        self.xpos = x
        self.ypos = y
        self.size = 6
        self.counter = 0
        self.color = color

        self.camera = camera

        self.compass = randint(0,3)

        self.Red = (255, 0, 0)

        self.biomaterial = 100

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.xpos + self.camera.xpos), int(self.ypos + self.camera.ypos)), self.size)

    def move(self):
        self.counter +=1
        # self.biomaterial += 1
        temp = randint(0,3)
        temp2 = randint(0,5)
        if temp != self.compass:
            temp = randint(0,3)

        # Cell goes right
        if temp == 0:
            self.xpos = self.xpos + temp2
        # Cell goes left
        if temp == 1:
            self.xpos = self.xpos - temp2
        # Cell goes
        if temp == 2:
            self.ypos = self.ypos + temp2
        # Cell goes
        if temp == 3:
            self.ypos = self.ypos - temp2

        if self.counter >= 250:
            self.counter = 0
            self.compass = randint(0, 3)
           #  print("Compass has been changed")