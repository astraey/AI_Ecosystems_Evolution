import pygame

from random import randint


class Plant:

    def __init__(self, cell, camera):
        self.xPos = cell.xPos
        self.yPos = cell.yPos
        self.size = 3
        self.counter = 0
        self.color = (0, 153, 0)
        self.cell = cell
        self.wood = False
        self.isPlant = True
        self.isPredator = False


        self.camera = camera

        self.compass = randint(0,3)

        self.biomaterial = 10


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.xPos + self.camera.xpos), int(self.yPos + self.camera.ypos)), self.size)

    def move(self):
        return False

    def attack_agent(self, defender_agent):
        return False

    def grow(self):

        if self.biomaterial < 25:

            self.biomaterial += randint(0, 5)
