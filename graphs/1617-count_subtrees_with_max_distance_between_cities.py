#1617. Count Subtrees With Max Distance Between Cities
#Hard
#
#There are n cities numbered from 1 to n. You are given an array edges of size
#n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities
#ui and vi. There exists a unique path between each pair of cities.
#
#A subtree is a subset of cities where every city is reachable from every other
#city in the subset, with the path between each pair passing through only the
#cities from the subset. Two subtrees are different if there is a city in one
#subtree that is not present in the other.
#
#For each d from 1 to n-1, find the number of subtrees in which the maximum
#distance between any two cities in the subtree is equal to d.
#
#Return an array of size n-1 where the dth element (1-indexed) is the number
#of subtrees in which the maximum distance between any two cities is equal to d.
#
#Notice that the distance between the two cities is the number of edges in the
#path between them.
#
#Example 1:
#Input: n = 4, edges = [[1,2],[2,3],[2,4]]
#Output: [3,4,0]
#Explanation:
#The subtrees with max distance 1 are: {1,2}, {2,3}, {2,4}.
#The subtrees with max distance 2 are: {1,2,3}, {1,2,4}, {2,3,4}, {1,2,3,4}.
#
#Example 2:
#Input: n = 2, edges = [[1,2]]
#Output: [1]
#
#Example 3:
#Input: n = 3, edges = [[1,2],[2,3]]
#Output: [2,1]
#
#Constraints:
#    2 <= n <= 15
#    edges.length == n - 1
#    edges[i].length == 2
#    1 <= ui, vi <= n
#    All pairs (ui, vi) are distinct.

from typing import List
from collections import defaultdict, deque

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Enumerate all 2^n subsets of cities.
        For each subset:
        1. Check if it forms a connected subtree
        2. If connected, compute max distance (diameter)
        """
        # Build adjacency list (0-indexed)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        def is_connected(mask: int) -> bool:
            """Check if nodes in mask form a connected tree."""
            nodes = [i for i in range(n) if mask & (1 << i)]
            if len(nodes) <= 1:
                return len(nodes) == 1

            # BFS from first node
            start = nodes[0]
            visited = {start}
            queue = deque([start])

            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if (mask & (1 << neighbor)) and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return len(visited) == len(nodes)

        def count_edges(mask: int) -> int:
            """Count edges in the subgraph."""
            count = 0
            nodes = set(i for i in range(n) if mask & (1 << i))
            for u in nodes:
                for v in adj[u]:
                    if v in nodes and u < v:
                        count += 1
            return count

        def get_diameter(mask: int) -> int:
            """Compute diameter (max distance) of subtree."""
            nodes = [i for i in range(n) if mask & (1 << i)]
            if len(nodes) <= 1:
                return 0

            max_dist = 0
            for start in nodes:
                # BFS from start
                dist = {start: 0}
                queue = deque([start])
                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if (mask & (1 << neighbor)) and neighbor not in dist:
                            dist[neighbor] = dist[node] + 1
                            max_dist = max(max_dist, dist[neighbor])
                            queue.append(neighbor)

            return max_dist

        result = [0] * (n - 1)

        # Enumerate all subsets with at least 2 nodes
        for mask in range(3, 1 << n):
            nodes = [i for i in range(n) if mask & (1 << i)]
            node_count = len(nodes)

            if node_count < 2:
                continue

            # A tree with k nodes has k-1 edges
            edge_count = count_edges(mask)
            if edge_count != node_count - 1:
                continue  # Not a tree

            if not is_connected(mask):
                continue

            diameter = get_diameter(mask)
            if 1 <= diameter <= n - 1:
                result[diameter - 1] += 1

        return result


class SolutionFloydWarshall:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Use Floyd-Warshall for distance computation.
        """
        # Build distance matrix using Floyd-Warshall
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u, v in edges:
            dist[u - 1][v - 1] = dist[v - 1][u - 1] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        result = [0] * (n - 1)

        for mask in range(3, 1 << n):
            nodes = [i for i in range(n) if mask & (1 << i)]
            k = len(nodes)

            if k < 2:
                continue

            # Check connectivity and count edges
            edges_in_sub = 0
            diameter = 0

            for i, u in enumerate(nodes):
                for j, v in enumerate(nodes):
                    if i < j:
                        if dist[u][v] == 1:
                            edges_in_sub += 1
                        # Max distance within subset
                        if dist[u][v] < INF:
                            diameter = max(diameter, dist[u][v])

            # Valid tree: k-1 edges
            if edges_in_sub == k - 1:
                result[diameter - 1] += 1

        return result
