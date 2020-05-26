# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 23:30
# @Author  : LTstrange

import random

import pygame
from pygame.color import THECOLORS
from pygame.sprite import Group
from entity import Particle
from quadtree import Quadtree

width = 600
height = 600


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("quadtree")

    clock = pygame.time.Clock()

    particles = Group([Particle(random.gauss(width/2, 100), random.gauss(height/2, 100), 2, screen)
                       for _ in range(1000)])

    qtree = Quadtree(screen.get_rect(), 4, screen)
    for p in particles:
        qtree.insert(p)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill(THECOLORS['black'])

        particles.update()

        particles.draw(screen)

        qtree.show()


        pygame.display.update()


if __name__ == '__main__':
    main()
