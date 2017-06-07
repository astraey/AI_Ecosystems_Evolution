import pygame

from random import randint

class Animal:

    def __init__(self, cell, color, camera, generation, genome):

        self.xPos = cell.xPos
        self.yPos = cell.yPos
        self.size = 2
        self.counter = 0
        self.movementCounter = 0
        self.color = color
        self.cell = cell
        self.isPlant = False
        self.isAnimal = True
        self.wood = False
        self.compass = randint(0,3)
        self.biomaterial = 100
        self.camera = camera
        self.radarRange = 20

        self.generation = generation
        self.genome = genome

        self.animalNorth = False
        self.animalSouth = False
        self.animalEast = False
        self.animalWest = False

        self.plantNorth = False
        self.plantSouth = False
        self.plantEast = False
        self.plantWest = False


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.xPos + self.camera.xpos), int(self.yPos + self.camera.ypos)), self.size)


    def move(self):
        return self.genome.get_move()


    def attack_agent(self, defender_agent):

        if not defender_agent.wood:

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

    #Update environment information
    def update_genome_environment_information(self):

        self.genome.plantsDir = (self.plantNorth, self.plantSouth, self.plantEast, self.plantWest)
        self.genome.predatorsDir = (self.animalNorth, self.animalSouth, self.animalEast, self.animalWest)

        if not True in self.genome.plantsDir and not True in self.genome.predatorsDir:
            self.genome.nothingDetected = True
            #print("Nothing Detected")

        else:
            self.genome.nothingDetected = False
            #print(".")
