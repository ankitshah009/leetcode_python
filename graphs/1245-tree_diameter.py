#1245. Tree Diameter
#Medium
#
#The diameter of a tree is the number of edges in the longest path in that tree.
#
#There is an undirected tree of n nodes labeled from 0 to n - 1. You are given
#a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates
#that there is an undirected edge between nodes ai and bi in the tree.
#
#Return the diameter of the tree.
#
#Example 1:
#Input: edges = [[0,1],[0,2]]
#Output: 2
#Explanation: The longest path of the tree is 0 - 1 and 0 - 2.
#
#Example 2:
#Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
#Output: 4
#Explanation: The longest path of the tree is 3 - 2 - 1 - 4 - 5.
#
#Constraints:
#    n == edges.length + 1
#    1 <= n <= 10^4
#    0 <= ai, bi < n
#    ai != bi

from typing import List
from collections import defaultdict, deque

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        DFS from each node to find deepest path.
        Diameter = max(depth(left) + depth(right)) for any node.
        """
        if not edges:
            return 0

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.diameter = 0

        def dfs(node, parent):
            """Return max depth from node. Update diameter."""
            max_depth = 0
            second_max = 0

            for neighbor in graph[node]:
                if neighbor != parent:
                    depth = 1 + dfs(neighbor, node)
                    if depth > max_depth:
                        second_max = max_depth
                        max_depth = depth
                    elif depth > second_max:
                        second_max = depth

            # Diameter through this node
            self.diameter = max(self.diameter, max_depth + second_max)

            return max_depth

        dfs(0, -1)
        return self.diameter


class SolutionBFS:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        Two BFS approach:
        1. BFS from any node to find farthest node (call it A)
        2. BFS from A to find farthest node - that distance is diameter
        """
        if not edges:
            return 0

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            """Return (farthest node, distance)"""
            visited = {start}
            queue = deque([(start, 0)])
            farthest = start
            max_dist = 0

            while queue:
                node, dist = queue.popleft()
                if dist > max_dist:
                    max_dist = dist
                    farthest = node

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

            return farthest, max_dist

        # First BFS from node 0
        farthest_node, _ = bfs(0)

        # Second BFS from farthest node
        _, diameter = bfs(farthest_node)

        return diameter
