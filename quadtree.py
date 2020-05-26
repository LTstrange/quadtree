# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 23:45
# @Author  : LTstrange
import pygame
from pygame import Rect
from pygame.color import THECOLORS


class Quadtree:
    def __init__(self, boundary: Rect, n: int, screen):
        self.boundary = boundary
        self.capacity = n

        self.points = []
        self.divided = False

        self.screen = screen

    def insert(self, particle, depth=0):
        if not self.boundary.collidepoint(particle.x, particle.y):
            return False
        if len(self.points) < self.capacity:
            # particle.highlight = True
            self.points.append(particle)
        else:
            if not self.divided:
                self.subdivide()

            self.northeast.insert(particle, depth + 1)
            self.northwest.insert(particle, depth + 1)
            self.southeast.insert(particle, depth + 1)
            self.southwest.insert(particle, depth + 1)

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        centerx = self.boundary.centerx
        centery = self.boundary.centery
        width = self.boundary.width / 2
        height = self.boundary.height / 2

        ne = Rect(x, y, width, height)
        self.northeast = Quadtree(ne, self.capacity, self.screen)
        nw = Rect(centerx, y, width, height)
        self.northwest = Quadtree(nw, self.capacity, self.screen)
        se = Rect(x, centery, width, height)
        self.southeast = Quadtree(se, self.capacity, self.screen)
        sw = Rect(centerx, centery, width, height)
        self.southwest = Quadtree(sw, self.capacity, self.screen)

        self.divided = True

    def show(self):
        pygame.draw.rect(self.screen, THECOLORS['white'], self.boundary, 1)

        if self.divided:
            self.northeast.show()
            self.northwest.show()
            self.southeast.show()
            self.southwest.show()

    def query(self, rect: Rect):
        if self.boundary.colliderect(rect):
            for p in self.points:
                if rect.collidepoint(p.x, p.y):
                    p.highlight = True
                    pass
            if self.divided:
                self.northeast.query(rect)
                self.northwest.query(rect)
                self.southeast.query(rect)
                self.southwest.query(rect)
