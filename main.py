# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 23:30
# @Author  : LTstrange

import pygame
from pygame.color import THECOLORS




def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("quadtree")

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill(THECOLORS['black'])

        pygame.display.update()


if __name__ == '__main__':
    main()
