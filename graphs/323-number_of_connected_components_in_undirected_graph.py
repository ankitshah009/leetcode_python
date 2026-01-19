#323. Number of Connected Components in an Undirected Graph
#Medium
#
#You have a graph of n nodes. You are given an integer n and an array edges
#where edges[i] = [ai, bi] indicates that there is an edge between ai and bi
#in the graph.
#
#Return the number of connected components in the graph.
#
#Example 1:
#Input: n = 5, edges = [[0,1],[1,2],[3,4]]
#Output: 2
#
#Example 2:
#Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
#Output: 1
#
#Constraints:
#    1 <= n <= 2000
#    1 <= edges.length <= 5000
#    edges[i].length == 2
#    0 <= ai <= bi < n
#    ai != bi
#    There are no repeated edges.

from typing import List
from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Union-Find approach"""
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False

            # Union by rank
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        components = n
        for a, b in edges:
            if union(a, b):
                components -= 1

        return components


class SolutionDFS:
    """DFS approach"""

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1

        return components


class SolutionBFS:
    """BFS approach"""

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        components = 0

        for start in range(n):
            if start in visited:
                continue

            components += 1
            queue = deque([start])
            visited.add(start)

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return components


class SolutionUnionFindSimple:
    """Simpler Union-Find without rank"""

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            # Path compression
            while parent[x] != root:
                parent[x], x = root, parent[x]
            return root

        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb
                n -= 1

        return n
