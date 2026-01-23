#882. Reachable Nodes In Subdivided Graph
#Hard
#
#You are given an undirected graph (the "original graph") with n nodes labeled
#from 0 to n - 1. You decide to subdivide each edge in the graph into a chain
#of nodes, with the number of new nodes varying between each edge.
#
#The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti]
#indicates that there is an edge between nodes ui and vi in the original graph,
#and cnti is the total number of new nodes that you will subdivide the edge into.
#
#The subdivided edge consists of cnti + 2 nodes in total: original ui, original vi,
#and cnti new nodes.
#
#You are also given an integer maxMoves. Return the maximum number of nodes you
#can reach from node 0, given that you have maxMoves moves.
#
#Example 1:
#Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
#Output: 13
#
#Example 2:
#Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
#Output: 23
#
#Constraints:
#    0 <= edges.length <= min(n * (n - 1) / 2, 10^4)
#    edges[i].length == 3
#    0 <= ui < vi < n
#    There are no multiple edges in the graph.
#    0 <= cnti <= 10^4
#    0 <= maxMoves <= 10^9
#    1 <= n <= 3000

import heapq
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        """
        Dijkstra's algorithm to find shortest paths.
        Track how many subdivision nodes we can reach on each edge.
        """
        # Build graph
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt

        # Dijkstra from node 0
        dist = {0: 0}
        heap = [(0, 0)]  # (distance, node)

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist.get(u, float('inf')):
                continue

            for v, cnt in graph[u].items():
                # Edge weight = cnt + 1 (need to traverse cnt subdivision nodes + 1)
                new_dist = d + cnt + 1
                if new_dist < dist.get(v, float('inf')):
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        # Count reachable nodes
        count = 0

        # Original nodes reachable
        count += sum(1 for node in range(n) if dist.get(node, float('inf')) <= maxMoves)

        # Subdivision nodes on each edge
        for u, v, cnt in edges:
            # From u's side
            from_u = max(0, maxMoves - dist.get(u, float('inf')))
            # From v's side
            from_v = max(0, maxMoves - dist.get(v, float('inf')))
            # Total from this edge (can't exceed cnt)
            count += min(cnt, from_u + from_v)

        return count
