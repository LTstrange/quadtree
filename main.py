# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 23:30
# @Author  : LTstrange

import random

import pygame
from pygame.color import THECOLORS
from pygame.sprite import Group
from entity import Particle


width = 600
height = 600


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("quadtree")

    clock = pygame.time.Clock()

    particles = Group([Particle(random.randint(0, width), random.randint(0, height), 8, screen)
                       for _ in range(100)])

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill(THECOLORS['black'])

        particles.update()

        particles.draw(screen)

        pygame.display.update()


if __name__ == '__main__':
    main()
