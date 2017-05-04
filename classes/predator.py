import pygame

from random import randint

class Predator:

    def __init__(self, cell, color, camera):
        self.xPos = cell.xPos
        self.yPos = cell.yPos
        self.size = 6
        self.counter = 0
        self.color = color
        self.cell = cell

        self.isPlant = False

        self.camera = camera

        self.compass = randint(0,3)

        self.biomaterial = 100


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.xPos + self.camera.xpos), int(self.yPos + self.camera.ypos)), self.size)


    def move(self):
        self.counter +=1

        temp = randint(0,3)
        if temp != self.compass:
            temp = randint(0,3)

        if self.counter >= 250:
            self.counter = 0
            self.compass = randint(0, 3)

        # Cell goes right
        if temp == 0:
            return 0        # Cell goes left
        if temp == 1:
            return 1        # Cell goes
        if temp == 2:
            return 2        # Cell goes
        if temp == 3:
            return 3


    def attack_agent(self, defender_agent):

        if self.biomaterial > 0:
            taken_biomaterial = randint(0,20)

            if defender_agent.biomaterial >= taken_biomaterial:
                self.biomaterial += taken_biomaterial
                defender_agent.biomaterial -= taken_biomaterial
            else:
                self.biomaterial += defender_agent.biomaterial
                defender_agent.biomaterial = 0

            #print("[Attacker Agent Biomaterial] "+ str(self.biomaterial))
            #print("[Defender Agent Biomaterial] "+ str(defender_agent.biomaterial))
