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
        self.distance = 20
        self.cellSize = 20
        self.cellHalfSize = self.cellSize/2
        self.cellBorder = 1
        self.color = (100, 100, 100)
        self.colorhighlight = (255,255,250)
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


                #Highlights the occupied cells
                """
                if self.grid[i][j].occupant == 0:

                    pygame.draw.rect(self.screen, self.color, position, self.cellBorder)

                else:

                    pygame.draw.rect(self.screen, self.colorhighlight, position, self.cellBorder)

                """

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

    def top_cell(self, cell):

        if cell.yIndex > 0:
            xIndex = cell.xIndex
            yIndex = cell.yIndex - 1

            return self.grid[xIndex][yIndex]
        else:
            return 9

    def bottom_cell(self, cell):

        if cell.yIndex < self.size - 1:
            xIndex = cell.xIndex
            yIndex = cell.yIndex + 1

            return self.grid[xIndex][yIndex]
        else:
            return 9

    def right_cell(self, cell):

        if cell.xIndex < self.size - 1:
            xIndex = cell.xIndex + 1
            yIndex = cell.yIndex

            return self.grid[xIndex][yIndex]
        else:
            return 9

    def left_cell(self, cell):

        if cell.xIndex > 0:
            xIndex = cell.xIndex - 1
            yIndex = cell.yIndex

            return self.grid[xIndex][yIndex]
        else:
            return 9
