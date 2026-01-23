#684. Redundant Connection
#Medium
#
#In this problem, a tree is an undirected graph that is connected and has no
#cycles.
#
#You are given a graph that started as a tree with n nodes labeled from 1 to n,
#with one additional edge added. The added edge has two different vertices
#chosen from 1 to n, and was not an edge that already existed. The graph is
#represented as an array edges of length n where edges[i] = [ai, bi] indicates
#that there is an edge between nodes ai and bi in the graph.
#
#Return an edge that can be removed so that the resulting graph is a tree of n
#nodes. If there are multiple answers, return the answer that occurs last in
#the input.
#
#Example 1:
#Input: edges = [[1,2],[1,3],[2,3]]
#Output: [2,3]
#
#Example 2:
#Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
#Output: [1,4]
#
#Constraints:
#    n == edges.length
#    3 <= n <= 1000
#    edges[i].length == 2
#    1 <= ai < bi <= edges.length
#    ai != bi
#    There are no repeated edges.
#    The given graph is connected.

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """
        Union-Find: the first edge that connects two already-connected nodes
        is the redundant edge.
        """
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # Already connected

            # Union by rank
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []


class SolutionDFS:
    """DFS approach: check if path exists before adding edge"""

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        from collections import defaultdict

        graph = defaultdict(set)

        def has_path(source, target, visited):
            if source == target:
                return True
            visited.add(source)
            for neighbor in graph[source]:
                if neighbor not in visited:
                    if has_path(neighbor, target, visited):
                        return True
            return False

        for u, v in edges:
            if has_path(u, v, set()):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)

        return []
