# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 23:30
# @Author  : LTstrange

import random

import pygame
from pygame.color import THECOLORS
from pygame.rect import Rect
from pygame.sprite import Group
from entity import Particle
from quadtree import Quadtree

width = 700
height = 700

map_width = 1024
map_height = 1024


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    map = pygame.Surface((map_width, map_height))
    pygame.display.set_caption("quadtree")

    clock = pygame.time.Clock()

    particles = Group([Particle(random.gauss(map_width/2, 100) % map_width,
                                random.gauss(map_height/2, 100) % map_height, 4, map)
                       for _ in range(1000)])

    qtree = Quadtree(map.get_rect(), 4, map)
    for p in particles:
        qtree.insert(p)

    # for p in particles:
    #     if not p.highlight:
    #         print(p)

    query_rect = Rect(0, 0, 200, 200)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                query_rect.centerx = event.pos[0] * (map_width / width)
                query_rect.centery = event.pos[1] * (map_height / height)

        qtree.query(query_rect)

        map.fill(THECOLORS['black'])

        particles.update()

        qtree.show()
        particles.draw(map)

        pygame.draw.rect(map, THECOLORS['green'], query_rect, 2)

        pygame.transform.scale(map, (width, height), screen)

        pygame.display.update()
        for p in particles:
            p.highlight = False


if __name__ == '__main__':
    main()
