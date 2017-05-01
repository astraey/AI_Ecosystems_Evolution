import pygame
from manager import Manager


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None

        self.size = self.width, self.height = 800, 800

        display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.manager = Manager(display, self.height, self.width)

        self.manager.icon_setter()

        self.masterClock = pygame.time.Clock()

    def on_init(self):

        pygame.init()

        self._running = True

        # self.manager.test_add_predators()

        self.manager.random_add_predators(250)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        self.manager.event_management(event)

    def on_loop(self):

        if not self.manager.pause:

            self.manager.camera_move()

            self.manager.move_agents()

            self.manager.agent_attacker()

            self.manager.agent_killer()

            self.manager.agent_reproducer()

            #Prints the number of agents alive in the simulation
            #print(str(len(self.manager.grid.agents)))

    def on_render(self):

        self.manager.paint_screen_black()

        self.manager.draw_grid()

        self.manager.draw_agents()

        #old
        #self.manager.render_predators_plants()

        pygame.display.flip()

    def on_execute(self):

        if self.on_init() is False:
            self._running = False

        while self._running:

            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

            # Limits the number of times that the loop is executed in a second
            self.masterClock.tick(15)

        pygame.quit()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
