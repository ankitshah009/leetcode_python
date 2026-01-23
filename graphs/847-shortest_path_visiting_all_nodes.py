#847. Shortest Path Visiting All Nodes
#Hard
#
#You have an undirected, connected graph of n nodes labeled from 0 to n - 1.
#You are given an array graph where graph[i] is a list of all the nodes
#connected with node i by an edge.
#
#Return the length of the shortest path that visits every node. You may start
#and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
#
#Example 1:
#Input: graph = [[1,2,3],[0],[0],[0]]
#Output: 4
#Explanation: One possible path is [1,0,2,0,3]
#
#Example 2:
#Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
#Output: 4
#Explanation: One possible path is [0,1,4,2,3]
#
#Constraints:
#    n == graph.length
#    1 <= n <= 12
#    0 <= graph[i].length < n
#    graph[i] does not contain i.
#    If graph[a] contains b, then graph[b] contains a.
#    The input graph is always connected.

from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        """
        BFS with state = (current_node, visited_bitmask).
        """
        n = len(graph)
        if n == 1:
            return 0

        target = (1 << n) - 1  # All nodes visited

        # BFS: (node, visited_mask)
        queue = deque()
        visited = set()

        # Start from all nodes
        for i in range(n):
            state = (i, 1 << i)
            queue.append((i, 1 << i, 0))  # node, mask, distance
            visited.add(state)

        while queue:
            node, mask, dist = queue.popleft()

            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)

                if new_mask == target:
                    return dist + 1

                state = (neighbor, new_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((neighbor, new_mask, dist + 1))

        return -1


class SolutionDP:
    """DP with bitmask"""

    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0

        # dp[mask][i] = min distance to reach node i with visited set = mask
        INF = float('inf')
        dp = [[INF] * n for _ in range(1 << n)]

        queue = deque()
        for i in range(n):
            dp[1 << i][i] = 0
            queue.append((1 << i, i))

        target = (1 << n) - 1

        while queue:
            mask, u = queue.popleft()

            if mask == target:
                return dp[mask][u]

            for v in graph[u]:
                new_mask = mask | (1 << v)

                if dp[new_mask][v] > dp[mask][u] + 1:
                    dp[new_mask][v] = dp[mask][u] + 1
                    queue.append((new_mask, v))

        return dp[target][0]  # Should not reach here
