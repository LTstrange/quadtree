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

    def insert(self, particle):
        if not self.boundary.collidepoint(particle.x, particle.y):
            return False
        if len(self.points) < self.capacity:
            self.points.append(particle)
        else:
            if not self.divided:
                self.subdivide()

            self.northeast.insert(particle)
            self.northwest.insert(particle)
            self.southeast.insert(particle)
            self.southwest.insert(particle)

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






