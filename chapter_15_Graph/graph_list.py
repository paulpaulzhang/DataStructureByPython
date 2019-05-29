#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys


class Graph:
    """
    邻接表实现
    """

    class _Vertex:
        def __init__(self, value, dummy_head):
            self.value = value
            self.dummy_head = dummy_head

        def __str__(self):
            return str(self.value) + "   "

    class _Node:
        def __init__(self, direction, weight, info):
            self.direction = direction
            self.weight = weight
            self.info = info
            self.next = None

        def __str__(self):
            return "Direction: {}, Weight: {}, Info: {}" \
                .format(str(self.direction),
                        str(self.weight), str(self.info))

    def __init__(self, vertex):
        self._size = len(vertex)
        self._vertex = [self._Vertex(None,
                                     self._Node(None, None, None))
                        for i in range(self._size)]
        for i in range(self._size):
            self._vertex[i].value = vertex[i]

    def union(self, i, j, weight, info=None):
        self._union_help(i, j, weight, info)
        self._union_help(j, i, weight, info)

    def _union_help(self, cur, direction, weight, info):
        node = self._Node(direction, weight, info)
        prev = self._vertex[cur].dummy_head
        while prev.next:
            prev = prev.next
        prev.next = node

    def dfs(self):
        """深度优先遍历"""
        visit = [False for i in range(self._size)]
        for i in range(self._size):
            if not visit[i]:
                self._dfs(visit, i)
                print()

    def _dfs(self, visit, v):
        visit[v] = True
        print(self._vertex[v], end="")
        prev = self._vertex[v].dummy_head
        while prev.next:
            w = prev.next.direction
            if not visit[w]:
                self._dfs(visit, w)
            prev = prev.next

    def bfs(self):
        """广度优先搜索"""
        visit = [False for i in range(self._size)]
        for i in range(self._size):
            if not visit[i]:
                self._bfs(visit, i)
                print()

    def _bfs(self, visit, v):
        queue = [v]
        while queue:
            w = queue.pop(0)
            visit[w] = True
            print(self._vertex[w], end="")
            prev = self._vertex[w].dummy_head
            while prev.next:
                w = prev.next.direction
                if not visit[w]:
                    queue.append(w)
                prev = prev.next

    class _Edges:
        def __init__(self, pre, weight, known):
            self.pre = pre
            self.weight = weight
            self.known = known

        def __str__(self):
            return str(self.pre) + "(weight:" + str(self.weight) + ")"

    def prim(self, v):
        """最小生成树Prim算法"""
        close = [self._Edges(None, sys.maxsize, False)
                 for i in range(self._size)]
        close[v].weight = 0
        for i in range(self._size):
            k = self._get_min(close)
            close[k].known = True
            prev = self._vertex[k].dummy_head
            while prev.next:
                w = prev.next.direction
                if not close[w].known \
                        and prev.next.weight < close[w].weight:
                    close[w].weight = prev.next.weight
                    close[w].pre = k
                prev = prev.next
        return close

    def dijkstra(self, v):
        close = [self._Edges(None, sys.maxsize, False)
                 for _ in range(self._size)]
        close[v].weight = 0

        for i in range(self._size):
            k = self._get_min(close)
            close[k].known = True
            prev = self._vertex[k].dummy_head
            while prev.next:
                w = prev.next.direction
                if not close[w].known and \
                        close[k].weight + prev.next.weight \
                        < close[w].weight:
                    close[w].weight = close[k].weight + prev.next.weight
                    close[w].pre = k
                prev = prev.next
        return close

    def _get_min(self, close):
        min = sys.maxsize
        temp = -1
        for i in range(self._size):
            if not close[i].known and min > close[i].weight:
                min = close[i].weight
                temp = i
        if temp == -1:
            raise ValueError("temp=" + str(temp))
        return temp

    def print(self):
        for temp in self._vertex:
            dummy_head = temp.dummy_head
            prev = dummy_head
            data = []
            while prev.next:
                data.append(str(prev.next))
                prev = prev.next
            print(data)


if __name__ == '__main__':
    graph = Graph(['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7'])

    graph.union(0, 1, 2)
    graph.union(0, 3, 1)
    graph.union(0, 2, 4)
    graph.union(1, 3, 3)
    graph.union(1, 4, 10)
    graph.union(3, 4, 2)
    graph.union(3, 6, 4)
    graph.union(3, 5, 8)
    graph.union(2, 3, 2)
    graph.union(2, 5, 5)

    c = graph.dijkstra(0)
    for i in range(len(c)):
        print(c[i], '->', i)
