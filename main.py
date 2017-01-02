import pygame
import os

from manager import Manager

NEGRO = (0, 0, 0)




class App:
    def __init__(self):
        self._running = True
        self._display_surf = None

        self.size = self.width, self.height = 800, 800

        display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.manager = Manager([], [], display, self.height, self.width)

        self.manager.generator()

        self.masterClock = pygame.time.Clock()

    def on_init(self):

        pygame.init()

        icon = pygame.image.load('media/icon.png')

        # Icon needs to be a Surface
        pygame.display.set_icon(icon)

        pygame.display.set_caption("Ecosystem Simulator")

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):

        self.manager.predator_move_reproduce()

        self.manager.plant_reproduce()

        self.manager.eating_manager()

    def on_render(self):

        self.manager.render_predators_plants()

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
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
