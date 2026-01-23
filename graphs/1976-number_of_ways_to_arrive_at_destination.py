#1976. Number of Ways to Arrive at Destination
#Medium
#
#You are in a city that consists of n intersections numbered from 0 to n - 1
#with bi-directional roads between some intersections. The inputs are generated
#such that you can reach any intersection from any other intersection and that
#there is at most one road between any two intersections.
#
#You are given an integer n and a 2D integer array roads where
#roads[i] = [ui, vi, timei] means that there is a road between intersections
#ui and vi that takes timei minutes to travel. You want to know in how many
#ways you can travel from intersection 0 to intersection n - 1 in the shortest
#amount of time.
#
#Return the number of ways you can arrive at your destination in the shortest
#amount of time. Since the answer may be large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
#Output: 4
#
#Example 2:
#Input: n = 2, roads = [[1,0,10]]
#Output: 1
#
#Constraints:
#    1 <= n <= 200
#    n - 1 <= roads.length <= n * (n - 1) / 2
#    roads[i].length == 3
#    0 <= ui, vi <= n - 1
#    1 <= timei <= 10^9
#    ui != vi
#    There is at most one road connecting any two intersections.
#    You can reach any intersection from any other intersection.

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        Dijkstra's algorithm tracking number of shortest paths.
        """
        MOD = 10**9 + 7

        # Build graph
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Dijkstra with path counting
        dist = [float('inf')] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]  # (distance, node)

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist[u]:
                continue

            for v, time in graph[u]:
                new_dist = d + time

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(heap, (new_dist, v))
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]


class SolutionDP:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        First find shortest paths, then count using DP.
        """
        MOD = 10**9 + 7

        # Build graph
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Dijkstra to find shortest distances
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist[u]:
                continue

            for v, time in graph[u]:
                if d + time < dist[v]:
                    dist[v] = d + time
                    heapq.heappush(heap, (dist[v], v))

        # Count paths using only shortest path edges
        # Sort nodes by distance and do DP
        order = sorted(range(n), key=lambda x: dist[x])
        ways = [0] * n
        ways[0] = 1

        for u in order:
            for v, time in graph[u]:
                if dist[v] == dist[u] + time:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]
