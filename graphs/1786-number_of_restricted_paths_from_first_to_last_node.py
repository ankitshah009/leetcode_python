#1786. Number of Restricted Paths From First to Last Node
#Medium
#
#There is an undirected weighted connected graph. You are given a positive
#integer n which denotes that the graph has n nodes labeled from 1 to n, and an
#array edges where each edges[i] = [ui, vi, weighti] denotes that there is an
#edge between nodes ui and vi with weight equal to weighti.
#
#A path from node start to node end is a sequence of nodes [z0, z1, ..., zk]
#such that z0 = start and zk = end and there is an edge between zi and zi+1
#where 0 <= i <= k-1.
#
#The distance of a path is the sum of the weights on the edges of the path. Let
#distanceToLastNode(x) denote the shortest distance of a path between node x and
#node n in the graph.
#
#A restricted path is a path that also satisfies that
#distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.
#
#Return the number of restricted paths from node 1 to node n. Since that number
#may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
#Output: 3
#
#Example 2:
#Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
#Output: 1
#
#Constraints:
#    1 <= n <= 2 * 10^4
#    n - 1 <= edges.length <= 4 * 10^4
#    edges[i].length == 3
#    1 <= ui, vi <= n
#    ui != vi
#    1 <= weighti <= 10^5
#    There is at most one edge between any two nodes.
#    There is at least one path between any two nodes.

from typing import List
import heapq
from collections import defaultdict
from functools import lru_cache

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        """
        1. Dijkstra from node n to get distances
        2. DFS/DP to count restricted paths
        """
        MOD = 10**9 + 7

        # Build graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra from node n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        # Count restricted paths using DFS with memoization
        @lru_cache(maxsize=None)
        def dfs(node: int) -> int:
            if node == n:
                return 1

            count = 0
            for neighbor, _ in graph[node]:
                if dist[node] > dist[neighbor]:  # Restricted path condition
                    count = (count + dfs(neighbor)) % MOD

            return count

        return dfs(1)


class SolutionTopSort:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        """
        Topological sort based on distances.
        """
        MOD = 10**9 + 7

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra from n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                if d + weight < dist[neighbor]:
                    dist[neighbor] = d + weight
                    heapq.heappush(heap, (dist[neighbor], neighbor))

        # Sort nodes by distance (ascending) and compute paths
        nodes = list(range(1, n + 1))
        nodes.sort(key=lambda x: dist[x])

        dp = [0] * (n + 1)
        dp[n] = 1

        for node in nodes:
            for neighbor, _ in graph[node]:
                if dist[neighbor] < dist[node]:
                    dp[node] = (dp[node] + dp[neighbor]) % MOD

        return dp[1]
