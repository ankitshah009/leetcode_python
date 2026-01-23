#1129. Shortest Path with Alternating Colors
#Medium
#
#You are given an integer n, the number of nodes in a directed graph where
#the nodes are labeled from 0 to n - 1. Each edge is red or blue in this
#graph, and there could be self-edges and parallel edges.
#
#You are given two arrays redEdges and blueEdges where:
#    redEdges[i] = [ai, bi] indicates that there is a directed red edge
#    from node ai to node bi in the graph, and
#    blueEdges[j] = [uj, vj] indicates that there is a directed blue edge
#    from node uj to node vj in the graph.
#
#Return an array answer of length n, where each answer[x] is the length of
#the shortest path from node 0 to node x such that the edge colors alternate
#along the path, or -1 if such a path does not exist.
#
#Example 1:
#Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
#Output: [0,1,-1]
#
#Example 2:
#Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
#Output: [0,1,-1]
#
#Constraints:
#    1 <= n <= 100
#    0 <= redEdges.length, blueEdges.length <= 400
#    redEdges[i].length == blueEdges[j].length == 2
#    0 <= ai, bi, uj, vj < n

from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """
        BFS with state (node, last_color).
        """
        RED, BLUE = 0, 1

        # Build graphs
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        # BFS: (node, last_color, distance)
        # Start with both colors
        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        visited = {(0, RED), (0, BLUE)}

        result = [-1] * n
        result[0] = 0

        while queue:
            node, last_color, dist = queue.popleft()

            # Get next graph based on alternating color
            if last_color == RED:
                next_graph = blue_graph
                next_color = BLUE
            else:
                next_graph = red_graph
                next_color = RED

            for neighbor in next_graph[node]:
                if (neighbor, next_color) not in visited:
                    visited.add((neighbor, next_color))
                    queue.append((neighbor, next_color, dist + 1))

                    if result[neighbor] == -1:
                        result[neighbor] = dist + 1

        return result


class SolutionAlternative:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """Combined graph with edge colors"""
        from collections import defaultdict, deque

        graph = defaultdict(list)  # node -> [(neighbor, color)]

        for u, v in redEdges:
            graph[u].append((v, 0))  # 0 = red
        for u, v in blueEdges:
            graph[u].append((v, 1))  # 1 = blue

        INF = float('inf')
        # dist[node][color] = shortest distance ending with edge of color
        dist = [[INF, INF] for _ in range(n)]
        dist[0] = [0, 0]

        queue = deque([(0, -1, 0)])  # (node, last_color, distance)

        while queue:
            node, last_color, d = queue.popleft()

            for neighbor, edge_color in graph[node]:
                if edge_color != last_color and dist[neighbor][edge_color] == INF:
                    dist[neighbor][edge_color] = d + 1
                    queue.append((neighbor, edge_color, d + 1))

        return [min(d) if min(d) != INF else -1 for d in dist]
