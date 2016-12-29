import pygame

from random import randint


class NewObject:

    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.size = 10
        self.counter = 0

        self.compass = randint(0,3)

        self.Red = (255, 0, 0)

        self.biomaterial = 100

    def draw(self, screen):
        pygame.draw.rect(screen, self.Red, [self.xpos, self.ypos, self.size, self.size])

    def move(self):
        self.counter +=1
        #self.biomaterial += 1
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
            print("Compass has been changed")


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
        self.biomaterial += 1
        temp = randint(0,100)

        if temp == 0:
            self.readyToGrow = True


