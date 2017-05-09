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
        self.cellSize = 5
        self.distance = self.cellSize
        self.cellSize = self.cellSize
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


    #Doesn't highlight the occupied cells

    def draw(self):

        for i in range(0, self.size):
            for j in range(0, self.size):

                position = [ int(self.grid[i][j].xPos - self.cellHalfSize + self.camera.xpos),
                             int(self.grid[i][j].yPos - self.cellHalfSize + self.camera.ypos),
                             self.cellSize,
                             self.cellSize]


                pygame.draw.rect(self.screen, self.color, position, self.cellBorder)



    #Highlights the occupied cells
    def draw_highlighted(self):

        for i in range(0, self.size):
            for j in range(0, self.size):

                position = [ int(self.grid[i][j].xPos - self.cellHalfSize + self.camera.xpos),
                             int(self.grid[i][j].yPos - self.cellHalfSize + self.camera.ypos),
                             self.cellSize,
                             self.cellSize]




                if self.grid[i][j].occupant == 0:

                    pygame.draw.rect(self.screen, self.color, position, self.cellBorder)

                else:

                    pygame.draw.rect(self.screen, self.colorhighlight, position, self.cellBorder)

    def draw_grid_frame(self):

        for i in range(0, self.size):
            for j in range(0, self.size):

                if i == 0 or j == 0 or i == self.size - 1 or j == self.size - 1:

                    position = [ int(self.grid[i][j].xPos - self.cellHalfSize + self.camera.xpos),
                                 int(self.grid[i][j].yPos - self.cellHalfSize + self.camera.ypos),
                                 self.cellSize,
                                 self.cellSize]

                    pygame.draw.rect(self.screen, self.color, position, self.cellBorder)


    def top_cell(self, cell):

        xIndex = cell.xIndex
        yIndex = cell.yIndex - 1

        return self.grid[xIndex][yIndex]

    def bottom_cell(self, cell):


        xIndex = cell.xIndex
        yIndex = cell.yIndex + 1

        return self.grid[xIndex][yIndex]


    def right_cell(self, cell):

        xIndex = cell.xIndex + 1
        yIndex = cell.yIndex

        return self.grid[xIndex][yIndex]

    def left_cell(self, cell):

        xIndex = cell.xIndex - 1
        yIndex = cell.yIndex

        return self.grid[xIndex][yIndex]

    def neighbour_agent(self, agent):
        return_data = []
        xIndex = agent.cell.xIndex
        yIndex = agent.cell.yIndex


        if  0 < yIndex and 0 < xIndex and self.grid[xIndex-1][yIndex-1].occupant != 0:
            #print("Found an occupant at the top left corner ["+ str(xIndex-1) +", "+ str(yIndex-1) +"]")
            return_data.append(self.grid[xIndex-1][yIndex-1].occupant)

        if  0 < yIndex and self.grid[xIndex][yIndex-1].occupant != 0:
            #print("Found an occupant at the top ["+ str(xIndex) +", "+ str(yIndex-1) +"]")
            return_data.append(self.grid[xIndex][yIndex-1].occupant)

        if  0 < yIndex and xIndex < self.size -1 and self.grid[xIndex+1][yIndex-1].occupant != 0:
            #print("Found an occupant at the top right corner ["+ str(xIndex+1) +", "+ str(yIndex-1) +"]")
            return_data.append(self.grid[xIndex+1][yIndex-1].occupant)

        if  0 < xIndex and self.grid[xIndex-1][yIndex].occupant != 0:
            #print("Found an occupant at the left ["+ str(xIndex-1) +", "+ str(yIndex) +"]")
            return_data.append(self.grid[xIndex-1][yIndex].occupant)

        if  xIndex < self.size -1 and self.grid[xIndex+1][yIndex].occupant != 0:
            #print("Found an occupant at the right ["+ str(xIndex+1) +", "+ str(yIndex) +"]")
            return_data.append(self.grid[xIndex+1][yIndex].occupant)
#
        if  yIndex < self.size -1 and 0 < xIndex and self.grid[xIndex-1][yIndex+1].occupant != 0:
            #print("Found an occupant at the bottom left corner ["+ str(xIndex-1) +", "+ str(yIndex+1) +"]")
            return_data.append(self.grid[xIndex-1][yIndex+1].occupant)

        if  yIndex < self.size -1 and self.grid[xIndex][yIndex+1].occupant != 0:
            #print("Found an occupant at the bottom ["+ str(xIndex) +", "+ str(yIndex+1) +"]")
            return_data.append(self.grid[xIndex][yIndex+1].occupant)

        if  yIndex < self.size -1 and xIndex < self.size -1 and self.grid[xIndex+1][yIndex+1].occupant != 0:
            #print("Found an occupant at the bottom right corner ["+ str(xIndex+1) +", "+ str(yIndex+1) +"]")
            return_data.append(self.grid[xIndex+1][yIndex+1].occupant)

        return return_data

    def free_cell(self, agent):

        return_data = []

        xIndex = agent.cell.xIndex
        yIndex = agent.cell.yIndex


        if  0 < yIndex and 0 < xIndex and self.grid[xIndex-1][yIndex-1].occupant == 0:
            #print("Found a free cell at the top left corner ["+ str(xIndex-1) +", "+ str(yIndex-1) +"]")
            return_data.append(self.grid[xIndex-1][yIndex-1])

        if  0 < yIndex and self.grid[xIndex][yIndex-1].occupant == 0:
            #print("Found a free cell at the top ["+ str(xIndex) +", "+ str(yIndex-1) +"]")
            return_data.append(self.grid[xIndex][yIndex-1])

        if  0 < yIndex and xIndex < self.size -1 and self.grid[xIndex+1][yIndex-1].occupant == 0:
            #print("Found a free cell at the top right corner ["+ str(xIndex+1) +", "+ str(yIndex-1) +"]")
            return_data.append(self.grid[xIndex+1][yIndex-1])

        if  0 < xIndex and self.grid[xIndex-1][yIndex].occupant == 0:
            #print("Found a free cell at the left ["+ str(xIndex-1) +", "+ str(yIndex) +"]")
            return_data.append(self.grid[xIndex-1][yIndex])

        if  xIndex < self.size -1 and self.grid[xIndex+1][yIndex].occupant == 0:
            #print("Found a free cell at the right ["+ str(xIndex+1) +", "+ str(yIndex) +"]")
            return_data.append(self.grid[xIndex+1][yIndex])
#
        if  yIndex < self.size -1 and 0 < xIndex and self.grid[xIndex-1][yIndex+1].occupant == 0:
            #print("Found a free cell at the bottom left corner ["+ str(xIndex-1) +", "+ str(yIndex+1) +"]")
            return_data.append(self.grid[xIndex-1][yIndex+1])

        if  yIndex < self.size -1 and self.grid[xIndex][yIndex+1].occupant == 0:
            #print("Found a free cell at the bottom ["+ str(xIndex) +", "+ str(yIndex+1) +"]")
            return_data.append(self.grid[xIndex][yIndex+1])

        if  yIndex < self.size -1 and xIndex < self.size -1 and self.grid[xIndex+1][yIndex+1].occupant == 0:
            #print("Found a free cell at the bottom right corner ["+ str(xIndex+1) +", "+ str(yIndex+1) +"]")
            return_data.append(self.grid[xIndex+1][yIndex+1])

        return return_data
