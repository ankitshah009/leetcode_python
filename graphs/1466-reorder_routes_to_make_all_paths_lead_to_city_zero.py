#1466. Reorder Routes to Make All Paths Lead to the City Zero
#Medium
#
#There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is
#only one way to travel between two different cities (this network form a tree).
#Last year, The ministry of transport decided to orient the roads in one direction
#because they are too narrow.
#
#Roads are represented by connections where connections[i] = [ai, bi] represents
#a road from city ai to city bi.
#
#This year, there will be a big event in the capital (city 0), and many people
#want to travel to this city.
#
#Your task consists of reorienting some roads such that each city can visit the
#city 0. Return the minimum number of roads changed.
#
#It's guaranteed that each city can reach city 0 after reorder.
#
#Example 1:
#Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
#Output: 3
#Explanation: Change the direction of edges shown in red such that each node can
#reach the node 0.
#
#Example 2:
#Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
#Output: 2
#Explanation: Change the direction of edges shown in red such that each node can
#reach the node 0.
#
#Example 3:
#Input: n = 3, connections = [[1,0],[2,0]]
#Output: 0
#
#Constraints:
#    2 <= n <= 5 * 10^4
#    connections.length == n - 1
#    connections[i].length == 2
#    0 <= ai, bi <= n - 1
#    ai != bi

from typing import List
from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        BFS/DFS from city 0.
        Build undirected graph but track original direction.
        Count roads pointing away from 0 (need to be reversed).
        """
        # Build adjacency list with direction info
        # (neighbor, needs_reversal): 1 if original edge goes away from current
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))  # a -> b: if we traverse a to b, needs reversal
            graph[b].append((a, 0))  # b -> a: if we traverse b to a, already correct

        visited = [False] * n
        changes = 0

        # BFS from city 0
        queue = deque([0])
        visited[0] = True

        while queue:
            city = queue.popleft()

            for neighbor, cost in graph[city]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    changes += cost  # Add cost if edge points away
                    queue.append(neighbor)

        return changes


class SolutionDFS:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        DFS approach with same logic.
        """
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = [False] * n

        def dfs(node: int) -> int:
            visited[node] = True
            changes = 0

            for neighbor, cost in graph[node]:
                if not visited[neighbor]:
                    changes += cost + dfs(neighbor)

            return changes

        return dfs(0)


class SolutionSet:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Use set to track original directions.
        """
        # Store original edges as (from, to)
        original = set()
        graph = defaultdict(list)

        for a, b in connections:
            original.add((a, b))
            graph[a].append(b)
            graph[b].append(a)

        visited = set([0])
        changes = 0

        queue = deque([0])
        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # If original edge goes node -> neighbor, need to reverse
                    if (node, neighbor) in original:
                        changes += 1
                    queue.append(neighbor)

        return changes
