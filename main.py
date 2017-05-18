import pygame, time
from manager import Manager




class App:
    def __init__(self):

        self.start_time = time.time()

        self._running = True
        self._display_surf = None

        #Times that the loop is executed every second
        self.masterLoopController = 30

        self.size = self.width, self.height = 1010, 1010

        display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.manager = Manager(display, self.height, self.width)

        self.manager.icon_setter()

        self.masterClock = pygame.time.Clock()

    def on_init(self):

        pygame.init()

        self._running = True


        self.manager.random_add_predators(6)

        self.manager.random_add_plants(400)

    def on_event(self, event):

        if event.type == pygame.QUIT:
            self._running = False

        self.manager.event_management(event)

    def on_loop(self):

        self.manager.camera_move()

        if not self.manager.pause:

            self.manager.update_predators_radar()

            self.manager.move_agents()

            self.manager.predator_attacker()

            self.manager.plant_grower()

            self.manager.agent_killer()



            self.manager.plant_reproducer()

            self.manager.predator_reproducer()

            self.manager.wood_manager()

            #Only printed when a predator has been updated
            if self.manager.print_stats:
                self.stats_printer()
                self.manager.print_stats = False


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
            self.masterClock.tick(self.masterLoopController)

        pygame.quit()

    def stats_printer(self):

        ratio = [len(self.manager.grid.predators), len(self.manager.grid.plants)]


        #Prints the number of agents alive in the simulation

        print("Agents: %d, Predators: %d, Plants: %d" %(len(self.manager.grid.agents), len(self.manager.grid.predators), len(self.manager.grid.plants)))


        #print("Exact Predators:Plants Ratio ["+self.manager.simplify_ratio(ratio)+"]")
        print("Predators:Plants Ratio ["+self.manager.approximate_ratio(ratio)+"]")

        m, s = divmod((time.time() - self.start_time), 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        print("[%d days - %02d hours - %02d min - %02d sec]" % (d, h, m, s))

        #print("Generations: "+str(self.manager.generations)+"\n")


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
