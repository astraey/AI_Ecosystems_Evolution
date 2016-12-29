import pygame
from random import randint
from classes import NewObject
from classes import Plant

NEGRO = (0, 0, 0)
icon = pygame.image.load('icon.png')


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 800

        self.entitiesList = []

        self.plantsList = []

        # for i in range(0, 4):
        self.entitiesList.append(NewObject(400, 400))

        for i in range(0, 1):
            self.plantsList.append(Plant(50*i + 100, 50*i + 100))

        self.counter = 0
        self.masterClock = pygame.time.Clock()
        #print (len(self.entitiesList))

    def on_init(self):
        pygame.init()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Ecosystem Simulator")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):

        for i in range(0, len(self.entitiesList)):
            self.entitiesList[i].move()
            if self.entitiesList[i].biomaterial > 200:
                self.entitiesList[i].biomaterial -= 100
                self.entitiesList.append(NewObject(self.entitiesList[i].xpos, self.entitiesList[i].ypos))

        for i in range(0, len(self.plantsList)):
            self.plantsList[i].grow()
            if self.plantsList[i].readyToGrow:

                temp = randint(0, 3)

                # Plant Grows south-west
                if temp == 0:
                    self.plantsList.append(Plant(self.plantsList[i].xpos - 10, self.plantsList[i].ypos + 10))

                # Plant Grows north-west
                if temp == 1:
                    self.plantsList.append(Plant(self.plantsList[i].xpos - 10, self.plantsList[i].ypos - 10))

                # Plant Grows south-east
                if temp == 2:
                    self.plantsList.append(Plant(self.plantsList[i].xpos + 10, self.plantsList[i].ypos + 10))

                # Plant Grows north-east
                if temp == 3:
                    self.plantsList.append(Plant(self.plantsList[i].xpos + 10, self.plantsList[i].ypos - 10))

                self.plantsList[i].readyToGrow = False

    def on_render(self):
        self._display_surf.fill(NEGRO)

        for i in range(0, len(self.entitiesList)):
            self.entitiesList[i].draw(self._display_surf)

        for i in range(0, len(self.plantsList)):
            self.plantsList[i].draw(self._display_surf)

        pygame.display.flip()
        # print(self.counter)
        self.counter += 1

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
            self.masterClock.tick(5)

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
