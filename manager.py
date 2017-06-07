from random import randint
from fractions import gcd
from classes.plant import Plant
from classes.animal import Animal
from classes.camera import Camera
from classes.cell import Cell
from classes.grid import Grid
from classes.genome import Genome


import pygame
import sys
import numpy
import functools




class Manager:

    def __init__(self, screen, height, width):

        self.screen = screen
        self.height = height
        self.width = width
        self.pause = False
        self.print_stats = False

        self.growingCounter = 0

        self.animal_range = 10

        #Modify this variable to adjust the initial position of the camera, in order
        #to center the grid.
        self.camera_focus = 20

        self.camera = Camera(0 + self.camera_focus, 0 + self.camera_focus)

        #Defines the size of the grid
        self.grid_size = 195


        self.maxWoods = self.grid_size / 2
        self.currentWoods = 0

        self.generations = 0


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

        xIndex = self.grid.animals[index].cell.xIndex
        yIndex = self.grid.animals[index].cell.yIndex -1

        self.grid.grid[xIndex][yIndex].occupant = self.grid.animals[index]
        self.grid.animals[index].cell.occupant = 0
        self.grid.animals[index].cell = self.grid.grid[xIndex][yIndex]

        self.grid.animals[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.animals[index].yPos = self.grid.grid[xIndex][yIndex].yPos

    def entity_down(self, index):

        xIndex = self.grid.animals[index].cell.xIndex
        yIndex = self.grid.animals[index].cell.yIndex +1

        self.grid.grid[xIndex][yIndex].occupant = self.grid.animals[index]
        self.grid.animals[index].cell.occupant = 0
        self.grid.animals[index].cell = self.grid.grid[xIndex][yIndex]

        self.grid.animals[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.animals[index].yPos = self.grid.grid[xIndex][yIndex].yPos

    def entity_left(self, index):

        xIndex = self.grid.animals[index].cell.xIndex -1
        yIndex = self.grid.animals[index].cell.yIndex

        self.grid.grid[xIndex][yIndex].occupant = self.grid.animals[index]
        self.grid.animals[index].cell.occupant = 0
        self.grid.animals[index].cell = self.grid.grid[xIndex][yIndex]

        self.grid.animals[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.animals[index].yPos = self.grid.grid[xIndex][yIndex].yPos

    def entity_right(self, index):

        xIndex = self.grid.animals[index].cell.xIndex +1
        yIndex = self.grid.animals[index].cell.yIndex

        self.grid.grid[xIndex][yIndex].occupant = self.grid.animals[index]
        self.grid.animals[index].cell.occupant = 0
        self.grid.animals[index].cell = self.grid.grid[xIndex][yIndex]

        self.grid.animals[index].xPos = self.grid.grid[xIndex][yIndex].xPos
        self.grid.animals[index].yPos = self.grid.grid[xIndex][yIndex].yPos

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

            if agent.isPlant:
                self.grid.plants.remove(agent)
            else:
                self.grid.animals.remove(agent)
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
                self.entity_left(0)

            if event.key == pygame.K_d:
                self.entity_right(0)

            if event.key == pygame.K_w:
                self.entity_up(0)

            if event.key == pygame.K_s:
                self.entity_down(0)

            if event.key == pygame.K_e:
                self.agent_remove(self.grid.animals[0])
                #print("Agent Deleted")
            if event.key == pygame.K_r:
                self.random_add_animals(1)

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


    def random_add_animals(self, amount):

        for i in range(0, amount):
            xIndex = randint(0, self.grid_size -1)
            yIndex = randint(0, self.grid_size -1)

            if self.grid.grid[xIndex][yIndex].occupant != 0:

                continue

            targetCell = self.grid.grid[xIndex][yIndex]

            color = (randint(0,255),randint(0,255),randint(0,255))

            self.add_agent_animal(Animal(targetCell, color, self.camera, 0, Genome(True)), xIndex, yIndex)

    def random_add_plants(self, amount):

        for i in range(0, amount):
            xIndex = randint(0, self.grid_size -1)
            yIndex = randint(0, self.grid_size -1)

            if self.grid.grid[xIndex][yIndex].occupant != 0:

                continue

            targetCell = self.grid.grid[xIndex][yIndex]


            self.add_agent_plant(Plant(targetCell, self.camera), xIndex, yIndex)



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

    def add_agent_plant(self, agent, xPos, yPos):

        self.grid.grid[xPos][yPos].occupant = agent
        self.grid.agents.append(agent)
        self.grid.plants.append(agent)

    def add_agent_animal(self, agent, xPos, yPos):

        self.grid.grid[xPos][yPos].occupant = agent
        self.grid.agents.append(agent)
        self.grid.animals.append(agent)


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

        # Moving Cost

        if agent.movementCounter > 15:
            agent.biomaterial -= 1
            agent.movementCounter = 0

        else:
            agent.movementCounter += 1

    def update_animals_radar(self):

        for animal in self.grid.animals:
            #update animals radars
            self.update_animal_radar(animal)
            animal.update_genome_environment_information()


    def update_animal_radar(self, agent):
        #The closest of each type should be selected.
        xIndex = agent.cell.xIndex
        yIndex = agent.cell.yIndex

        #A base distance, so big that doesn't interfere with the algorithm
        closestPlantDistance = 300
        closestAnimalDistance = 300

        #Each position correspond to the directions North, South, East and West respectively
        closestPlantDirection = (False, False, False, False)
        closestAnimalDirection = (False, False, False, False)


        #print("*******************Animal North Radar Update STARTED*******************")
        #print("Starting pos: ["+str(xIndex)+", "+str(yIndex)+"]")


        #North
        for i in range(1, self.animal_range + 1):


            targetXIndex = xIndex
            targetYIndex = yIndex - i

            #Right
            for j in range(0,i):
                targetXIndex = xIndex + j
                if 0 <= targetXIndex < self.grid_size and 0 <= targetYIndex < self.grid_size:
                    #print("Cheking pos: ["+str(targetXIndex)+", "+str(targetYIndex)+"]")
                    if self.grid.grid[targetXIndex][targetYIndex].occupant != 0:


                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isPlant and not self.grid.grid[targetXIndex][targetYIndex].occupant.wood:
                            #print("We have detected a plant!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestPlantDistance > dist:
                                #print("++++++++++++NEW CLOSEST PLANT AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestPlantDirection = (True, False, False, False)
                                closestPlantDistance = dist

                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isAnimal:
                            #print("We have detected a animal!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestAnimalDistance > dist:
                                #print("++++++++++++NEW CLOSEST ANIMAL AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestAnimalDirection = (True, False, False, False)
                                closestAnimalDistance = dist

            #Left, starts from 1 instad of 0 so it doesn't check the middle cell again
            for j in range(1,i):
                targetXIndex = xIndex - j
                if 0 <= targetXIndex < self.grid_size and 0 <= targetYIndex < self.grid_size:
                    #print("Cheking pos: ["+str(targetXIndex)+", "+str(targetYIndex)+"]")
                    if self.grid.grid[targetXIndex][targetYIndex].occupant != 0:


                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isPlant and not self.grid.grid[targetXIndex][targetYIndex].occupant.wood:
                            #print("We have detected a plant!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestPlantDistance > dist:
                                #print("++++++++++++NEW CLOSEST PLANT AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestPlantDirection = (True, False, False, False)
                                closestPlantDistance = dist

                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isAnimal:
                            #print("We have detected a animal!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestAnimalDistance > dist:
                                #print("++++++++++++NEW CLOSEST ANIMAL AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestAnimalDirection = (True, False, False, False)
                                closestAnimalDistance = dist


        #print("*******************Animal North Radar Update FINISHED*******************\n")

        #print("*******************Animal South Radar Update STARTED*******************")
        #print("Starting pos: ["+str(xIndex)+", "+str(yIndex)+"]")


        #South
        for i in range(1, self.animal_range + 1):


            targetXIndex = xIndex
            targetYIndex = yIndex + i

            #Right
            for j in range(0,i):
                targetXIndex = xIndex + j
                if 0 <= targetXIndex < self.grid_size and 0 <= targetYIndex < self.grid_size:
                    #print("Cheking pos: ["+str(targetXIndex)+", "+str(targetYIndex)+"]")
                    if self.grid.grid[targetXIndex][targetYIndex].occupant != 0:


                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isPlant and not self.grid.grid[targetXIndex][targetYIndex].occupant.wood:
                            #print("We have detected a plant!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestPlantDistance > dist:
                                #print("++++++++++++NEW CLOSEST PLANT AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestPlantDirection = (False, True, False, False)
                                closestPlantDistance = dist

                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isAnimal:
                            #print("We have detected a animal!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestAnimalDistance > dist:
                                #print("++++++++++++NEW CLOSEST ANIMAL AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestAnimalDirection = (False, True, False, False)
                                closestAnimalDistance = dist


            #Left, starts from 1 instad of 0 so it doesn't check the middle cell again
            for j in range(1,i):
                targetXIndex = xIndex - j
                if 0 <= targetXIndex < self.grid_size and 0 <= targetYIndex < self.grid_size:
                    #print("Cheking pos: ["+str(targetXIndex)+", "+str(targetYIndex)+"]")
                    if self.grid.grid[targetXIndex][targetYIndex].occupant != 0:


                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isPlant and not self.grid.grid[targetXIndex][targetYIndex].occupant.wood:
                            #print("We have detected a plant!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestPlantDistance > dist:
                                #print("++++++++++++NEW CLOSEST PLANT AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestPlantDirection = (False, True, False, False)
                                closestPlantDistance = dist

                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isAnimal:
                            #print("We have detected a Animal!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestAnimalDistance > dist:
                                #print("++++++++++++NEW CLOSEST ANIMAL AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestAnimalDirection = (False, True, False, False)
                                closestAnimalDistance = dist


        #print("*******************Animal South Radar Update FINISHED*******************\n")

        #print("*******************Animal East Radar Update STARTED*******************")
        #print("Starting pos: ["+str(xIndex)+", "+str(yIndex)+"]")


        #East
        for i in range(1, self.animal_range + 1):


            targetXIndex = xIndex + i
            targetYIndex = yIndex

            #Down
            for j in range(0,i):
                targetYIndex = yIndex + j
                if 0 <= targetXIndex < self.grid_size and 0 <= targetYIndex < self.grid_size:
                    #print("Cheking pos: ["+str(targetXIndex)+", "+str(targetYIndex)+"]")
                    if self.grid.grid[targetXIndex][targetYIndex].occupant != 0:


                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isPlant and not self.grid.grid[targetXIndex][targetYIndex].occupant.wood:
                            #print("We have detected a plant!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestPlantDistance > dist:
                                #print("++++++++++++NEW CLOSEST PLANT AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestPlantDirection = (False, False, True, False)
                                closestPlantDistance = dist

                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isAnimal:
                            #print("We have detected an animal!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestAnimalDistance > dist:
                                #print("++++++++++++NEW CLOSEST ANIMAL AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestAnimalDirection = (False, False, True, False)
                                closestAnimalDistance = dist


            #Up, starts from 1 instad of 0 so it doesn't check the middle cell again
            for j in range(1,i):
                targetYIndex = yIndex - j
                if 0 <= targetXIndex < self.grid_size and 0 <= targetYIndex < self.grid_size:
                    #print("Cheking pos: ["+str(targetXIndex)+", "+str(targetYIndex)+"]")
                    if self.grid.grid[targetXIndex][targetYIndex].occupant != 0:


                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isPlant and not self.grid.grid[targetXIndex][targetYIndex].occupant.wood:
                            #print("We have detected a plant!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestPlantDistance > dist:
                                #print("++++++++++++NEW CLOSEST PLANT AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestPlantDirection = (False, False, True, False)
                                closestPlantDistance = dist

                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isAnimal:
                            #print("We have detected a animal!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestAnimalDistance > dist:
                                #print("++++++++++++NEW CLOSEST ANIMAL AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestAnimalDirection = (False, False, True, False)
                                closestAnimalDistance = dist


        #print("*******************Animal East Radar Update FINISHED*******************\n")

        #print("*******************Animal West Radar Update STARTED*******************")
        #print("Starting pos: ["+str(xIndex)+", "+str(yIndex)+"]")


        #West
        for i in range(1, self.animal_range + 1):


            targetXIndex = xIndex - i
            targetYIndex = yIndex

            #Down
            for j in range(0,i):
                targetYIndex = yIndex + j
                if 0 <= targetXIndex < self.grid_size and 0 <= targetYIndex < self.grid_size:
                    #print("Cheking pos: ["+str(targetXIndex)+", "+str(targetYIndex)+"]")
                    if self.grid.grid[targetXIndex][targetYIndex].occupant != 0:


                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isPlant and not self.grid.grid[targetXIndex][targetYIndex].occupant.wood:
                            #print("We have detected a plant!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestPlantDistance > dist:
                                #print("++++++++++++NEW CLOSEST PLANT AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestPlantDirection = (False, False, False, True)
                                closestPlantDistance = dist

                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isAnimal:
                            #print("We have detected a animal!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestAnimalDistance > dist:
                                #print("++++++++++++NEW CLOSEST ANIMAL AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestAnimalDirection = (False, False, False, True)
                                closestAnimalDistance = dist

            #Up, starts from 1 instad of 0 so it doesn't check the middle cell again
            for j in range(1,i):
                targetYIndex = yIndex - j
                if 0 <= targetXIndex < self.grid_size and 0 <= targetYIndex < self.grid_size:
                    #print("Cheking pos: ["+str(targetXIndex)+", "+str(targetYIndex)+"]")
                    if self.grid.grid[targetXIndex][targetYIndex].occupant != 0:


                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isPlant and not self.grid.grid[targetXIndex][targetYIndex].occupant.wood:
                            #print("We have detected a plant!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestPlantDistance > dist:
                                #print("++++++++++++NEW CLOSEST PLANT AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestPlantDirection = (False, False, False, True)
                                closestPlantDistance = dist

                        if self.grid.grid[targetXIndex][targetYIndex].occupant.isAnimal:
                            #print("We have detected a animal!!!")
                            dist = abs(xIndex - targetXIndex) + abs(yIndex - targetYIndex)
                            if closestAnimalDistance > dist:
                                #print("++++++++++++NEW CLOSEST ANIMAL AT: ["+str(targetXIndex)+", "+str(targetYIndex)+"]+++++++++++++")
                                closestAnimalDirection = (False, False, False, True)
                                closestAnimalDistance = dist



        #print("*******************Animal West Radar Update FINISHED*******************\n")

        if closestPlantDirection[0]:
            agent.plantNorth = True
            agent.plantSouth = False
            agent.plantEast = False
            agent.plantWest = False
            #print("------------------RESULTS: North")
        elif closestPlantDirection[1]:
            agent.plantNorth = False
            agent.plantSouth = True
            agent.plantEast = False
            agent.plantWest = False
            #print("------------------RESULTS: South")
        elif closestPlantDirection[2]:
            agent.plantNorth = False
            agent.plantSouth = False
            agent.plantEast = True
            agent.plantWest = False
            #print("------------------RESULTS: East")
        elif closestPlantDirection[3]:
            agent.plantNorth = False
            agent.plantSouth = False
            agent.plantEast = False
            agent.plantWest = True
            #print("------------------RESULTS: West")
        else:
            agent.plantNorth = False
            agent.plantSouth = False
            agent.plantEast = False
            agent.plantWest = False
            #print("------------------RESULTS: NO NEARBY PLANTS")



        if closestAnimalDirection[0]:
            agent.animalNorth = True
            agent.animalSouth = False
            agent.animalEast = False
            agent.animalWest = False
            #print("------------------RESULTS: North")
        elif closestAnimalDirection[1]:
            agent.animalNorth = False
            agent.animalSouth = True
            agent.animalEast = False
            agent.animalWest = False
            #print("------------------RESULTS: South")
        elif closestAnimalDirection[2]:
            agent.animalNorth = False
            agent.animalSouth = False
            agent.animalEast = True
            agent.animalWest = False
            #print("------------------RESULTS: East")
        elif closestAnimalDirection[3]:
            agent.animalNorth = False
            agent.animalSouth = False
            agent.animalEast = False
            agent.animalWest = True
            #print("------------------RESULTS: West")
        else:
            agent.animalNorth = False
            agent.animalSouth = False
            agent.animalEast = False
            agent.animalWest = False
            #print("------------------RESULTS: NO NEARBY Animals")



    def move_agents(self):
        for agent in self.grid.animals:
            self.agent_mover(agent)

    def animal_attacker(self):
        for agent in self.grid.animals:

            neighbours = self.grid.neighbour_agent(agent)

            if neighbours != []:
                agent.attack_agent(neighbours[randint(0,len(neighbours)-1)])
            for neighbour in neighbours:
                agent.attack_agent(neighbour)


    #Everu 20 iterations, it coumputes a list of random indexes that correspond to the plants that will grow
    def plant_grower(self):
        if self.growingCounter > 20:

            self.growingCounter = 0
            randomIndexList = []

            #The lenght of the randomIndexList will deternime the amount of plants that will grow every time this function is executed
            for i in range(0, int(len(self.grid.plants) / 5) + 1):
                randomIndexList.append(randint(0, len(self.grid.plants)-1))
            for j in randomIndexList:
                self.grid.plants[j].grow()

        else:
            self.growingCounter += 1


    def wood_manager(self):
        if self.currentWoods < self.maxWoods:

            if randint(0,100) == 0:
                randIndex = randint(0,len(self.grid.plants) - 1)
                if not self.grid.plants[randIndex].wood:
                    self.grid.plants[randIndex].wood = True
                    self.grid.plants[randIndex].color = (102, 81, 0)
                    self.currentWoods += 1


    def agent_killer(self):
        for agent in self.grid.agents:
            if agent.biomaterial <= 0:
                self.agent_remove(agent)


    def plant_reproducer(self):

        for agent in self.grid.plants:

            if agent.biomaterial >= 20:

                free_cells = self.grid.free_cell(agent)

                if free_cells != []:
                    randomFreeCellIndex = 0
                    agent.biomaterial -= 10
                    self.add_agent_plant(Plant(free_cells[randomFreeCellIndex], self.camera), free_cells[randomFreeCellIndex].xIndex, free_cells[randomFreeCellIndex].yIndex)

    def animal_reproducer(self):

        for agent in self.grid.animals:

            if agent.biomaterial >= 200:

                free_cells = self.grid.free_cell(agent)

                if free_cells != []:
                    randomFreeCellIndex = 0
                    agent.biomaterial -= 100
                    newColor = self.generateNewColor(agent.color)
                    self.add_agent_animal(Animal(free_cells[randomFreeCellIndex], newColor, self.camera, agent.generation + 1, agent.genome.mutate_genome()), free_cells[randomFreeCellIndex].xIndex, free_cells[randomFreeCellIndex].yIndex)

                    if agent.generation + 1 > self.generations:

                        print("Generation [Latest]: "+str(agent.generation + 1))
                        self.generations = agent.generation + 1
                    else:
                        print("Generation: "+str(agent.generation + 1))

                    self.print_stats = True



    def generateNewColor(self, baseColor):
        red = baseColor[0]
        green = baseColor[1]
        blue = baseColor[2]

        redVariation = randint(-10,10)
        greenVariation = randint(-10,10)
        blueVariation = randint(-10,10)

        finalRed = red - redVariation
        finalGreen = green - greenVariation
        finalBlue = blue - blueVariation

        if red - redVariation < 0:
            finalRed = 0
        if green - greenVariation < 0:
            finalGreen = 0
        if blue - blueVariation < 0:
            finalBlue = 0

        if red - redVariation > 255:
            finalRed = 255
        if green - greenVariation > 255:
            finalGreen = 255
        if blue - blueVariation > 255:
            finalBlue = 255


        return (finalRed, finalGreen, finalBlue)



    def pause_button(self):

        if not self.pause:
            print("Game has been paused")
        else:
            print("Game has been resumed")

        self.pause = not self.pause

    #Function that simplifies the ratio of Plants:Animals
    def simplify_ratio(self, ratio):
        denominater = functools.reduce(gcd,ratio)
        solved = [i/denominater for i in ratio]
        return ':'.join(str(int(i)) for i in solved)

    def approximate_ratio(self, ratio):
        solved = int(ratio[1]/ratio[0])
        return '1:'+str(solved)
