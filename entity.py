# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 23:41
# @Author  : LTstrange
import random
import pygame
from pygame.color import THECOLORS
from pygame.sprite import Sprite
from pygame import Surface


class Particle(Sprite):
    def __init__(self, x, y, r):
        super(Particle, self).__init__()
        self.x = x
        self.y = y
        self.r = r
        self.image = Surface((2*r, 2*r))
        self.rect = self.image.get_rect()

    def update(self, *args):
        # self.x += random.gauss(0, 1)
        # self.y += random.gauss(0, 1)

        self.rect.x = self.x
        self.rect.y = self.y

        pygame.draw.ellipse(self.image, THECOLORS['white'], (0, 0, self.r*2, self.r*2))
