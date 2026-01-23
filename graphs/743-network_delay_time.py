#743. Network Delay Time
#Medium
#
#You are given a network of n nodes, labeled from 1 to n. You are also given
#times, a list of travel times as directed edges times[i] = (ui, vi, wi), where
#ui is the source node, vi is the target node, and wi is the time it takes for
#a signal to travel from source to target.
#
#We will send a signal from a given node k. Return the minimum time it takes
#for all the n nodes to receive the signal. If it is impossible for all the n
#nodes to receive the signal, return -1.
#
#Example 1:
#Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
#Output: 2
#
#Example 2:
#Input: times = [[1,2,1]], n = 2, k = 1
#Output: 1
#
#Example 3:
#Input: times = [[1,2,1]], n = 2, k = 2
#Output: -1
#
#Constraints:
#    1 <= k <= n <= 100
#    1 <= times.length <= 6000
#    times[i].length == 3
#    1 <= ui, vi <= n
#    ui != vi
#    0 <= wi <= 100
#    All the pairs (ui, vi) are unique.

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Dijkstra's algorithm: find shortest path from k to all nodes.
        """
        # Build graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Dijkstra
        dist = {k: 0}
        heap = [(0, k)]

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist.get(u, float('inf')):
                continue

            for v, w in graph[u]:
                new_dist = d + w
                if new_dist < dist.get(v, float('inf')):
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        if len(dist) != n:
            return -1

        return max(dist.values())


class SolutionBellmanFord:
    """Bellman-Ford algorithm"""

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        for _ in range(n - 1):
            updated = False
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break

        max_dist = max(dist[1:])
        return max_dist if max_dist < float('inf') else -1


class SolutionFloydWarshall:
    """Floyd-Warshall for all pairs"""

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        INF = float('inf')
        dist = [[INF] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dist[i][i] = 0

        for u, v, w in times:
            dist[u][v] = w

        for mid in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])

        max_dist = max(dist[k][1:])
        return max_dist if max_dist < INF else -1


class SolutionDFS:
    """DFS with memoization"""

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        def dfs(node, time):
            if time >= dist[node]:
                return
            dist[node] = time

            for neighbor, weight in graph[node]:
                dfs(neighbor, time + weight)

        dfs(k, 0)

        max_dist = max(dist[1:])
        return max_dist if max_dist < float('inf') else -1
