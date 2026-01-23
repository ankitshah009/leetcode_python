#1514. Path with Maximum Probability
#Medium
#
#You are given an undirected weighted graph of n nodes (0-indexed), represented
#by an edge list where edges[i] = [a, b] is an undirected edge connecting the
#nodes a and b with a probability of success of traversing that edge succProb[i].
#
#Given two nodes start and end, find the path with the maximum probability of
#success to go from start to end and return its success probability.
#
#If there is no path from start to end, return 0. Your answer will be accepted
#if it differs from the correct answer by at most 1e-5.
#
#Example 1:
#Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
#Output: 0.25000
#Explanation: There are two paths from start to end, one having a probability of
#success = 0.2 and the other has 0.5 * 0.5 = 0.25.
#
#Example 2:
#Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
#Output: 0.30000
#
#Example 3:
#Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
#Output: 0.00000
#Explanation: There is no path between 0 and 2.
#
#Constraints:
#    2 <= n <= 10^4
#    0 <= edges.length <= 2 * 10^4
#    edges[i].length == 2
#    0 <= a, b < n
#    a != b
#    0 <= succProb.length == edges.length <= 2 * 10^4
#    0 <= succProb[i] <= 1
#    There is at most one edge between every two nodes.

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start: int, end: int) -> float:
        """
        Modified Dijkstra's algorithm to find maximum probability path.
        Use max-heap (negate values for min-heap).
        """
        # Build adjacency list
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        # Max-heap: (-probability, node)
        heap = [(-1.0, start)]  # Start with probability 1
        max_prob = [0.0] * n
        max_prob[start] = 1.0

        while heap:
            neg_prob, node = heapq.heappop(heap)
            prob = -neg_prob

            if node == end:
                return prob

            # Skip if we found a better path already
            if prob < max_prob[node]:
                continue

            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

        return 0.0


class SolutionBellmanFord:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start: int, end: int) -> float:
        """
        Bellman-Ford style relaxation.
        Converges in at most n-1 iterations.
        """
        max_prob = [0.0] * n
        max_prob[start] = 1.0

        for _ in range(n - 1):
            updated = False
            for (a, b), prob in zip(edges, succProb):
                if max_prob[a] * prob > max_prob[b]:
                    max_prob[b] = max_prob[a] * prob
                    updated = True
                if max_prob[b] * prob > max_prob[a]:
                    max_prob[a] = max_prob[b] * prob
                    updated = True

            if not updated:
                break

        return max_prob[end]


class SolutionBFS:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start: int, end: int) -> float:
        """
        BFS with updates when better probability found.
        """
        from collections import deque

        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        queue = deque([start])

        while queue:
            node = queue.popleft()

            for neighbor, edge_prob in graph[node]:
                new_prob = max_prob[node] * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    queue.append(neighbor)

        return max_prob[end]


class SolutionLogDijkstra:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start: int, end: int) -> float:
        """
        Use log transformation: max(p1*p2*...) = max(-log(p1)-log(p2)-...)
        Convert to standard shortest path.
        """
        import math

        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            if prob > 0:
                log_prob = -math.log(prob)
                graph[a].append((b, log_prob))
                graph[b].append((a, log_prob))

        # Standard Dijkstra for shortest path
        dist = [float('inf')] * n
        dist[start] = 0

        heap = [(0, start)]

        while heap:
            d, node = heapq.heappop(heap)

            if node == end:
                return math.exp(-d)

            if d > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        return 0.0
