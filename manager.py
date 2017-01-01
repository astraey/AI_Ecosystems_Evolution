from random import randint
from classes.plant import Plant
from classes.predator import Predator
import functions


class Manager:

    def __init__(self, predatorlist, plantlist, screen, height, width):
        self.predatorlist = predatorlist
        self.plantlist = plantlist
        self.screen = screen
        self.height = height
        self.width = width

    def generator(self):

        functions.predatorgenerator(self.predatorlist)

        functions.plantgenerator(self.plantlist)

    def predator_move_reproduce(self):
        for element in self.predatorlist:
            element.move()
            if element.biomaterial > 200:
                element.biomaterial -= 100
                self.predatorlist.append(Predator(element.xpos, element.ypos))

    def plant_reproduce(self):

        for i in range(0, len(self.plantlist)):
            self.plantlist[i].grow()
            if self.plantlist[i].readyToGrow and self.plantlist[i].xpos > 0 and self.plantlist[i].xpos < self.width and self.plantlist[i].ypos < self.height and self.plantlist[i].ypos > 0:

                print("No Plantas: " + str(len(self.plantlist)))
                # print("Creator Plant: " + str(self.plantsList[i].xpos) + " , " + str(self.plantsList[i].ypos))

                temp = randint(0, 3)

                # Plant Grows south-west
                if temp == 0:
                    flag = True
                    for element in self.plantlist:
                        if abs(element.xpos - self.plantlist[i].xpos) < 15 and abs(element.ypos - self.plantlist[i].ypos) < 15:
                            flag = False

                    if flag:

                        self.plantlist.append(Plant(self.plantlist[i].xpos - 10, self.plantlist[i].ypos + 10))

                # Plant Grows north-west
                if temp == 1:

                    flag = True
                    for element in self.plantlist:
                        if abs(element.xpos - self.plantlist[i].xpos - 10) < 10 and abs(element.ypos - self.plantlist[i].ypos - 10) < 10:
                            flag = False

                    if flag:

                        self.plantlist.append(Plant(self.plantlist[i].xpos - 10, self.plantlist[i].ypos - 10))

                # Plant Grows south-east
                if temp == 2:
                    flag = True
                    for element in self.plantlist:
                        if abs(element.xpos - self.plantlist[i].xpos + 10) < 10 and abs(element.ypos - self.plantlist[i].ypos + 10) < 10:
                            flag = False

                    if flag:

                        self.plantlist.append(Plant(self.plantlist[i].xpos + 10, self.plantlist[i].ypos + 10))

                # Plant Grows north-east
                if temp == 3:
                    flag = True
                    for element in self.plantlist:
                        if abs(element.xpos - self.plantlist[i].xpos + 10) < 10 and abs(element.ypos - self.plantlist[i].ypos - 10) < 10:
                            flag = False

                    if flag:

                        self.plantlist.append(Plant(self.plantlist[i].xpos + 10, self.plantlist[i].ypos - 10))

                self.plantlist[i].readyToGrow = False

    def eating_manager(self):

        for i in range(0, len(self.predatorlist)):
            for element in self.plantlist:
                if abs(self.predatorlist[i].xpos - element.xpos) < 10 and abs(self.predatorlist[i].ypos - element.ypos) < 10:
                    self.predatorlist[i].biomaterial +=10
                    print("New element's biomaterial: " + str(self.predatorlist[i].biomaterial))
                    self.plantlist.remove(element)

    def render_predators_plants(self):

        # (0, 0, 0) is the RGB codification of Black
        self.screen.fill((0, 0, 0))

        for i in range(0, len(self.predatorlist)):
            self.predatorlist[i].draw(self.screen)

        for i in range(0, len(self.plantlist)):
            self.plantlist[i].draw(self.screen)

