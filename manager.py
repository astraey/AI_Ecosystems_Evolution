from random import randint
from classes.plant import Plant
from classes.predator import Predator
from classes.camera import Camera
from classes.cell import Cell
from classes.grid import Grid

import pygame
import sys
import numpy
class Manager:

    def __init__(self, screen, height, width):
        self.predatorlist = []
        self.plantlist = []
        self.screen = screen
        self.height = height
        self.width = width

        self.grey = (100, 100, 100)

        self.camera_focus = 0

        self.camera = Camera(0, 0)

        # We declare a grid of 30*30
        self.grid = Grid(30, self.camera, self.screen)

    def predator_move_reproduce(self):
        for element in self.predatorlist:
            element.move()
            if element.biomaterial > 200:
                element.biomaterial -= 100
                self.predatorlist.append(Predator(element.xpos, element.ypos, element.color, self.camera))

    def camera_move(self):
        if self.camera.moving_down:
            self.camera.ypos += self.camera.moving_distance

        if self.camera.moving_up:
            self.camera.ypos -= self.camera.moving_distance

        if self.camera.moving_right:
            self.camera.xpos += self.camera.moving_distance

        if self.camera.moving_left:
            self.camera.xpos -= self.camera.moving_distance


    def plant_reproduce(self):


        for element in self.plantlist:
            element.grow()

            if element.readyToGrow and element.biomaterial >= 25:


                if element.biomaterial < 40:
                    element.biomaterial += 1

                if element.biomaterial >= 40 and not element.wood:
                    element.is_wood()
                    if element.wood:
                        element.color = (128, 64, 0)

                temp = randint(0, 3)
                position_free = True
                new_plant_xpos = 0
                new_plant_ypos = 0

                if temp == 0:
                    new_plant_xpos = element.xpos + element.size
                    new_plant_ypos = element.ypos + element.size

                if temp == 1:
                    new_plant_xpos = element.xpos - element.size
                    new_plant_ypos = element.ypos + element.size

                if temp == 2:
                    new_plant_xpos = element.xpos + element.size
                    new_plant_ypos = element.ypos - element.size

                if temp == 3:
                    new_plant_xpos = element.xpos - element.size
                    new_plant_ypos = element.ypos - element.size

                for element2 in self.plantlist:
                    if abs(new_plant_xpos - element2.xpos) < 10 and abs(new_plant_ypos - element2.ypos) < 10:
                        position_free = False

                if position_free:
                    self.addplant(new_plant_xpos, new_plant_ypos, self.camera)
                    print("New Plant at " + str(new_plant_xpos) + ", " + str(new_plant_ypos) + "  No Plants: " + str(len(self.plantlist)))

                element.readyToGrow = False

            if element.readyToGrow and element.biomaterial < 25:
                element.biomaterial += 1
                if element.biomaterial == 25:
                    element.color = (0, 77, 0)
                element.readyToGrow = False

    def eating_manager(self):

        for predator in self.predatorlist:
            for element in self.plantlist:
                if abs(predator.xpos - element.xpos) < 10 and abs(predator.ypos - element.ypos) < 10 and not element.wood:
                    predator.biomaterial += element.biomaterial
                    self.plantlist.remove(element)
                    print("Predator's new Biomaterial: " + str(predator.biomaterial))

    def fill_screen_black(self):
        self.screen.fill((0,0,0))

    def render_predators_plants(self):

        # (0, 0, 0) is the RGB codification for Black

        for i in range(0, len(self.plantlist)):
            self.plantlist[i].draw(self.screen)

        for i in range(0, len(self.predatorlist)):
            self.predatorlist[i].draw(self.screen)

    def generator(self):

        self.predatorgenerator()

        self.plantgenerator()


    def entity_up(self, index):

        xIndex = self.grid.agents[index].cell.xIndex
        yIndex = self.grid.agents[index].cell.yIndex -1

        print("xIndex: "+ str(xIndex)+"\n")
        print("yIndex: "+ str(yIndex)+"\n\n")

        self.grid.grid[xIndex][yIndex].occupant = self.grid.agents[index]
        self.grid.agents[index].cell.occupant = 0
        self.grid.agents[index].cell = self.grid.grid[xIndex][yIndex]

        print("old Xpos: "+ str(self.grid.agents[index].xPos)+"\n")
        print("old Ypos: "+ str(self.grid.agents[index].yPos)+"\n\n")

        self.grid.agents[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.agents[index].yPos = self.grid.grid[xIndex][yIndex].yPos

        print("new Xpos: "+ str(self.grid.agents[index].xPos)+"\n")
        print("new Ypos: "+ str(self.grid.agents[index].yPos)+"\n\n")

    def entity_down(self, index):

        xIndex = self.grid.agents[index].cell.xIndex
        yIndex = self.grid.agents[index].cell.yIndex +1

        print("xIndex: "+ str(xIndex)+"\n")
        print("yIndex: "+ str(yIndex)+"\n\n")

        self.grid.grid[xIndex][yIndex].occupant = self.grid.agents[index]
        self.grid.agents[index].cell.occupant = 0
        self.grid.agents[index].cell = self.grid.grid[xIndex][yIndex]

        print("old Xpos: "+ str(self.grid.agents[index].xPos)+"\n")
        print("old Ypos: "+ str(self.grid.agents[index].yPos)+"\n\n")

        self.grid.agents[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.agents[index].yPos = self.grid.grid[xIndex][yIndex].yPos

        print("new Xpos: "+ str(self.grid.agents[index].xPos)+"\n")
        print("new Ypos: "+ str(self.grid.agents[index].yPos)+"\n\n")

    def entity_left(self, index):

        xIndex = self.grid.agents[index].cell.xIndex -1
        yIndex = self.grid.agents[index].cell.yIndex

        print("xIndex: "+ str(xIndex)+"\n")
        print("yIndex: "+ str(yIndex)+"\n\n")

        self.grid.grid[xIndex][yIndex].occupant = self.grid.agents[index]
        self.grid.agents[index].cell.occupant = 0
        self.grid.agents[index].cell = self.grid.grid[xIndex][yIndex]

        print("old Xpos: "+ str(self.grid.agents[index].xPos)+"\n")
        print("old Ypos: "+ str(self.grid.agents[index].yPos)+"\n\n")

        self.grid.agents[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.agents[index].yPos = self.grid.grid[xIndex][yIndex].yPos

        print("new Xpos: "+ str(self.grid.agents[index].xPos)+"\n")
        print("new Ypos: "+ str(self.grid.agents[index].yPos)+"\n\n")

    def entity_right(self, index):

        xIndex = self.grid.agents[index].cell.xIndex +1
        yIndex = self.grid.agents[index].cell.yIndex

        print("xIndex: "+ str(xIndex)+"\n")
        print("yIndex: "+ str(yIndex)+"\n\n")

        self.grid.grid[xIndex][yIndex].occupant = self.grid.agents[index]
        self.grid.agents[index].cell.occupant = 0
        self.grid.agents[index].cell = self.grid.grid[xIndex][yIndex]

        print("old Xpos: "+ str(self.grid.agents[index].xPos)+"\n")
        print("old Ypos: "+ str(self.grid.agents[index].yPos)+"\n\n")

        self.grid.agents[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.agents[index].yPos = self.grid.grid[xIndex][yIndex].yPos

        print("new Xpos: "+ str(self.grid.agents[index].xPos)+"\n")
        print("new Ypos: "+ str(self.grid.agents[index].yPos)+"\n\n")

    def position_check(self):

        print("Starting Position Test")

        flag2 = False
        for element in self.plantlist:
            flag = 0
            for element2 in self.plantlist:
                if element.xpos == element2.xpos and element.ypos == element2.ypos:
                    flag += 1

            if flag >= 2:
                print("ERROR DETECTED")
                flag2 = True

        if flag2:
            print("Errors were Detected")
        else:
            print("No errors Were Detected")

    def event_management(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.camera.moving_right = True

            if event.key == pygame.K_RIGHT:
                self.camera.moving_left = True

            if event.key == pygame.K_UP:
                self.camera.moving_down = True

            if event.key == pygame.K_DOWN:
                self.camera.moving_up = True

            if event.key == pygame.K_a:
                self.entity_left(1)

            if event.key == pygame.K_d:
                self.entity_right(1)

            if event.key == pygame.K_w:
                self.entity_up(1)

            if event.key == pygame.K_s:
                self.entity_down(1)

            if event.key == pygame.K_t:
                self.position_check()

            if event.key == pygame.K_ESCAPE:
                sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.camera.moving_right = False

            if event.key == pygame.K_RIGHT:
                self.camera.moving_left = False

            if event.key == pygame.K_UP:
                self.camera.moving_down = False

            if event.key == pygame.K_DOWN:
                self.camera.moving_up = False

    def test_array_objects(self):
        #self.grid.testFunction()
        self.add_agent(Predator(self.grid.grid[1][1].xPos, self.grid.grid[1][1].xPos, self.grid.grid[1][1], (54,111,200), self.camera), 1, 1)
        self.add_agent(Predator(self.grid.grid[2][2].xPos, self.grid.grid[2][2].xPos, self.grid.grid[2][2], (54,111,200), self.camera), 2, 2)
        self.add_agent(Predator(self.grid.grid[28][28].xPos, self.grid.grid[28][28].xPos, self.grid.grid[28][28], (54,111,200), self.camera), 28, 28)



    def draw_grid(self):
        self.grid.draw()

    def draw_agents(self):
        for agent in self.grid.agents:
            agent.draw(self.screen)

    def add_agent(self, agent, xPos, yPos):
        self.grid.agents.append(agent)
        self.grid.grid[xPos][yPos].occupant = agent
