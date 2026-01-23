#1615. Maximal Network Rank
#Medium
#
#There is an infrastructure of n cities with some number of roads connecting
#these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional
#road between cities ai and bi.
#
#The network rank of two different cities is defined as the total number of
#directly connected roads to either city. If a road is directly connected to
#both cities, it is only counted once.
#
#The maximal network rank of the infrastructure is the maximum network rank of
#all pairs of different cities.
#
#Given the integer n and the array roads, return the maximal network rank of
#the entire infrastructure.
#
#Example 1:
#Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
#Output: 4
#Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads
#connected to city 0 or 1. The road between 0 and 1 is only counted once.
#
#Example 2:
#Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
#Output: 5
#Explanation: There are 5 roads connected to cities 1 or 2.
#
#Example 3:
#Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
#Output: 5
#
#Constraints:
#    2 <= n <= 100
#    0 <= roads.length <= n * (n - 1) / 2
#    roads[i].length == 2
#    0 <= ai, bi <= n-1
#    ai != bi
#    Each pair of cities has at most one road connecting them.

from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """
        Count degree of each city and check all pairs.
        """
        # Count degrees
        degree = [0] * n
        connected = set()

        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected.add((min(a, b), max(a, b)))

        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                # Subtract 1 if directly connected (counted twice)
                if (i, j) in connected:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank


class SolutionAdjMatrix:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """
        Using adjacency matrix for O(1) connection lookup.
        """
        adj = [[False] * n for _ in range(n)]
        degree = [0] * n

        for a, b in roads:
            adj[a][b] = adj[b][a] = True
            degree[a] += 1
            degree[b] += 1

        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if adj[i][j]:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank


class SolutionOptimized:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """
        Optimized: Focus on nodes with highest degrees.
        """
        if not roads:
            return 0

        degree = [0] * n
        edges = set()

        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            edges.add((min(a, b), max(a, b)))

        # Get max degree and second max degree
        max_deg = max(degree)
        max_nodes = [i for i in range(n) if degree[i] == max_deg]

        if len(max_nodes) >= 2:
            # Check if any pair of max degree nodes are NOT connected
            for i in range(len(max_nodes)):
                for j in range(i + 1, len(max_nodes)):
                    a, b = max_nodes[i], max_nodes[j]
                    if (min(a, b), max(a, b)) not in edges:
                        return 2 * max_deg
            # All max nodes are connected to each other
            return 2 * max_deg - 1

        # Only one max node, pair with second max
        # Find second max that's not connected to max node
        max_node = max_nodes[0]

        # Find best partner
        best = 0
        for i in range(n):
            if i != max_node:
                rank = degree[max_node] + degree[i]
                if (min(max_node, i), max(max_node, i)) in edges:
                    rank -= 1
                best = max(best, rank)

        return best
