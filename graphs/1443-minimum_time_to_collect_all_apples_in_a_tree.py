#1443. Minimum Time to Collect All Apples in a Tree
#Medium
#
#Given an undirected tree consisting of n vertices numbered from 0 to n-1, which
#has some apples in their vertices. You spend 1 second to walk over one edge of
#the tree. Return the minimum time in seconds you have to spend to collect all
#apples in the tree, starting at vertex 0 and coming back to this vertex.
#
#The edges of the undirected tree are given in the array edges, where
#edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.
#Additionally, there is a boolean array hasApple, where hasApple[i] = true means
#that vertex i has an apple; otherwise, it does not have any apple.
#
#Example 1:
#Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
#Output: 8
#Explanation: The figure above represents the given tree where red vertices have
#an apple. One optimal path to collect all apples is shown by the green arrows.
#
#Example 2:
#Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
#Output: 6
#Explanation: The figure above represents the given tree where red vertices have
#an apple. One optimal path to collect all apples is shown by the green arrows.
#
#Example 3:
#Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
#Output: 0
#
#Constraints:
#    1 <= n <= 10^5
#    edges.length == n - 1
#    edges[i].length == 2
#    0 <= ai < bi <= n - 1
#    hasApple.length == n

from typing import List
from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        DFS from root. For each subtree, if it contains an apple,
        we need 2 seconds (down and back) to visit it.
        """
        # Build adjacency list
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node: int, parent: int) -> int:
            """Return time needed to collect all apples in subtree of node"""
            total_time = 0

            for child in adj[node]:
                if child != parent:
                    child_time = dfs(child, node)
                    # If subtree has apples, add 2 for this edge
                    if child_time > 0 or hasApple[child]:
                        total_time += child_time + 2

            return total_time

        return dfs(0, -1)


class SolutionIterative:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """Iterative DFS using stack"""
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # Post-order traversal with stack
        visited = [False] * n
        parent = [-1] * n
        order = []  # Post-order

        stack = [0]
        while stack:
            node = stack[-1]
            if not visited[node]:
                visited[node] = True
                for child in adj[node]:
                    if not visited[child]:
                        parent[child] = node
                        stack.append(child)
            else:
                stack.pop()
                order.append(node)

        # Process in post-order
        time = [0] * n
        for node in order:
            if node == 0:
                continue
            p = parent[node]
            # If this subtree needs to be visited
            if time[node] > 0 or hasApple[node]:
                time[p] += time[node] + 2

        return time[0]


class SolutionBFS:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """BFS to find distances, then sum needed edges"""
        from collections import deque

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # DFS to mark nodes on path to any apple
        on_path = [False] * n

        def mark_path(node: int, parent: int) -> bool:
            has_apple_in_subtree = hasApple[node]

            for child in adj[node]:
                if child != parent:
                    if mark_path(child, node):
                        has_apple_in_subtree = True

            if has_apple_in_subtree:
                on_path[node] = True

            return has_apple_in_subtree

        mark_path(0, -1)

        # Count edges on paths to apples (each edge counted once, traversed twice)
        edge_count = 0
        for node in range(1, n):
            if on_path[node]:
                edge_count += 1

        return edge_count * 2
