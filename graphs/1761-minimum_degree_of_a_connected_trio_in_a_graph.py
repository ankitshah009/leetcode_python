#1761. Minimum Degree of a Connected Trio in a Graph
#Hard
#
#You are given an undirected graph. You are given an integer n which is the
#number of nodes in the graph and an array edges, where each edges[i] = [ui, vi]
#indicates that there is an undirected edge between ui and vi.
#
#A connected trio is a set of three nodes where there is an edge between every
#pair of them.
#
#The degree of a connected trio is the number of edges where one endpoint is in
#the trio, and the other is not.
#
#Return the minimum degree of a connected trio in the graph, or -1 if the graph
#has no connected trios.
#
#Example 1:
#Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
#Output: 3
#
#Example 2:
#Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
#Output: 0
#
#Constraints:
#    2 <= n <= 400
#    edges[i].length == 2
#    1 <= ui, vi <= n
#    ui != vi
#    There are no repeated edges.

from typing import List

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        """
        Find all triangles and compute their degrees.
        Optimization: order edges by degree to reduce iterations.
        """
        # Build adjacency set and degree count
        adj = set()
        degree = [0] * (n + 1)

        for u, v in edges:
            adj.add((min(u, v), max(u, v)))
            degree[u] += 1
            degree[v] += 1

        min_degree = float('inf')

        # Check all potential triangles
        for u, v in edges:
            # Ensure u < v for consistency
            if u > v:
                u, v = v, u

            # Find common neighbors
            for w in range(1, n + 1):
                if w != u and w != v:
                    # Check if u-w and v-w edges exist
                    uw = (min(u, w), max(u, w))
                    vw = (min(v, w), max(v, w))

                    if uw in adj and vw in adj:
                        # Found triangle u-v-w
                        # Degree = total degree - 6 (each internal edge counted twice)
                        trio_degree = degree[u] + degree[v] + degree[w] - 6
                        min_degree = min(min_degree, trio_degree)

        return min_degree if min_degree != float('inf') else -1


class SolutionOptimized:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        """
        Optimized with directed graph by degree.
        """
        from collections import defaultdict

        # Build undirected adjacency and degree
        adj = defaultdict(set)
        degree = [0] * (n + 1)

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1

        min_degree = float('inf')

        # Direct edges from lower degree to higher degree (or lower id for ties)
        directed = defaultdict(set)
        for u, v in edges:
            if (degree[u], u) < (degree[v], v):
                directed[u].add(v)
            else:
                directed[v].add(u)

        # Find triangles
        for u in range(1, n + 1):
            for v in directed[u]:
                for w in directed[v]:
                    if w in directed[u]:
                        trio_degree = degree[u] + degree[v] + degree[w] - 6
                        min_degree = min(min_degree, trio_degree)

        return min_degree if min_degree != float('inf') else -1
