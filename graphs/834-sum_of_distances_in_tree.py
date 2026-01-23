#834. Sum of Distances in Tree
#Hard
#
#There is an undirected connected tree with n nodes labeled from 0 to n - 1 and
#n - 1 edges.
#
#You are given the integer n and the array edges where edges[i] = [ai, bi]
#indicates that there is an edge between nodes ai and bi in the tree.
#
#Return an array answer of length n where answer[i] is the sum of the distances
#between the ith node and all other nodes in the tree.
#
#Example 1:
#Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
#Output: [8,12,6,10,10,10]
#
#Example 2:
#Input: n = 1, edges = []
#Output: [0]
#
#Example 3:
#Input: n = 2, edges = [[1,0]]
#Output: [1,1]
#
#Constraints:
#    1 <= n <= 3 * 10^4
#    edges.length == n - 1
#    edges[i].length == 2
#    0 <= ai, bi < n
#    ai != bi
#    The given input represents a valid tree.

from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        """
        Two DFS passes:
        1. Compute subtree sizes and sum of distances for root
        2. Propagate to all nodes using relationship:
           When moving from parent to child:
           answer[child] = answer[parent] - count[child] + (n - count[child])
        """
        if n == 1:
            return [0]

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n  # Subtree size
        answer = [0] * n

        # DFS 1: Compute count[] and answer[0]
        def dfs1(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs1(child, node)
                    count[node] += count[child]
                    answer[node] += answer[child] + count[child]

        # DFS 2: Propagate answer to all nodes
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    # Moving from node to child:
                    # - count[child] nodes get closer by 1
                    # - (n - count[child]) nodes get farther by 1
                    answer[child] = answer[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs1(0, -1)
        dfs2(0, -1)

        return answer


class SolutionIterative:
    """Iterative version using topological processing"""

    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        from collections import deque

        graph = defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Process leaves first (like topological sort)
        count = [1] * n
        answer = [0] * n
        parent = [-1] * n

        # BFS from root to establish parent relationships
        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for child in graph[node]:
                if not visited[child]:
                    visited[child] = True
                    parent[child] = node
                    queue.append(child)

        # Process in reverse order (leaves to root)
        for node in reversed(order):
            for child in graph[node]:
                if parent[child] == node:
                    count[node] += count[child]
                    answer[node] += answer[child] + count[child]

        # Process in order (root to leaves)
        for node in order:
            if parent[node] != -1:
                p = parent[node]
                answer[node] = answer[p] - count[node] + (n - count[node])

        return answer
