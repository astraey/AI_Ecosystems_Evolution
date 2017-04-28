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
        self.pause = False

        self.grey = (100, 100, 100)

        self.camera_focus = 0

        self.camera = Camera(0, 0)

        # We declare a grid of 30*30
        self.grid = Grid(30, self.camera, self.screen)

    def icon_setter(self):

        icon = pygame.image.load('media/icon.png')

        pygame.display.set_icon(icon)

        pygame.display.set_caption("Ecosystem Simulator")

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

    def paint_screen_black(self):
        self.screen.fill((0,0,0))

    # entity_dir receives an index corresponding to an agent in the agent list and moves it

    def entity_up(self, index):

        xIndex = self.grid.agents[index].cell.xIndex
        yIndex = self.grid.agents[index].cell.yIndex -1

        self.grid.grid[xIndex][yIndex].occupant = self.grid.agents[index]
        self.grid.agents[index].cell.occupant = 0
        self.grid.agents[index].cell = self.grid.grid[xIndex][yIndex]

        self.grid.agents[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.agents[index].yPos = self.grid.grid[xIndex][yIndex].yPos

    def entity_down(self, index):

        xIndex = self.grid.agents[index].cell.xIndex
        yIndex = self.grid.agents[index].cell.yIndex +1

        self.grid.grid[xIndex][yIndex].occupant = self.grid.agents[index]
        self.grid.agents[index].cell.occupant = 0
        self.grid.agents[index].cell = self.grid.grid[xIndex][yIndex]

        self.grid.agents[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.agents[index].yPos = self.grid.grid[xIndex][yIndex].yPos

    def entity_left(self, index):

        xIndex = self.grid.agents[index].cell.xIndex -1
        yIndex = self.grid.agents[index].cell.yIndex

        self.grid.grid[xIndex][yIndex].occupant = self.grid.agents[index]
        self.grid.agents[index].cell.occupant = 0
        self.grid.agents[index].cell = self.grid.grid[xIndex][yIndex]

        self.grid.agents[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.agents[index].yPos = self.grid.grid[xIndex][yIndex].yPos

    def entity_right(self, index):

        xIndex = self.grid.agents[index].cell.xIndex +1
        yIndex = self.grid.agents[index].cell.yIndex

        self.grid.grid[xIndex][yIndex].occupant = self.grid.agents[index]
        self.grid.agents[index].cell.occupant = 0
        self.grid.agents[index].cell = self.grid.grid[xIndex][yIndex]

        self.grid.agents[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.agents[index].yPos = self.grid.grid[xIndex][yIndex].yPos

    # agent_dir receives an agent as a parameter and moves it in the grid

    def agent_up(self, agent):

        xIndex = agent.cell.xIndex
        yIndex = agent.cell.yIndex -1

        self.grid.grid[xIndex][yIndex].occupant = agent
        agent.cell.occupant = 0
        agent.cell = self.grid.grid[xIndex][yIndex]

        agent.xPos = self.grid.grid[xIndex][yIndex].xPos
        agent.yPos = self.grid.grid[xIndex][yIndex].yPos

    def agent_down(self, agent):

        xIndex = agent.cell.xIndex
        yIndex = agent.cell.yIndex +1

        self.grid.grid[xIndex][yIndex].occupant = agent
        agent.cell.occupant = 0
        agent.cell = self.grid.grid[xIndex][yIndex]


        agent.xPos = self.grid.grid[xIndex][yIndex].xPos
        agent.yPos = self.grid.grid[xIndex][yIndex].yPos

    def agent_left(self, agent):

        xIndex = agent.cell.xIndex -1
        yIndex = agent.cell.yIndex

        self.grid.grid[xIndex][yIndex].occupant = agent
        agent.cell.occupant = 0
        agent.cell = self.grid.grid[xIndex][yIndex]

        agent.xPos = self.grid.grid[xIndex][yIndex].xPos
        agent.yPos = self.grid.grid[xIndex][yIndex].yPos

    def agent_right(self, agent):

        xIndex = agent.cell.xIndex +1
        yIndex = agent.cell.yIndex


        self.grid.grid[xIndex][yIndex].occupant = agent
        agent.cell.occupant = 0
        agent.cell = self.grid.grid[xIndex][yIndex]

        agent.xPos = self.grid.grid[xIndex][yIndex].xPos
        agent.yPos = self.grid.grid[xIndex][yIndex].yPos

    def agent_remove(self, agent):
        if agent in self.grid.agents:
            agent.cell.occupant = 0
            self.grid.agents.remove(agent)

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

            if event.key == pygame.K_e:
                self.agent_remove(self.grid.agents[0])
                print("Agent Deleted")

            if event.key == pygame.K_p:
                self.pause_button()

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

    def test_add_predators(self):

        self.add_agent(Predator(self.grid.grid[1][1].xPos, self.grid.grid[1][1].xPos, self.grid.grid[1][1], (244, 78, 66), self.camera), 1, 1)
        self.add_agent(Predator(self.grid.grid[2][2].xPos, self.grid.grid[2][2].xPos, self.grid.grid[2][2], (113, 209, 62), self.camera), 2, 2)
        self.add_agent(Predator(self.grid.grid[8][8].xPos, self.grid.grid[8][8].xPos, self.grid.grid[8][8], (54,111,200), self.camera), 8, 8)
        self.add_agent(Predator(self.grid.grid[9][9].xPos, self.grid.grid[9][9].xPos, self.grid.grid[9][9], (255, 250, 0), self.camera), 9, 9)
        self.add_agent(Predator(self.grid.grid[7][7].xPos, self.grid.grid[7][7].xPos, self.grid.grid[7][7], (200, 56, 200), self.camera), 7, 7)


    def draw_grid(self):

        #Highlights occupied cells
        self.grid.draw_highlighted()

        #self.grid.draw()

    def draw_agents(self):
        for agent in self.grid.agents:
            agent.draw(self.screen)

    def add_agent(self, agent, xPos, yPos):
        self.grid.agents.append(agent)
        self.grid.grid[xPos][yPos].occupant = agent

    def agent_mover(self, agent):

        compass = agent.move()

        if compass == 0 and agent.cell.yIndex > 0 and self.grid.top_cell(agent.cell).occupant == 0:
            self.agent_up(agent)
        elif compass == 1 and agent.cell.yIndex < self.grid.size - 1 and self.grid.bottom_cell(agent.cell).occupant == 0:
            self.agent_down(agent)
        elif compass == 2 and agent.cell.xIndex < self.grid.size - 1 and self.grid.right_cell(agent.cell).occupant == 0:
            self.agent_right(agent)
        elif compass == 3 and agent.cell.xIndex > 0 and self.grid.left_cell(agent.cell).occupant == 0:
            self.agent_left(agent)

    def move_agents(self):
        for agent in self.grid.agents:
            self.agent_mover(agent)

    def agent_attacker(self):
        for agent in self.grid.agents:
            self.grid.neighbour_agent(agent)

    def pause_button(self):


        if not self.pause:
            print("Game has been paused")
        else:
            print("Game has been resumed")

        self.pause = not self.pause
