#1059. All Paths from Source Lead to Destination
#Medium
#
#Given the edges of a directed graph where edges[i] = [ai, bi] indicates
#there is an edge between nodes ai and bi, and two nodes source and
#destination of this graph, determine whether or not all paths starting
#from source eventually, end at destination, that is:
#    At least one path exists from the source node to the destination node
#    If a path exists from the source node to a node with no outgoing edges,
#    then that node is equal to destination.
#    The number of possible paths from source to destination is a finite number.
#
#Return true if and only if all paths from source lead to destination.
#
#Example 1:
#Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
#Output: false
#Explanation: It is possible to reach and get stuck on both node 1 and 2.
#
#Example 2:
#Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
#Output: false
#Explanation: There is a path 0 -> 1 -> 2 -> 1 that doesn't end at 3.
#
#Example 3:
#Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
#Output: true
#
#Constraints:
#    1 <= n <= 10^4
#    0 <= edges.length <= 10^4
#    edges.length == 2
#    0 <= ai, bi <= n - 1
#    0 <= source <= n - 1
#    0 <= destination <= n - 1
#    The given graph may have self-loops and parallel edges.

from typing import List
from collections import defaultdict

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        DFS with cycle detection.
        1. Destination must have no outgoing edges.
        2. All paths from source must end at destination.
        3. No cycles (would mean infinite paths).
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        # Destination must have no outgoing edges
        if graph[destination]:
            return False

        # States: 0 = unvisited, 1 = visiting (in current path), 2 = visited (verified)
        state = [0] * n

        def dfs(node):
            if state[node] == 1:  # Cycle detected
                return False
            if state[node] == 2:  # Already verified
                return True

            # No outgoing edges - must be destination
            if not graph[node]:
                return node == destination

            state[node] = 1  # Mark as visiting

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2  # Mark as verified
            return True

        return dfs(source)


class SolutionIterative:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """Iterative DFS"""
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        if graph[destination]:
            return False

        # Color: 0 = white (unvisited), 1 = gray (in stack), 2 = black (done)
        color = [0] * n
        stack = [source]

        while stack:
            node = stack[-1]

            if color[node] == 2:
                stack.pop()
                continue

            if color[node] == 1:
                color[node] = 2
                stack.pop()
                continue

            color[node] = 1

            if not graph[node]:
                if node != destination:
                    return False
                color[node] = 2
                stack.pop()
                continue

            for neighbor in graph[node]:
                if color[neighbor] == 1:  # Cycle
                    return False
                if color[neighbor] == 0:
                    stack.append(neighbor)

        return True
