#1377. Frog Position After T Seconds
#Hard
#
#Given an undirected tree consisting of n vertices numbered from 1 to n. A frog
#starts jumping from vertex 1. In one second, the frog jumps from its current
#vertex to another unvisited vertex if they are directly connected. The frog
#can not jump back to a visited vertex. In case the frog can jump to several
#vertices, it jumps randomly to one of them with the same probability. Otherwise,
#when the frog can not jump to any unvisited vertex, it jumps forever on the
#same vertex.
#
#The edges of the undirected tree are given in the array edges, where
#edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.
#
#Return the probability that after t seconds the frog is on the vertex target.
#Answers within 10^-5 of the actual answer will be accepted.
#
#Example 1:
#Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
#Output: 0.16666666666666666
#Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666.
#
#Example 2:
#Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
#Output: 0.3333333333333333
#Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1.
#
#Constraints:
#    1 <= n <= 100
#    edges.length == n - 1
#    edges[i].length == 2
#    1 <= ai, bi <= n
#    1 <= t <= 50
#    1 <= target <= n

from typing import List
from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        """
        BFS tracking probability at each node.
        """
        if n == 1:
            return 1.0 if target == 1 else 0.0

        # Build adjacency list
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # BFS with probability
        visited = {1}
        queue = deque([(1, 1.0)])  # (node, probability)

        for _ in range(t):
            if not queue:
                break

            next_queue = deque()

            for _ in range(len(queue)):
                node, prob = queue.popleft()

                # Find unvisited neighbors
                neighbors = [nbr for nbr in adj[node] if nbr not in visited]

                if not neighbors:
                    # Frog stays here
                    if node == target:
                        return prob
                    continue

                # Jump to each neighbor with equal probability
                new_prob = prob / len(neighbors)
                for nbr in neighbors:
                    visited.add(nbr)
                    if nbr == target and _ == len(queue) - 1:
                        # Check if we can stay at target
                        pass
                    next_queue.append((nbr, new_prob))

            queue = next_queue

        # After t seconds, check if frog is at target
        for node, prob in queue:
            if node == target:
                # Check if frog can stay (no unvisited neighbors)
                neighbors = [nbr for nbr in adj[node] if nbr not in visited]
                if not neighbors:
                    return prob
                return 0.0  # Frog would have jumped away

        return 0.0


class SolutionDFS:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        """DFS approach"""
        if n == 1:
            return 1.0 if target == 1 else 0.0

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, parent, time, prob):
            # Get children (neighbors except parent)
            children = [nbr for nbr in adj[node] if nbr != parent]

            if node == target:
                # At target: return prob if we can stay here
                if time == 0 or not children:
                    return prob
                return 0.0  # Still have time but must jump

            if time == 0 or not children:
                return 0.0  # Out of time or dead end

            # Try each child
            child_prob = prob / len(children)
            for child in children:
                result = dfs(child, node, time - 1, child_prob)
                if result > 0:
                    return result

            return 0.0

        return dfs(1, -1, t, 1.0)
