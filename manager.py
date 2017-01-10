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
        self.addplant(550, 550, self.camera)
        self.addplant(300, 450, self.camera)
        self.addplant(200, 200, self.camera)
        self.addplant(500, 200, self.camera)
        # self.addplant(1500, 1500, self.camera)

    def cell_up(self, index):
        self.predatorlist[index].ypos -= 15

    def cell_down(self, index):
        self.predatorlist[index].ypos += 15

    def cell_left(self, index):
        self.predatorlist[index].xpos -= 15

    def cell_right(self, index):
        self.predatorlist[index].xpos += 15

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

