#261. Graph Valid Tree
#Medium
#
#You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n
#and a list of edges where edges[i] = [ai, bi] indicates that there is an
#undirected edge between nodes ai and bi in the graph.
#
#Return true if the edges of the given graph make up a valid tree, and false
#otherwise.
#
#Example 1:
#Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
#Output: true
#
#Example 2:
#Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
#Output: false
#
#Constraints:
#    1 <= n <= 2000
#    0 <= edges.length <= 5000
#    edges[i].length == 2
#    0 <= ai, bi < n
#    ai != bi
#    There are no self-loops or repeated edges.

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n-1 edges and be connected
        if len(edges) != n - 1:
            return False

        # Check if graph is connected using Union-Find
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # Cycle detected
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        for a, b in edges:
            if not union(a, b):
                return False

        return True

    # DFS approach
    def validTreeDFS(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        from collections import defaultdict
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # DFS to check connectivity
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False  # Cycle
                if not dfs(neighbor, node):
                    return False
            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Check if all nodes are visited (connected)
        return len(visited) == n

    # BFS approach
    def validTreeBFS(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        from collections import defaultdict, deque

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = {0}
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == n
