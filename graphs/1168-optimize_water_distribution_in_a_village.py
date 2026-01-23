#1168. Optimize Water Distribution in a Village
#Hard
#
#There are n houses in a village. We want to supply water for all the houses
#by building wells and laying pipes.
#
#For each house i, we can either build a well inside it directly with cost
#wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another
#well to it. The costs to lay pipes between houses are given by the array pipes
#where each pipes[j] = [house1j, house2j, costj] represents the cost to connect
#house1j and house2j together using a pipe.
#
#Return the minimum total cost to supply water to all houses.
#
#Example 1:
#Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
#Output: 3
#Explanation: Build a well in the first house with cost 1.
#Connect house 2 to house 1 with cost 1.
#Connect house 3 to house 2 with cost 1.
#Total cost = 1 + 1 + 1 = 3.
#
#Example 2:
#Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
#Output: 2
#
#Constraints:
#    2 <= n <= 10^4
#    wells.length == n
#    0 <= wells[i] <= 10^5
#    1 <= pipes.length <= 10^4
#    pipes[j].length == 3
#    1 <= house1j, house2j <= n
#    0 <= costj <= 10^5
#    house1j != house2j

from typing import List
import heapq

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """
        Create virtual node 0 (water source).
        Edge from 0 to house i has cost wells[i-1].
        Find MST using Prim's algorithm.
        """
        # Build adjacency list
        graph = [[] for _ in range(n + 1)]

        # Add edges from virtual node 0 to each house (well cost)
        for i in range(n):
            graph[0].append((wells[i], i + 1))
            graph[i + 1].append((wells[i], 0))

        # Add pipe edges
        for h1, h2, cost in pipes:
            graph[h1].append((cost, h2))
            graph[h2].append((cost, h1))

        # Prim's algorithm from node 0
        visited = set([0])
        heap = graph[0][:]  # Start with edges from node 0
        heapq.heapify(heap)
        total_cost = 0

        while len(visited) <= n:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            total_cost += cost

            for next_cost, next_node in graph[node]:
                if next_node not in visited:
                    heapq.heappush(heap, (next_cost, next_node))

        return total_cost


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


class SolutionKruskal:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """Kruskal's algorithm with Union-Find"""
        # Create edges: virtual node 0 to each house
        edges = []
        for i in range(n):
            edges.append((wells[i], 0, i + 1))

        # Add pipe edges
        for h1, h2, cost in pipes:
            edges.append((cost, h1, h2))

        # Sort by cost
        edges.sort()

        # Kruskal's algorithm
        uf = UnionFind(n + 1)
        total_cost = 0
        edges_used = 0

        for cost, u, v in edges:
            if uf.union(u, v):
                total_cost += cost
                edges_used += 1
                if edges_used == n:
                    break

        return total_cost
