import pygame, time
from manager import Manager



class App:
    def __init__(self):

        self.start_time = time.time()

        self._running = True
        self._display_surf = None

        self.size = self.width, self.height = 1010, 1010

        display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.manager = Manager(display, self.height, self.width)

        self.manager.icon_setter()

        self.masterClock = pygame.time.Clock()

    def on_init(self):

        pygame.init()

        self._running = True


        self.manager.random_add_predators(2)

        self.manager.random_add_plants(40)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        self.manager.event_management(event)

    def on_loop(self):

        self.manager.camera_move()

        if not self.manager.pause:

            self.manager.move_agents()

            self.manager.predator_attacker()

            #self.manager.plant_grower()
            self.manager.plant_optimized_grower()

            self.manager.agent_killer()

            self.manager.agent_reproducer()

            self.manager.wood_manager()

            self.manager.update_predators_radar()

            self.stats_printer()



    def on_render(self):

        self.manager.paint_screen_black()

        #Draws the whole grid
        #self.manager.draw_grid()

        #Draws just the exterior frame of the grid
        self.manager.draw_grid_frame()

        self.manager.draw_agents()


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

    def stats_printer(self):

        #Prints the number of agents alive in the simulation

        print("Agents: %d, Predators: %d, Plants: %d" %(len(self.manager.grid.agents), len(self.manager.grid.predators), len(self.manager.grid.plants)))


        m, s = divmod((time.time() - self.start_time), 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        print("[%d days - %02d hours - %02d min - %02d sec]\n" % (d, h, m, s))


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
