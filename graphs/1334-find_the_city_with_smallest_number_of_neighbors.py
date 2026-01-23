#1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
#Medium
#
#There are n cities numbered from 0 to n-1. Given the array edges where
#edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge
#between cities fromi and toi, and given the integer distanceThreshold.
#
#Return the city with the smallest number of cities that are reachable through
#some path and whose distance is at most distanceThreshold, If there are
#multiple such cities, return the city with the greatest number.
#
#Notice that the distance of a path connecting cities i and j is equal to the
#sum of the edges' weights along that path.
#
#Example 1:
#Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
#Output: 3
#Explanation: The figure above describes the graph.
#The neighboring cities at a distanceThreshold = 4 for each city are:
#City 0 -> [City 1, City 2]
#City 1 -> [City 0, City 2, City 3]
#City 2 -> [City 0, City 1, City 3]
#City 3 -> [City 1, City 2]
#Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
#
#Example 2:
#Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
#Output: 0
#
#Constraints:
#    2 <= n <= 100
#    1 <= edges.length <= n * (n - 1) / 2
#    edges[i].length == 3
#    0 <= fromi < toi < n
#    1 <= weighti, distanceThreshold <= 10^4
#    All pairs (fromi, toi) are distinct.

from typing import List
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
        Floyd-Warshall to find all pairs shortest paths.
        Then count reachable cities for each city.
        """
        INF = float('inf')

        # Initialize distance matrix
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Count reachable cities for each city
        result_city = 0
        min_reachable = n

        for i in range(n):
            reachable = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            if reachable <= min_reachable:
                min_reachable = reachable
                result_city = i

        return result_city


class SolutionDijkstra:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """Run Dijkstra from each city"""
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]

            while heap:
                d, u = heapq.heappop(heap)
                if d > dist[u]:
                    continue
                for v, w in adj[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(heap, (dist[v], v))

            return dist

        result_city = 0
        min_reachable = n

        for i in range(n):
            dist = dijkstra(i)
            reachable = sum(1 for d in dist if 0 < d <= distanceThreshold)

            if reachable <= min_reachable:
                min_reachable = reachable
                result_city = i

        return result_city
