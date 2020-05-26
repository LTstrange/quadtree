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
    font = pygame.font.SysFont('arial', 20)

    clock = pygame.time.Clock()

    particles = Group([Particle(random.gauss(map_width/2, 150) % map_width,
                                random.gauss(map_height/2, 150) % map_height, 4, map)
                       for _ in range(1000)])

    qtree = Quadtree(map.get_rect(), 4, map)
    for p in particles:
        qtree.insert(p)

    while True:
        clock.tick(60)
        fps_text = font.render(f'fps:{int(clock.get_fps())}', True, THECOLORS['white'])
        fps_rect = fps_text.get_rect()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        qtree = Quadtree(map.get_rect(), 4, map)
        for p in particles:
            qtree.insert(p)

        particles.update()

        for p in particles:
            p.highlight = False
            query_rect = Rect(p.rect.x, p.rect.y, p.radius * 2, p.radius * 2)
            if len(qtree.query(query_rect)) != 1:
                p.highlight = True


        map.fill(THECOLORS['black'])
        particles.draw(map)

        pygame.transform.scale(map, (width, height), screen)

        screen.blit(fps_text, fps_rect)

        pygame.display.update()


if __name__ == '__main__':
    main()
