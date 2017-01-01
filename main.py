import pygame
import functions
from random import randint
from classes import Predator
from classes import Plant
from manager import Manager

NEGRO = (0, 0, 0)

icon = pygame.image.load('icon.png')


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 800

        # self.predatorlist = []

        # self.plantslist = []

        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.manager = Manager([], [], self._display_surf, self.height, self.width)

        # functions.predatorgenerator(self.predatorlist)

        # functions.plantgenerator(self.plantslist)

        self.manager.generator()

        self.masterClock = pygame.time.Clock()

    def on_init(self):

        pygame.init()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Ecosystem Simulator")

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):

        """

        for i in range(0, len(self.predatorlist)):
            self.predatorlist[i].move()
            if self.predatorlist[i].biomaterial > 200:
                self.predatorlist[i].biomaterial -= 100
                self.predatorlist.append(Predator(self.predatorlist[i].xpos, self.predatorlist[i].ypos))

        """

        # Equivalente en Manager

        self.manager.predator_move_reproduce()

        """

        for i in range(0, len(self.plantslist)):
            self.plantslist[i].grow()
            if self.plantslist[i].readyToGrow and self.plantslist[i].xpos > 0 and self.plantslist[i].xpos < self.width and self.plantslist[i].ypos < self.height and self.plantslist[i].ypos > 0:

                print("No Plantas: " + str(len(self.plantslist)))
                # print("Creator Plant: " + str(self.plantsList[i].xpos) + " , " + str(self.plantsList[i].ypos))

                temp = randint(0, 3)


                # Plant Grows south-west
                if temp == 0:
                    flag = True
                    for element in self.plantslist:
                        if abs(element.xpos - self.plantslist[i].xpos - 10) < 15 and abs(element.ypos - self.plantslist[i].ypos + 10) < 15:
                            flag = False

                    if flag:

                        self.plantslist.append(Plant(self.plantslist[i].xpos - 10, self.plantslist[i].ypos + 10))

                # Plant Grows north-west
                if temp == 1:

                    flag = True
                    for element in self.plantslist:
                        if abs(element.xpos - self.plantslist[i].xpos - 10) < 10 and abs(element.ypos - self.plantslist[i].ypos - 10) < 10:
                            flag = False

                    if flag:

                        self.plantslist.append(Plant(self.plantslist[i].xpos - 10, self.plantslist[i].ypos - 10))

                # Plant Grows south-east
                if temp == 2:
                    flag = True
                    for element in self.plantslist:
                        if abs(element.xpos - self.plantslist[i].xpos + 10) < 10 and abs(element.ypos - self.plantslist[i].ypos + 10) < 10:
                            flag = False

                    if flag:

                        self.plantslist.append(Plant(self.plantslist[i].xpos + 10, self.plantslist[i].ypos + 10))

                # Plant Grows north-east
                if temp == 3:
                    flag = True
                    for element in self.plantslist:
                        if abs(element.xpos - self.plantslist[i].xpos + 10) < 10 and abs(element.ypos - self.plantslist[i].ypos - 10) < 10:
                            flag = False

                    if flag:

                        self.plantslist.append(Plant(self.plantslist[i].xpos + 10, self.plantslist[i].ypos - 10))

                self.plantslist[i].readyToGrow = False

        """

        # Manager Equivalent

        self.manager.plant_reproduce()

        """

        for i in range(0, len(self.predatorlist)):
            for element in self.plantslist:
                if abs(self.predatorlist[i].xpos - element.xpos) < 10 and abs(self.predatorlist[i].ypos - element.ypos) < 10:
                    self.predatorlist[i].biomaterial +=10
                    print("New element's biomaterial: " + str(self.predatorlist[i].biomaterial))
                    self.plantslist.remove(element)

        """

        # Manager Equivalent

        self.manager.eating_manager()

    def on_render(self):

        """
        self._display_surf.fill(NEGRO)

        for i in range(0, len(self.predatorlist)):
            self.predatorlist[i].draw(self._display_surf)

        for i in range(0, len(self.plantslist)):
            self.plantslist[i].draw(self._display_surf)

        """

        # Manager Equivalent

        self.manager.render_predators_plants()

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):

            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

            # Limits the number of times that the loop is executed in a second
            self.masterClock.tick(15)

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
