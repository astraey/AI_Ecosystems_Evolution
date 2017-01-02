import pygame

from random import randint


class Camera:

    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y

        self.moving_distance = 10

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def move_right(self):
        self.xpos += self.moving_distance

    def move_left(self):
        self.xpos -= self.moving_distance

    def move_up(self):
        self.ypos -= self.moving_distance

    def move_down(self):
        self.ypos += self.moving_distance
