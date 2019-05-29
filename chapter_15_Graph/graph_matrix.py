#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys


class Graph:
    """
    邻接矩阵实现
    """

    class _Vertex:
        def __init__(self, value):
            self.value = value

    class _Edges:
        def __init__(self, weight, info):
            self.weight = weight
            self.info = info

        def __str__(self):
            return "Weight: {}, Info: {}".format(str(self.weight), str(self.info))

    def __init__(self, vertex):
        self._vertex = vertex
        length = len(vertex)
        self._edges = [[self._Edges(sys.maxsize, None)
                        for j in range(length)] for i in range(length)]

    def union(self, i, j, w, info):
        self._edges[i][j].weight = self._edges[j][i].weight = w
        self._edges[i][j].info = self._edges[j][i].info = info

    def print(self):
        for temp in self._edges:
            for ret in temp:
                print(ret)


if __name__ == '__main__':
    graph = Graph([2, 3, 1, 7, 6, 9, 0, 10])

    graph.union(1, 2, 10, "test")
    graph.union(1, 6, 100, "word")
    graph.union(3, 4, 20, "success")
    graph.print()
