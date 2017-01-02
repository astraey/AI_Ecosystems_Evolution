from random import randint
from classes.plant import Plant
from classes.predator import Predator
from classes.camera import Camera


class Manager:

    def __init__(self, predatorlist, plantlist, screen, height, width):
        self.predatorlist = predatorlist
        self.plantlist = plantlist
        self.screen = screen
        self.height = height
        self.width = width

        self.camera = Camera(0, 0)

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

        for i in range(0, len(self.plantlist)):
            self.plantlist[i].grow()
            if self.plantlist[i].readyToGrow and 0 < self.plantlist[i].xpos < self.width and self.plantlist[i].ypos < self.height and self.plantlist[i].ypos > 0:

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

                        self.plantlist.append(Plant(self.plantlist[i].xpos - 10, self.plantlist[i].ypos + 10, self.camera))

                # Plant Grows north-west
                if temp == 1:

                    flag = True
                    for element in self.plantlist:
                        if abs(element.xpos - self.plantlist[i].xpos - 10) < 10 and abs(element.ypos - self.plantlist[i].ypos - 10) < 10:
                            flag = False

                    if flag:

                        self.plantlist.append(Plant(self.plantlist[i].xpos - 10, self.plantlist[i].ypos - 10, self.camera))

                # Plant Grows south-east
                if temp == 2:
                    flag = True
                    for element in self.plantlist:
                        if abs(element.xpos - self.plantlist[i].xpos + 10) < 10 and abs(element.ypos - self.plantlist[i].ypos + 10) < 10:
                            flag = False

                    if flag:

                        self.plantlist.append(Plant(self.plantlist[i].xpos + 10, self.plantlist[i].ypos + 10, self.camera))

                # Plant Grows north-east
                if temp == 3:
                    flag = True
                    for element in self.plantlist:
                        if abs(element.xpos - self.plantlist[i].xpos + 10) < 10 and abs(element.ypos - self.plantlist[i].ypos - 10) < 10:
                            flag = False

                    if flag:

                        self.plantlist.append(Plant(self.plantlist[i].xpos + 10, self.plantlist[i].ypos - 10, self.camera))

                self.plantlist[i].readyToGrow = False

    def eating_manager(self):

        for i in range(0, len(self.predatorlist)):
            for element in self.plantlist:
                if abs(self.predatorlist[i].xpos - element.xpos) < 10 and abs(self.predatorlist[i].ypos - element.ypos) < 10:
                    self.predatorlist[i].biomaterial += 10
                    # print("New element's biomaterial: " + str(self.predatorlist[i].biomaterial))
                    self.plantlist.remove(element)

    def render_predators_plants(self):

        # (0, 0, 0) is the RGB codification for Black
        self.screen.fill((0, 0, 0))

        for i in range(0, len(self.predatorlist)):
            self.predatorlist[i].draw(self.screen)

        for i in range(0, len(self.plantlist)):
            self.plantlist[i].draw(self.screen)

    def generator(self):

        self.predatorgenerator()

        self.plantgenerator()

    def addplant(self, x, y, camera):
        self.plantlist.append(Plant(x, y, camera))

    def addpredator(self, x, y, color, camera):
        self.predatorlist.append(Predator(x, y, color, camera))

    def predatorgenerator(self):

        self.addpredator(400, 400, (255, 0, 0), self.camera)
        self.addpredator(250, 250, (0, 0, 255), self.camera)

    def plantgenerator(self):

        self.addplant(350, 350, self.camera)
        self.addplant(350, 400, self.camera)
        self.addplant(400, 350, self.camera)
        self.addplant(350, 450, self.camera)
        self.addplant(450, 350, self.camera)
        self.addplant(350, 450, self.camera)
        self.addplant(550, 550, self.camera)
        self.addplant(300, 450, self.camera)
        self.addplant(200, 200, self.camera)
        self.addplant(500, 200, self.camera)

    def cell_up(self, index):
        self.predatorlist[index].ypos -= 15

    def cell_down(self, index):
        self.predatorlist[index].ypos += 15

    def cell_left(self, index):
        self.predatorlist[index].xpos -= 15

    def cell_right(self, index):
        self.predatorlist[index].xpos += 15




