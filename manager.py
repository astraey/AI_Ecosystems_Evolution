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

        self.screen = screen
        self.height = height
        self.width = width
        self.pause = False

        self.counter = 0

        self.grey = (100, 100, 100)

        self.camera_focus = 0

        self.camera = Camera(0, 0)

        #Defines the size of the grid
        self.grid_size = 195


        # We declare a grid of 30*30
        self.grid = Grid(self.grid_size, self.camera, self.screen)

    def icon_setter(self):

        icon = pygame.image.load('media/icon.png')

        pygame.display.set_icon(icon)

        pygame.display.set_caption("Ecosystem Simulator")

    def camera_move(self):
        if self.camera.moving_down:
            self.camera.ypos += self.camera.moving_distance

        if self.camera.moving_up:
            self.camera.ypos -= self.camera.moving_distance

        if self.camera.moving_right:
            self.camera.xpos += self.camera.moving_distance

        if self.camera.moving_left:
            self.camera.xpos -= self.camera.moving_distance

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
            #print("Agent KILLED")

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
                #print("Agent Deleted")

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


    def random_add_predators(self, amount):

        for i in range(0, amount):
            xIndex = randint(0, self.grid_size -1)
            yIndex = randint(0, self.grid_size -1)

            if self.grid.grid[xIndex][yIndex].occupant != 0:

                continue

            targetCell = self.grid.grid[xIndex][yIndex]

            color = (randint(0,255),randint(0,255),randint(0,255))

            self.add_agent(Predator(targetCell, color, self.camera), xIndex, yIndex)

    def random_add_plants(self, amount):

        for i in range(0, amount):
            xIndex = randint(0, self.grid_size -1)
            yIndex = randint(0, self.grid_size -1)

            if self.grid.grid[xIndex][yIndex].occupant != 0:

                continue

            targetCell = self.grid.grid[xIndex][yIndex]


            self.add_agent(Plant(targetCell, self.camera), xIndex, yIndex)



    def draw_grid(self):

        #Highlights occupied cells
        self.grid.draw_highlighted()

        #Doesn't highlight occupied cells
        #self.grid.draw()

    def draw_grid_frame(self):

        self.grid.draw_grid_frame()
        #self.grid.draw_grid_frame2()

    def draw_agents(self):
        for agent in self.grid.agents:
            agent.draw(self.screen)

    def add_agent(self, agent, xPos, yPos):

        self.grid.grid[xPos][yPos].occupant = agent
        self.grid.agents.append(agent)

    def agent_mover(self, agent):

        if not agent.isPlant:
            compass = agent.move()

            if compass == 0 and agent.cell.yIndex > 0 and self.grid.top_cell(agent.cell).occupant == 0:
                self.agent_up(agent)
            elif compass == 1 and agent.cell.yIndex < self.grid.size - 1 and self.grid.bottom_cell(agent.cell).occupant == 0:
                self.agent_down(agent)
            elif compass == 2 and agent.cell.xIndex < self.grid.size - 1 and self.grid.right_cell(agent.cell).occupant == 0:
                self.agent_right(agent)
            elif compass == 3 and agent.cell.xIndex > 0 and self.grid.left_cell(agent.cell).occupant == 0:
                self.agent_left(agent)

            # Moving Cost

            if self.counter > 10:

                agent.biomaterial -= 1
                self.counter = 0
            else:

                self.counter += 1


    def move_agents(self):
        for agent in self.grid.agents:
            self.agent_mover(agent)

    def agent_attacker(self):
        for agent in self.grid.agents:

            if not agent.isPlant:
                neighbours = self.grid.neighbour_agent(agent)
                if neighbours != []:
                    agent.attack_agent(neighbours[randint(0,len(neighbours)-1)])
                for neighbour in neighbours:
                    agent.attack_agent(neighbour)
            else:
                agent.grow()

    def agent_killer(self):
        for agent in self.grid.agents:
            if agent.biomaterial <= 0:
                self.agent_remove(agent)

    def agent_reproducer(self):
        for agent in self.grid.agents:
            if agent.biomaterial >= 200 and not agent.isPlant:

                free_cells = self.grid.free_cell(agent)

                if free_cells != []:

                    randomFreeCellIndex = 0

                    agent.biomaterial -= 100
                    self.add_agent(Predator(free_cells[randomFreeCellIndex], agent.color, self.camera), free_cells[randomFreeCellIndex].xIndex, free_cells[randomFreeCellIndex].yIndex)


            elif agent.biomaterial >= 20 and agent.isPlant:

                free_cells = self.grid.free_cell(agent)

                if free_cells != []:

                    randomFreeCellIndex = 0

                    agent.biomaterial -= 10
                    self.add_agent(Plant(free_cells[randomFreeCellIndex], self.camera), free_cells[randomFreeCellIndex].xIndex, free_cells[randomFreeCellIndex].yIndex)


    def pause_button(self):

        if not self.pause:
            print("Game has been paused")
        else:
            print("Game has been resumed")

        self.pause = not self.pause

    def checker(self):
        print("***************")
        for i in range(0, self.grid_size):
            for j in range(0, self.grid_size):
                if self.grid.grid[i][j].occupant == 0:
                    print("["+str(i)+", "+str(j)+"] FREE")
                else:
                    print("["+str(i)+", "+str(j)+"] Not Free")

        print("***************")

        for agent in self.grid.agents:
            print("Agent at ["+str(agent.cell.xIndex)+", "+str(agent.cell.yIndex)+"]")

        print("***************")
