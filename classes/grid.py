import pygame, numpy, copy
from classes.cell import Cell
from classes.plant import Plant
from classes.predator import Predator

class Grid:

    def __init__(self, size, camera, screen):
        self.predatorlist = []
        self.plantlist = []
        self.agents = []
        self.size = size
        self.distance = 50
        self.cellSize = 50
        self.cellHalfSize = self.cellSize/2
        self.cellBorder = 1
        self.color = (100, 100, 100)
        self.camera = camera
        self.screen = screen
        self.grid = []
        self.grid_builder()




    def grid_builder(self):
        for i in range(0, self.size):
            temp = []
            for j in range(0, self.size):
                temp.append(Cell(i, j, i * self.distance, j * self.distance))
            self.grid.append(temp)



    def draw(self):

        for i in range(0, self.size):
            for j in range(0, self.size):

                position = [ int(self.grid[i][j].xPos - self.cellHalfSize + self.camera.xpos),
                             int(self.grid[i][j].yPos - self.cellHalfSize + self.camera.ypos),
                             self.cellSize,
                             self.cellSize]

                pygame.draw.rect(self.screen, self.color, position, self.cellBorder)



    def testFunction(self):

        """
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.grid[i][j].printer()
        """
        temp = Predator(self.grid[0][0].xPos, self.grid[0][0].xPos, (200,200,200), self.camera)
        self.grid[0][0].occupant = temp
        self.agents.append(temp)
        #self.grid[0][0].occupant.draw(self.screen)
