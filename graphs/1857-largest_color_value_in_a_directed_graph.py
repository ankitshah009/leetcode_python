#1857. Largest Color Value in a Directed Graph
#Hard
#
#There is a directed graph of n colored nodes and m edges. The nodes are
#numbered from 0 to n - 1.
#
#You are given a string colors where colors[i] is a lowercase English letter
#representing the color of the ith node in this graph (0-indexed). You are also
#given a 2D array edges where edges[j] = [a_j, b_j] indicates that there is a
#directed edge from node a_j to node b_j.
#
#A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk
#such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The
#color value of the path is the number of nodes that are colored the most
#frequently occurring color along that path.
#
#Return the largest color value of any valid path in the given graph, or -1 if
#the graph contains a cycle.
#
#Example 1:
#Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
#Output: 3
#
#Example 2:
#Input: colors = "a", edges = [[0,0]]
#Output: -1
#
#Constraints:
#    n == colors.length
#    m == edges.length
#    1 <= n <= 10^5
#    0 <= m <= 10^5
#    colors consists of lowercase English letters.
#    0 <= a_j, b_j < n

from typing import List
from collections import deque, defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        Topological sort with DP.
        dp[node][color] = max count of color on any path ending at node.
        """
        n = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            in_degree[b] += 1

        # dp[node][color] = max count of that color ending at node
        dp = [[0] * 26 for _ in range(n)]

        # Initialize with nodes' own colors
        for i in range(n):
            dp[i][ord(colors[i]) - ord('a')] = 1

        # Kahn's algorithm for topological sort
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        processed = 0
        max_color = 0

        while queue:
            node = queue.popleft()
            processed += 1
            max_color = max(max_color, max(dp[node]))

            for neighbor in graph[node]:
                # Update neighbor's dp with current node's values
                for c in range(26):
                    extra = 1 if c == ord(colors[neighbor]) - ord('a') else 0
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c] + extra)

                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If not all nodes processed, there's a cycle
        return max_color if processed == n else -1


class SolutionDFS:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        DFS with memoization and cycle detection.
        """
        n = len(colors)
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)

        # 0 = unvisited, 1 = in current path, 2 = fully processed
        state = [0] * n
        dp = [[0] * 26 for _ in range(n)]

        def dfs(node: int) -> bool:
            """Returns False if cycle detected."""
            if state[node] == 1:  # Cycle
                return False
            if state[node] == 2:  # Already processed
                return True

            state[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
                for c in range(26):
                    dp[node][c] = max(dp[node][c], dp[neighbor][c])

            # Add current node's color
            dp[node][ord(colors[node]) - ord('a')] += 1
            state[node] = 2
            return True

        for i in range(n):
            if state[i] == 0:
                if not dfs(i):
                    return -1

        return max(max(row) for row in dp)
