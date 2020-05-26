# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 23:45
# @Author  : LTstrange


class Quadtree:
    def __init__(self, boundary, n):
        self.boundary = boundary
        self.capacity = n

        self.points = []
        self.divided = False

    def insert(self, point):
        if len(self.points) < self.capacity:
            self.points.append(point)
        else:
            self.subdivide()

    def subdivide(self):
        pass


