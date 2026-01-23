#1971. Find if Path Exists in Graph
#Easy
#
#There is a bi-directional graph with n vertices, where each vertex is labeled
#from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
#integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
#edge between vertex ui and vertex vi. Every vertex pair is connected by at
#most one edge, and no vertex has an edge to itself.
#
#You want to determine if there is a valid path that exists from vertex source
#to vertex destination.
#
#Given edges and the integers n, source, and destination, return true if there
#is a valid path from source to destination, or false otherwise.
#
#Example 1:
#Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
#Output: true
#
#Example 2:
#Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
#Output: false
#
#Constraints:
#    1 <= n <= 2 * 10^5
#    0 <= edges.length <= 2 * 10^5
#    edges[i].length == 2
#    0 <= ui, vi <= n - 1
#    ui != vi
#    0 <= source, destination <= n - 1
#    There are no duplicate edges.
#    There are no self edges.

from typing import List
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        BFS to find path from source to destination.
        """
        if source == destination:
            return True

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS
        visited = {source}
        queue = deque([source])

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if neighbor == destination:
                    return True

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False


class SolutionDFS:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        DFS approach.
        """
        if source == destination:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node: int) -> bool:
            if node == destination:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)


class SolutionUnionFind:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Union-Find to check connectivity.
        """
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] < rank[py]:
                    px, py = py, px
                parent[py] = px
                if rank[px] == rank[py]:
                    rank[px] += 1

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)
