# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 23:41
# @Author  : LTstrange
import random
import pygame
from pygame.color import THECOLORS
from pygame.sprite import Sprite
from pygame import Surface


class Particle(Sprite):
    def __init__(self, x, y, radius, screen):
        super(Particle, self).__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.image = Surface((2 * radius, 2 * radius)).convert_alpha(screen)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.highlight = False

        # debug
        self.tile = None

    def update(self, *args):
        self.x += int(random.gauss(0, 1))
        self.y += int(random.gauss(0, 1))

        self.rect.centerx = self.x
        self.rect.centery = self.y

        self.rect.centerx %= self.screen_rect.width
        self.rect.centery %= self.screen_rect.height

        if self.highlight:
            pygame.draw.ellipse(self.image, THECOLORS['green'], (0, 0, self.radius * 2, self.radius * 2))
        else:
            pygame.draw.ellipse(self.image, THECOLORS['red'], (0, 0, self.radius * 2, self.radius * 2))
