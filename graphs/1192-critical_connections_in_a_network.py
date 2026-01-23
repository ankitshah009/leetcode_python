#1192. Critical Connections in a Network
#Hard
#
#There are n servers numbered from 0 to n - 1 connected by undirected
#server-to-server connections forming a network where connections[i] = [ai, bi]
#represents a connection between servers ai and bi. Any server can reach other
#servers directly or indirectly through the network.
#
#A critical connection is a connection that, if removed, will make some servers
#unable to reach some other server.
#
#Return all critical connections in the network in any order.
#
#Example 1:
#Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
#Output: [[1,3]]
#Explanation: [[3,1]] is also accepted.
#
#Example 2:
#Input: n = 2, connections = [[0,1]]
#Output: [[0,1]]
#
#Constraints:
#    2 <= n <= 10^5
#    n - 1 <= connections.length <= 10^5
#    0 <= ai, bi <= n - 1
#    ai != bi
#    There are no repeated connections.

from typing import List
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Tarjan's algorithm for finding bridges.
        A bridge is an edge whose removal disconnects the graph.

        For each node, track:
        - disc[u]: discovery time
        - low[u]: lowest discovery time reachable from subtree of u

        Edge (u, v) is a bridge if low[v] > disc[u]
        (meaning v cannot reach anything at or before u without using edge u-v)
        """
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n  # Discovery time
        low = [0] * n    # Lowest reachable discovery time
        bridges = []
        time = [0]  # Use list for mutable closure

        def dfs(u, parent):
            disc[u] = low[u] = time[0]
            time[0] += 1

            for v in graph[u]:
                if disc[v] == -1:  # Not visited
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    # If v cannot reach anything at or before u
                    if low[v] > disc[u]:
                        bridges.append([u, v])
                elif v != parent:  # Back edge
                    low[u] = min(low[u], disc[v])

        # Start DFS from node 0 (graph is connected)
        dfs(0, -1)

        return bridges


class SolutionIterative:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """Iterative version to avoid stack overflow"""
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [0] * n
        bridges = []
        time = 0

        # Use explicit stack: (node, parent, iterator, phase)
        # phase 0: initial visit, phase 1: process children
        stack = [(0, -1, iter(graph[0]), 0)]
        disc[0] = low[0] = time
        time += 1

        while stack:
            u, parent, children, phase = stack.pop()

            if phase == 1:
                # Coming back from child v
                v = children  # In phase 1, children holds the child node
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append([u, v])
                # Restore iterator
                stack.append((u, parent, graph[u][graph[u].index(v) + 1:], 0))
                continue

            for v in children:
                if disc[v] == -1:
                    disc[v] = low[v] = time
                    time += 1
                    # Save current state and go to child
                    stack.append((u, parent, v, 1))  # Phase 1 to process return
                    stack.append((v, u, iter(graph[v]), 0))
                    break
                elif v != parent:
                    low[u] = min(low[u], disc[v])

        return bridges
